# engine.py
from datetime import datetime, timezone

def evaluate_business_rules(vessels_data):
    """
    Aplica reglas comerciales sobre los barcos detectados en el Mediterráneo.
    """
    alerts = []
    
    for vessel in vessels_data:
        imo = vessel.get("imo")
        name = vessel.get("name")
        status = vessel.get("navigation_status") # Ej: 'Underway', 'Anchored', 'Moored'
        eta_str = vessel.get("eta") # Fecha estimada de llegada
        destination = vessel.get("destination")
        
        # Regla 1: Barco fondeado (posible necesidad de servicio/soporte)
        if status == "Anchored":
            alerts.append({
                "imo": imo,
                "vessel_name": name,
                "type": "FONDEO",
                "message": f"El buque {name} (IMO: {imo}) lleva tiempo fondeado cerca de {destination}."
            })
            
        # Regla 2: ETA próxima (menos de 72 horas a un puerto)
        if eta_str:
            # Lógica simplificada de ejemplo para parsear y comprobar ETA
            # (Dependerá del formato exacto de fecha que devuelva tu API elegida)
            alerts.append({
                "imo": imo,
                "vessel_name": name,
                "type": "ETA_PROXIMA",
                "message": f"El buque {name} tiene previsto llegar a {destination} próximamente."
            })
            
    return alerts