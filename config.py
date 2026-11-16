# config.py
import os
from dotenv import load_dotenv

load_dotenv()

AISSTREAM_API_KEY = os.getenv("AISSTREAM_API_KEY")

# NOTA: AISStream funciona con MMSI para identificar barcos de forma precisa en tiempo real. 
# Debes mapear tus IMO a sus respectivos MMSI. (Ejemplos de placeholder)
TARGET_MMSIS = {
    "228385000": "Artexplorer",  # Reemplaza con el MMSI real de Artexplorer
    "210567000": "Breakthrough"  # Reemplaza con el MMSI real de Breakthrough
}

# Bounding Box del Mediterráneo adaptado al formato de AISStream: [[lat_min, lon_min], [lat_max, lon_max]]
MED_BOUNDING_BOX = [
    [30.0, -6.0],  # Esquina suroeste (Lat, Lon)
    [46.0, 36.0]   # Esquina noreste (Lat, Lon)
]