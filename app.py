
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        amount = float(request.form["amount"])
        rate = float(request.form["rate"])
        result = amount * rate
        return f"Umgerechnet: {result}"
    return '''
        <form method="post">
            Betrag: <input name="amount"><br>
            Wechselkurs: <input name="rate"><br>
            <input type="submit" value="Berechnen">
        </form>
    '''

if __name__ == "__main__":
    app.run()