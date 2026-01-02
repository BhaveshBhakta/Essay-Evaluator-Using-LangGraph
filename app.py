from flask import Flask, render_template, request
from evaluator import evaluate_essay

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        essay = request.form["essay"]
        if essay.strip():
            result = evaluate_essay(essay)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
