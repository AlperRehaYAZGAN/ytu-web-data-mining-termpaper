# app.py
from flask import Flask, request, jsonify, send_from_directory
app = Flask(__name__)


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('static/js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('static/css', path)

if __name__ == "__main__":
    app.run()

# A welcome message to test our server
@app.route('/')
def index():
    return "<h3>Web Data Mining Project</h3><br> <h4>18011020 - Alper Reha YAZGAN</h4><br> <h4>Web site will be available when project is ready.</h4>"


