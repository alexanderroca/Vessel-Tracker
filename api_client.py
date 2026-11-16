# api_client.py
import json
import websockets
from config import AISSTREAM_API_KEY, MED_BOUNDING_BOX

async def listen_mediterranean_stream(callback_function):
    """
    Se conecta al stream de AISStream y emite cada barco detectado en el Mediterráneo.
    """
    if not AISSTREAM_API_KEY:
        print("❌ Error: Falta AISSTREAM_API_KEY en el archivo .env")
        return

    subscription_message = {
        "APIKey": AISSTREAM_API_KEY,
        "BoundingBoxes": [MED_BOUNDING_BOX],
        "FilterMessageTypes": ["PositionReport"]
    }

    print("🔌 Conectando al stream de AISStream (Mediterráneo)...")
    print("⏳ Esperando tráfico marítimo en tiempo real (puede tardar unos segundos)...")
    
    async with websockets.connect("wss://stream.aisstream.io/v0/stream", compression="deflate") as ws:
        await ws.send(json.dumps(subscription_message))
        
        async for payload in ws:
            try:
                message = json.loads(payload)
                msg_type = message.get("MessageType")
                
                if msg_type == "PositionReport":
                    metadata = message.get("MetaData", {})
                    mmsi = str(metadata.get("MMSI"))
                    ship_name = metadata.get("ShipName", "Desconocido").strip()
                    
                    position_data = message.get("Message", {}).get("PositionReport", {})
                    
                    vessel_info = {
                        "mmsi": mmsi,
                        "name": ship_name,
                        "latitude": position_data.get("Latitude"),
                        "longitude": position_data.get("Longitude"),
                        "sog": position_data.get("Sog"),
                        "cog": position_data.get("Cog")
                    }
                    
                    # Envía los datos capturados a la función principal
                    callback_function(vessel_info)
                        
            except Exception as e:
                print(f"⚠️ Error procesando mensaje del stream: {e}")