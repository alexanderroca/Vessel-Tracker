# main.py
import asyncio
from api_client import listen_mediterranean_stream
from engine import evaluate_business_rules
from notifier import send_alerts_to_crm

def handle_vessel_event(vessel_data):
    """Callback que se ejecuta instantáneamente al detectar uno de nuestros barcos."""
    print(f"\n🎯 ¡Barco objetivo detectado en el stream!")
    print(f"   • {vessel_data['name']} (MMSI: {vessel_data['mmsi']})")
    print(f"   • Posición: Lat {vessel_data['latitude']}, Lon {vessel_data['longitude']}")
    
    # Evaluar reglas y notificar
    alerts = evaluate_business_rules([vessel_data])
    if alerts:
        send_alerts_to_crm(alerts)

if __name__ == "__main__":
    try:
        # Inicia el bucle asíncrono para escuchar el stream en tiempo real
        asyncio.run(listen_mediterranean_stream(handle_vessel_event))
    except KeyboardInterrupt:
        print("\n🛑 Monitoreo detenido manualmente por el usuario.")