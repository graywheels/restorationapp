from flask import Flask, jsonify, render_template
import random
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quote')
def quote():
    with open('quotes.json') as f:
        quotes = json.load(f)
    return jsonify(random.choice(quotes))

if __name__ == '__main__':
    app.run(debug=True)