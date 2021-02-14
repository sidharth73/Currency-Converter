from flask import Flask, render_template, request
import requests, json

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/", methods=["GET","POST"])
def hello():
	base = "EUR"
	other = request.form.get("currencyname")
	res = requests.get("http://data.fixer.io/api/latest?access_key=00837a053559c4abb2496fb3a59ac55d&format=1", params={"symbols": other})
	if res.status_code != 200:
		raise Exception("ERROR: API request unsuccessful.")
	data = res.json()
	rate = data["rates"][other]
	return render_template("index.html", rate=rate, other=other)

if __name__=="__main__":
	app.debug = True
	app.run()