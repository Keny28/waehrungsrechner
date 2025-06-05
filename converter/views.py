from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def convert_currency(request):
    result = None
    if request.method == 'POST':
        euro_amount = float(request.POST.get('euro_amount', 0))
        rate = 50  # Beispiel-Wechselkurs: 1 Euro = 50 EGP
        result = euro_amount * rate
    return render(request, 'converter/index.html', {'result': result})
from django.shortcuts import render

# Beispiel-Wechselkurs: 1 Euro = 30.9 EGP (Bitte aktuell prüfen!)
EXCHANGE_RATE = 30.9

def index(request):
    result = None

    if request.method == "POST":
        euro_amount = request.POST.get('euro_amount')
        if euro_amount:
            try:
                euro_amount = float(euro_amount)
                result = round(euro_amount * EXCHANGE_RATE, 2)
            except ValueError:
                result = "Ungültiger Betrag!"

    return render(request, 'converter/index.html', {'result': result})
from django.shortcuts import render

def index(request):
    result_eur_to_egp = None
    result_egp_to_eur = None
    amount_eur = None
    amount_egp = None

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'eur_to_egp':
            try:
                amount_eur = float(request.POST.get('amount_eur', 0))
                rate = 33  # Beispielkurs EUR → EGP
                result_eur_to_egp = round(amount_eur * rate, 2)
            except ValueError:
                result_eur_to_egp = "Ungültiger Betrag"

        elif action == 'egp_to_eur':
            try:
                amount_egp = float(request.POST.get('amount_egp', 0))
                rate = 33  # Beispielkurs EUR → EGP
                result_egp_to_eur = round(amount_egp / rate, 2)
            except ValueError:
                result_egp_to_eur = "Ungültiger Betrag"

    context = {
        'result_eur_to_egp': result_eur_to_egp,
        'result_egp_to_eur': result_egp_to_eur,
        'amount_eur': amount_eur,
        'amount_egp': amount_egp,
    }
    return render(request, "converter/index.html", context)
