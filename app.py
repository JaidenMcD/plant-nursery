from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def dashboard():
    return render_template("index.html")

@app.route("/data")
def get_data():
    sensor_value = random.uniform(20.0, 25.0)  # replace with GPIO/I2C read
    return jsonify({"temperature": sensor_value})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)