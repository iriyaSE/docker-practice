from flask import Flask
from redis import Redis

app = Flask(__name__)

redis = Redis(host='redis-db', port=6379)

@app.route('/')
def home():
    count = redis.incr('hits')
    return f"<h1>Hello, Goorm</h1><h2>Visit Count: {count}</h2>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
