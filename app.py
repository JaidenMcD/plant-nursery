from flask import Flask, jsonify, render_template
import adafruit_dht
import board

# Initialize Flask
app = Flask(__name__)

# Initialize the DHT device (using GPIO18 = physical pin 12)
dhtDevice = adafruit_dht.DHT22(board.D18, use_pulseio=False)

@app.route("/")
def dashboard():
    return render_template("index.html")

@app.route("/data")
def get_data():
    try:
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity

        if temperature_c is not None and humidity is not None:
            return jsonify({
                "temperature": round(temperature_c, 2),
                "humidity": round(humidity, 2)
            })
        else:
            return jsonify({"error": "Sensor returned None"}), 500

    except RuntimeError as error:
        # Common for DHT sensors, just retry on next request
        return jsonify({"error": str(error)}), 500
    except Exception as error:
        dhtDevice.exit()
        raise error

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)