# api_client.py
import requests
from config import API_KEY, API_URL, MED_BOUNDS

def fetch_vessels_data(imo_list):
    """
    Consulta la API para una lista de IMOs y filtra los que están en el Mediterráneo.
    """
    headers = {"Authorization": f"Bearer {API_KEY}"}
    payload = {"imos": imo_list}
    
    try:
        response = requests.post(API_URL, json=payload, headers=headers, timeout=30)
        response.raise_for_status()
        vessels_raw = response.json().get("data", [])
        
        med_vessels = []
        for vessel in vessels_raw:
            lat = vessel.get("latitude")
            lon = vessel.get("longitude")
            
            # Filtrar estrictamente dentro del Bounding Box del Mediterráneo
            if lat and lon and is_in_mediterranean(lat, lon):
                med_vessels.append(vessel)
                
        return med_vessels

    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API de AIS: {e}")
        return []

def is_in_mediterranean(lat, lon):
    return (MED_BOUNDS["lat_min"] <= lat <= MED_BOUNDS["lat_max"]) and \
           (MED_BOUNDS["lon_min"] <= lon <= MED_BOUNDS["lon_max"])