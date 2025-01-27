from flask import Flask, jsonify, request
import requests
import random
import logging

app = Flask(__name__)

# Server 2's URL (replace with actual IP or hostname)
SERVER_2_URL = "http://192.168.0.7:5001/calculate"

# Set up logging
logging.basicConfig(
    filename="server1.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Function to generate valid inputs
def generate_input():
    return {
        "Gt": random.randint(1, 20),  # Random antenna gain
        "Gr": random.randint(1, 20),  # Random receiver gain
        "Pt": random.randint(1, 50),  # Transmitted power (1 to 50)
        "Pr": round(random.uniform(0.1, 10), 2),  # Received power (0.1 to 10)
        "wavelength": round(random.uniform(0.05, 600), 3)  # Wavelength (0.05 to 600)
    }

@app.route('/send_next_input', methods=['POST'])
def send_next_input():
    try:
        # Generate a new valid input set
        current_input = generate_input()

        # Log the generated input
        logging.info(f"Generated input: {current_input}")

        # Send the input to Server 2
        response = requests.post(SERVER_2_URL, json=current_input)
        if response.status_code == 200:
            result = response.json()
            logging.info(f"Server 2 response: {result}")
        else:
            result = {"error": "Failed to get response from Server 2"}
            logging.error(f"Error from Server 2: {response.text}")

        # Return input and result in HTML format for the browser
        html_response = f"""
        <h1>Generated Input</h1>
        <p>Gt: {current_input['Gt']}</p>
        <p>Gr: {current_input['Gr']}</p>
        <p>Pt: {current_input['Pt']}</p>
        <p>Pr: {current_input['Pr']}</p>
        <p>Wavelength: {current_input['wavelength']}</p>

        <h1>Result from Server 2</h1>
        <p>{result}</p>
        """

        return html_response

    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        return jsonify({"error": "An unexpected error occurred"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)