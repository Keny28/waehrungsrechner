from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result_eur_to_egp = None
    result_egp_to_eur = None
    amount_eur = None
    amount_egp = None
    eur_to_egp_rate = 56.81  # Beispielkurs
    egp_to_eur_rate = 1 / eur_to_egp_rate

    if request.method == "POST":
        if request.form["action"] == "eur_to_egp":
            amount_eur = float(request.form["amount_eur"])
            result_eur_to_egp = round(amount_eur * eur_to_egp_rate, 2)
        elif request.form["action"] == "egp_to_eur":
            amount_egp = float(request.form["amount_egp"])
            result_egp_to_eur = round(amount_egp * egp_to_eur_rate, 2)

    return render_template(
        "index.html",
        result_eur_to_egp=result_eur_to_egp,
        result_egp_to_eur=result_egp_to_eur,
        amount_eur=amount_eur,
        amount_egp=amount_egp
    )

if __name__ == "__main__":
    app.run()