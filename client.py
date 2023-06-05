from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    if request.method == "POST":
        formula = request.form.get("formula")

        if formula == 'q':
            return "You have chosen to quit. Goodbye!"

        response = requests.post("http://localhost:8000/calculate", json={"formula": formula})

        if response.status_code == 200:
            result = response.text
        else:
            result = "Error: " + response.text

        return render_template("result.html", formula=formula, result=result)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=8001)
