from flask import Flask, jsonify
from random import randint

HEXColors = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>This is a random color API</p>"

@app.route("/api/randomcolor", methods=['GET'])
def get_color():
    color = "#"
    for i in range(6):
        color += HEXColors[randint(0,15)]
    return jsonify({"color": color})

if __name__ == "__main__":
    app.run(debug=True)

