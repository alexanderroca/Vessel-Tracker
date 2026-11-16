# config.py
import os
from dotenv import load_dotenv

load_dotenv()

AISSTREAM_API_KEY = os.getenv("AISSTREAM_API_KEY")

# Bounding Box completo del Mar Mediterráneo
MED_BOUNDING_BOX = [
    [30.0, -6.0],  # Esquina suroeste (Lat, Lon)
    [46.0, 36.0]   # Esquina noreste (Lat, Lon)
]