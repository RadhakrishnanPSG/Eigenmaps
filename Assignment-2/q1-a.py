from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/getip', methods=['GET'])
def get_ip():
    ip = request.remote_addr 
    return jsonify({'ip': ip})

app.run()