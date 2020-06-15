from flask import Flask, render_template, jsonify
import socket

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return render_template('index.html', hostname=host_name, ip=host_ip)
    except:
        return render_template('error.html')

@app.route('/api', methods=['POST'])
def api():
    return jsonify({"hello": "world"})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
