import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/order/<order_id>')
def get_order(order_id):
    order_info = {"101": {"item": "키보드", "user_id": "1"}, "102": {"item": "마우스", "user_id": "2"}}
    order = order_info.get(order_id)

    if not order:
        return jsonify({"error": "Order not found"}), 404

    user_response = requests.get(f"http://user-service:5000/user/{order['user_id']}")
    user_data = user_response.json()

    return jsonify({
        "order_id": order_id,
        "item": order["item"],
        "customer": user_data["user_name"]
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
