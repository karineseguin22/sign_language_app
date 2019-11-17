from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route("/output")
def output():
	return jsonify ({ "data" :"Hello World!" })

if __name__ == "__main__":
	app.run()