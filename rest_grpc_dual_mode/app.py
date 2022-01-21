from flask import Flask

app = Flask(__name__)

@app.route("/v1/get_message")
def get_message():
    return "This is a REST message!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
    