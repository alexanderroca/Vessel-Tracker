# config.py
import os

API_KEY = os.getenv("AIS_API_KEY", "tu_api_key_aqui")
API_URL = "https://api.proveedor-maritimo.com/v1/vessels"  # Ejemplo genérico

# Lista de IMOs de tus clientes en el CRM
IMO_LIST = [
    "9321483",
    "9456782",
    "9123456"
]

# Coordenadas aproximadas del Bounding Box del Mediterráneo (Lat Min/Max, Lon Min/Max)
MED_BOUNDS = {
    "lat_min": 30.0,
    "lat_max": 46.0,
    "lon_min": -6.0,
    "lon_max": 36.0
}