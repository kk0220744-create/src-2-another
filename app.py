# BeastX Web Health Endpoint
from flask import Flask

app = Flask(__name__)

@app.route("/")
def health():
    return "BeastX Bot is running"

if __name__ == "__main__":
    app.run()
