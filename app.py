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
if __name__== "__main__":
    app.run(host="0.0.0.0",debug=True)


# from flask import Flask, jsonify
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)

# @app.route('/api/data', methods=['GET'])
# def get_data():
#     data_tuple = ("item1", "item2", "item3")  # Example tuple
#     data = {
#         "message": "hello this is api end point",
#         "data_tuple": data_tuple
#     }
#     return jsonify(data)

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", debug=True)