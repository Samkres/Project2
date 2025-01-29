import json
from datetime import datetime, timedelta

# Functie om BTW-bedrag af te ronden volgens de richtlijnen van de Belastingdienst
def round_tax(amount):
    return round(amount, 2)

# Pad naar het order JSON-bestand
file_path = 'C:/Users/samkr/OneDrive/Documenten/GitHub/Project2/order.json'

# Lees het order JSON-bestand in
with open(file_path, 'r') as file:
    order_data = json.load(file)

# Extraheer relevante gegevens
order_id = order_data['order_id']
customer = order_data['customer']
items = order_data['items']
order_date = order_data['order_date']

# Bereken subtotaal, BTW, en totaalbedrag
subtotal = sum(item['quantity'] * item['unit_price'] for item in items)
vat_rate = 0.21  # 21% BTW
vat_amount = round_tax(subtotal * vat_rate)
total_amount = round_tax(subtotal + vat_amount)

# Genereer factuurdatum (huidige datum)
invoice_date = datetime.now().strftime('%Y-%m-%d')

# Maak de factuur JSON-structuur
invoice_data = {
    "invoice_id": f"INV-{order_id}",
    "invoice_date": invoice_date,
    "customer": customer,
    "items": items,
    "subtotal": subtotal,
    "vat_rate": vat_rate,
    "vat_amount": vat_amount,
    "total_amount": total_amount,
    "payment_due_date": (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d')  # Betalingstermijn van 30 dagen
}

# Sla de factuur op in een nieuw JSON-bestand
with open('C:/Users/samkr/OneDrive/Documenten/GitHub/Project2/invoice.json', 'w') as file:
    json.dump(invoice_data, file, indent=4)

print("Factuur JSON-bestand is succesvol gegenereerd!")