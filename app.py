from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/data',methods=['GET'])
def get_data():
    data_tuple = ("item1", "item2", "item3")  # Example tuple
    data = {
        "message":"hello this is api end point"
    }
    return jsonify(data)
