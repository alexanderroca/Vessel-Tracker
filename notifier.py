# notifier.py
import requests

CRM_WEBHOOK_URL = "https://tu-crm.com/api/webhooks/maritime-alerts"

def send_alerts_to_crm(alerts):
    """
    Envía las alertas procesadas al CRM para que cree tareas a los comerciales.
    """
    for alert in alerts:
        payload = {
            "imo": alert["imo"],
            "title": f"Alerta Marítima: {alert['vessel_name']}",
            "description": alert["message"],
            "type": alert["type"]
        }
        
        try:
            response = requests.post(CRM_WEBHOOK_URL, json=payload, timeout=10)
            if response.status_code == 200:
                print(f"Alerta enviada al CRM para el IMO {alert['imo']}")
            else:
                print(f"Error del CRM al registrar alerta: {response.status_code}")
        except Exception as e:
            print(f"Fallo de red al notificar al CRM: {e}")