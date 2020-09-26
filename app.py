from flask import Flask, jsonify, request

app = Flask(__name__)

Students = [
    {"Bob": "Senior"},
    {"Sara": "Jr"},
    {"Dale": "Sophmore"},
    {"Jess": "Freshman"},
]


@app.route("/")
def hello_world():
    return "Hello, World"


@app.route("/students", methods=["GET"])
def get_students():
    return jsonify({'students': Students})


if __name__ == "__main__":
    app.run(debug=True, port=8080)
