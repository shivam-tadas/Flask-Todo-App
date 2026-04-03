from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Todo app is running"

app.run()