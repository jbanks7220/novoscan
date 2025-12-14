from flask import Flask, render_template, request
from scanner.safe_scan import run_safe_scan

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    if request.method == "POST":
        target = request.form["target"]
        profile = request.form["profile"]
        results = run_safe_scan(target, profile)
    return render_template("report.html", results=results)

app.run(debug=True)
