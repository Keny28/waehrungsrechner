 from django.shortcuts import render

def index(request):
    result_eur_to_egp = None
    result_egp_to_eur = None
    amount_eur = None
    amount_egp = None
    rate = 33  # Beispiel-Wechselkurs

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'eur_to_egp':
            try:
                amount_eur = float(request.POST.get('amount_eur', '0'))
                result_eur_to_egp = round(amount_eur * rate, 2)
            except ValueError:
                result_eur_to_egp = "Ungültiger Betrag"

        elif action == 'egp_to_eur':
            try:
                amount_egp = float(request.POST.get('amount_egp', '0'))
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
