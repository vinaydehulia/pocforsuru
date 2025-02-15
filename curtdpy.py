from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data storage
data = []

# Create - Add new item to the list
@app.route('/create', methods=['POST'])
def create():
    item = request.json.get('item')
    if item:
        data.append(item)
        return jsonify({"message": f"Item '{item}' added successfully."}), 201
    return jsonify({"message": "Item is required."}), 400

# Read - Get all items
@app.route('/read', methods=['GET'])
def read():
    return jsonify({"data": data}), 200

# Update - Modify an item at a specific index
@app.route('/update/<int:index>', methods=['PUT'])
def update(index):
    if 0 <= index < len(data):
        new_item = request.json.get('item')
        if new_item:
            data[index] = new_item
            return jsonify({"message": f"Item at index {index} updated to '{new_item}'."}), 200
        return jsonify({"message": "New item is required."}), 400
    return jsonify({"message": "Invalid index."}), 404

# Delete - Remove an item from the list
@app.route('/delete/<int:index>', methods=['DELETE'])
def delete(index):
    if 0 <= index < len(data):
        removed_item = data.pop(index)
        return jsonify({"message": f"Item '{removed_item}' at index {index} deleted."}), 200
    return jsonify({"message": "Invalid index."}), 404

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
