from flask import Flask, request, jsonify
import math
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(
    filename="server2.log",  # Log file for Server 2
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

@app.route('/calculate', methods=['POST'])
def calculate_distance():
    try:
        # Receive input data
        data = request.get_json()
        logging.info(f"Received input: {data}")

        # Extract parameters
        P_t = data.get("Pt")
        G_t = data.get("Gt")
        G_r = data.get("Gr")
        P_r = data.get("Pr")
        wavelength = data.get("wavelength")

        # Validate inputs
        if None in (P_t, G_t, G_r, P_r, wavelength):
            error_msg = "Missing one or more required inputs."
            logging.error(error_msg)
            return jsonify({"error": error_msg}), 400
        if not (1 <= P_t <= 50):
            error_msg = "Pt (transmitted power) must be between 1 and 50."
            logging.error(error_msg)
            return jsonify({"error": error_msg}), 400
        if P_r <= 0 or wavelength <= 0:
            error_msg = "Pr and wavelength must be greater than 0."
            logging.error(error_msg)
            return jsonify({"error": error_msg}), 400

        # Calculate distance (D)
        numerator = P_t * G_t * G_r * (wavelength ** 2)
        denominator = 4 * math.pi * P_r
        D = math.sqrt(numerator / denominator)

        # Validate output (D)
        if not (100 <= D <= 5000):
            error_msg = f"Calculated distance (D) is out of range: {D}."
            logging.error(error_msg)
            return jsonify({"error": error_msg}), 400

        # Log the successful calculation
        logging.info(f"Calculated distance: {D}")
        
        # Return successful response
        return jsonify({
            "Pt": P_t,
            "Gt": G_t,
            "Gr": G_r,
            "Pr": P_r,
            "wavelength": wavelength,
            "D": D
        })

    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        return jsonify({"error": "An unexpected error occurred"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)