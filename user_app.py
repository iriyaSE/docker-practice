from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/user/<user_id>')
def get_user(user_id):
    users = {"1": "구름", "2": "주원"}
    user_name = users.get(user_id, "Null")
    return jsonify({"user_id": user_id, "user_name": user_name})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
