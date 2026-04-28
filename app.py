from flask import Flask, jsonify

app = Flask(__name__)

data = [
    {"name": "A", "age": 25},
    {"name": "B", "age": -5},   # invalid
    {"name": "C", "age": 30}
]

@app.route("/")
def home():
    # return "Mini ETL Running!"
    # return "Mini ETL Updated via CI/CD 🚀"
    return "yuva ETL pipeline"

@app.route("/etl")
def etl():
    valid = []
    invalid = []

    for record in data:
        if record["age"] >= 0:
            valid.append(record)
        else:
            invalid.append(record)

    return jsonify({
        "valid_data": valid,
        "invalid_data": invalid
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)