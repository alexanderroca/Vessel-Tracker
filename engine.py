# engine.py

def evaluate_business_rules(vessels_data):
    """
    Evalúa los datos actuales de los barcos y genera alertas comerciales.
    """
    alerts = []
    
    for vessel in vessels_data:
        imo = vessel.get("imo")
        name = vessel.get("name", "Desconocido")
        status = vessel.get("navigation_status") # Ej: 'Underway', 'Anchored'
        destination = vessel.get("destination", "No especificado")
        eta = vessel.get("eta", "No disponible")
        
        # Regla 1: Barco fondeado (posible necesidad de servicio o soporte)
        if status and status.lower() == "anchored":
            alerts.append({
                "imo": imo,
                "vessel_name": name,
                "type": "FONDEO",
                "message": f"El buque {name} está fondeado cerca de {destination}."
            })
            
        # Regla 2: Barco con destino declarado activo (actividad comercial detectada)
        if destination and destination != "No especificado":
            alerts.append({
                "imo": imo,
                "vessel_name": name,
                "type": "DESTINO_ACTIVO",
                "message": f"El buque {name} navega hacia {destination} (ETA: {eta})."
            })
            
    return alerts