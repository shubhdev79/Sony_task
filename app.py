# HOST THE APP on EC2 Machine

from flask import Flask, jsonify

app = Flask(__name__)

# Endpoint to check the health of the service
@app.route('/', methods=['GET'])
def health_check():
    status = {
        "status": "healthy"
    }
    return jsonify(status), 200

@app.route("/")
def hello():
    return "Displaying Page";

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=XXXX)
