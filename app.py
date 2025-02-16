from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['POST'])
def receive_data():
    # Get JSON data from the request
    data = request.get_json()

    # Check if data is present
    if not data:
        return jsonify({"error": "No JSON data received"}), 400

    # Process the data (example: echo back the received data)
    response = {
        "message": "Data received successfully",
        "received_data": data
    }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)