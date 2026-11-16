# engine.py

def evaluate_business_rules(vessel):
    """
    Evalúa los datos en tiempo real de un buque y genera alertas si cumple condiciones.
    """
    alerts = []
    
    name = vessel.get("name", "Desconocido")
    mmsi = vessel.get("mmsi")
    status = vessel.get("navigation_status") # Estado de navegación (ej: Fondeado, En marcha)
    
    # Ejemplo de regla comercial 1: Detectar si el barco está fondeado
    # (El valor numérico de 'Anchored' o texto depende de cómo devuelva el campo el mensaje AIS)
    if status is not None:
        # Puedes adaptar esta condición según los códigos de estado de AISStream si los necesitas
        pass
        
    # Por ahora, como estamos en fase de captura y descubrimiento de MMSIs, 
    # podemos dejar que devuelva una alerta informativa o simplemente usarlo de pasarela.
    
    return alerts