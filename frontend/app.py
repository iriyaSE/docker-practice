import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get("http://order-service:5000/order/101")
    data = response.json()
    
    return render_template('index.html', item=data['item'], customer=data['customer'])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
