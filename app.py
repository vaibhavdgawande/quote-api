from flask import Flask, jsonify
import random

app = Flask(__name__)

quotes = [
    "The only way to do great work is to love what you do.",
    "Success is not final, failure is not fatal.",
    "Believe you can and you're halfway there.",
    "The future belongs to those who believe in their dreams."
]

@app.route("/")
def home():
    return "Welcome to the Quote API! Try visiting /quote"

@app.route("/quote")
def get_quote():
    quote = random.choice(quotes)
    return jsonify({"quote": quote})

if __name__ == "__main__":
    app.run(debug=True)