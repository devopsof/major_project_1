from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/health")
def health():
    return jsonify(status="ok", message="App is running")

@app.route("/api/data")
def api_data():
    sample_data = {
        "project": "Flask CI/CD Demo",
        "version": "1.0",
        "status": "running"
    }
    return jsonify(sample_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
