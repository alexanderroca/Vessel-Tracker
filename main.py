# main.py
import asyncio
from api_client import listen_mediterranean_stream

def print_vessel_info(vessel):
    """Muestra por pantalla los datos de cada barco que cruza el Mediterráneo."""
    print(f"🚢 Barco detectado -> Nombre: {vessel['name']:<25} | MMSI: {vessel['mmsi']} | Lat: {vessel['latitude']}, Lon: {vessel['longitude']}")

if __name__ == "__main__":
    try:
        # Inicia el bucle asíncrono de escucha continua
        asyncio.run(listen_mediterranean_stream(print_vessel_info))
    except KeyboardInterrupt:
        print("\n🛑 Monitoreo detenido manualmente por el usuario.")