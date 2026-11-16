# notifier.py

def send_alerts_to_crm(alerts):
    """
    Imprime las alertas en la consola en lugar de enviarlas a un CRM externo.
    """
    print("\n==============================================")
    print(f" 🚨 ALERTAS COMERCIALES DETECTADAS ({len(alerts)})")
    print("==============================================")
    
    for i, alert in enumerate(alerts, 1):
        print(f"\n[Alerta {i}]")
        print(f"  • Barco: {alert['vessel_name']} (IMO: {alert['imo']})")
        print(f"  • Tipo:  {alert['type']}")
        print(f"  • Detalle: {alert['message']}")
        
    print("\n----------------------------------------------")
    print(" (Modo simulación: Webhook de CRM desactivado)")
    print("==============================================\n")