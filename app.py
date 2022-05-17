from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.get("/")
def index_get():
    return render_template("home.html")


@app.post("/chat")
def chat():
    text = request.get_json().get("message")
    message = {"answer": text}
    return jsonify(message)


if __name__ == "__main__":
    app.run(debug=True)
