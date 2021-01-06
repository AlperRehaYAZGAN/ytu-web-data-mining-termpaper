# app.py
from flask import Flask, request, jsonify
app = Flask(__name__)

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)

# A welcome message to test our server
@app.route('/')
def index():
    return "<h3>Web Data Mining Project</h3><br> <h4>18011020 - Alper Reha YAZGAN</h4><br> <h4>Web site will be available when project is ready.</h4>"