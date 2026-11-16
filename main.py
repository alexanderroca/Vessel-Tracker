# main.py
from config import IMO_LIST
from api_client import fetch_vessels_data
from engine import evaluate_business_rules
from notifier import send_alerts_to_crm

def run_tracking_cycle():
    print("--- Iniciando ciclo diario de tracking AIS ---")
    
    if not IMO_LIST:
        print("No hay números IMO configurados en el CRM/config.")
        return

    # 1. Obtener datos actuales filtrados por el Mediterráneo
    vessels_in_med = fetch_vessels_data(IMO_LIST)
    print(f"Barcos de cartera detectados en el Mediterráneo: {len(vessels_in_med)}")
    
    # 2. Evaluar reglas de negocio
    alerts = evaluate_business_rules(vessels_in_med)
    print(f"Alertas comerciales generadas: {len(alerts)}")
    
    # 3. Enviar al CRM
    if alerts:
        send_alerts_to_crm(alerts)
        
    print("--- Ciclo finalizado con éxito ---")

if __name__ == "__main__":
    run_tracking_cycle()