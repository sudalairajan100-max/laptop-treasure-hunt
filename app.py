import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

# 🔹 Load CSV file
df = pd.read_csv("laptops_1000.csv")
print(df.columns)
# Convert to list of dictionaries
laptops = df.to_dict(orient="records")

@app.route("/", methods=["GET", "POST"])
def home():
    suggestions = []

    if request.method == "POST":
        budget = int(request.form["budget"])
        ram = int(request.form["ram"])
        processor = request.form["processor"]
        gpu = request.form["gpu"]

        for laptop in laptops:
            if (
                laptop["Price"] <= budget and
                laptop["RAM"] >= ram and
                laptop["Processor"].lower() == processor.lower() and
                laptop["GPU"].lower() == gpu.lower()
            ):
                suggestions.append(laptop)

    return render_template("index.html", suggestions=suggestions)

if __name__ == "__main__":
    app.run(debug=True)