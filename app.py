from flask import Flask, render_template

app = Flask(__name__)

menu = [
    {"name": "Espresso",   "price": "$2.50", "emoji": "☕", "desc": "Strong & bold shot"},
    {"name": "Cappuccino", "price": "$3.50", "emoji": "🍵", "desc": "Espresso with milk foam"},
    {"name": "Latte",      "price": "$4.00", "emoji": "🥛", "desc": "Smooth espresso with milk"},
    {"name": "Cold Brew",  "price": "$4.50", "emoji": "🧊", "desc": "Slow-steeped cold coffee"},
    {"name": "Mocha",      "price": "$4.50", "emoji": "🍫", "desc": "Espresso with chocolate"},
    {"name": "Iced Latte", "price": "$4.00", "emoji": "🥤", "desc": "Chilled latte over ice"},
]

@app.route("/")
def home():
    return render_template("index.html", menu=menu)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
