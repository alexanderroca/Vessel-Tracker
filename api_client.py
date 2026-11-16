# api_client.py
import json
import websockets
from config import AISSTREAM_API_KEY, MED_BOUNDING_BOX, TARGET_MMSIS

async def listen_mediterranean_stream(callback_function):
    """
    Se conecta al stream en tiempo real de AISStream filtrando por el Bounding Box del Mediterráneo.
    Ejecuta el callback_function cada vez que detecta un barco de nuestra cartera.
    """
    if not AISSTREAM_API_KEY:
        print("❌ Error: Falta AISSTREAM_API_KEY en el archivo .env")
        return

    subscription_message = {
        "APIKey": AISSTREAM_API_KEY,
        "BoundingBoxes": [MED_BOUNDING_BOX],
        "FilterMessageTypes": ["PositionReport"] # Nos interesa lat, lon, velocidad, estado
    }

    print("🔌 Conectando al stream de AISStream (Mediterráneo)...")
    
    async with websockets.connect("wss://stream.aisstream.io/v0/stream", compression="deflate") as ws:
        await ws.send(json.dumps(subscription_message))
        
        async for payload in ws:
            try:
                message = json.loads(payload)
                msg_type = message.get("MessageType")
                
                if msg_type == "PositionReport":
                    metadata = message.get("MetaData", {})
                    mmsi = str(metadata.get("MMSI"))
                    ship_name = metadata.get("ShipName", "").strip()
                    
                    # Comprobar si el barco detectado está en nuestra lista objetivo por MMSI
                    if mmsi in TARGET_MMSIS:
                        position_data = message.get("Message", {}).get("PositionReport", {})
                        
                        vessel_info = {
                            "mmsi": mmsi,
                            "name": TARGET_MMSIS[mmsi] or ship_name,
                            "latitude": position_data.get("Latitude"),
                            "longitude": position_data.get("Longitude"),
                            "navigation_status": position_data.get("NavigationalStatus"),
                            "sog": position_data.get("Sog"), # Speed Over Ground
                            "cog": position_data.get("Cog")  # Course Over Ground
                        }
                        
                        # Pasamos los datos al motor de reglas/notificador
                        callback_function(vessel_info)
                        
            except Exception as e:
                print(f"⚠️ Error procesando mensaje del stream: {e}")