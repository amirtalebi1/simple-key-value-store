from flask import Flask, request, jsonify

app = Flask(__name__)

class KeyValueStore:
    def __init__(self):
        self.store = {}

    def set_value(self, key, value):
        self.store[key] = value

    def get_value(self, key):
        return self.store.get(key, None)


kv = KeyValueStore()

@app.route("/set", methods=["POST"])
def set_value():
    data = request.get_json()
    key = data.get("key")
    value = data.get("value")
    if key is None or value is None:
        return jsonify({"error": "Key and value required"}), 400
    kv.set_value(key, value)
    return jsonify({"message": f"{key} set successfully"}), 200

@app.route("/get/<key>", methods=["GET"])
def get_value(key):
    value = kv.get_value(key)
    if value is None:
        return jsonify({"error": "Key not found"}), 404
    return jsonify({"key": key, "value": value}), 200

if __name__ == "__main__":
    app.run(debug=True)

#API TESTED