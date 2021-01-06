# app.py
from flask import Flask, request, jsonify, send_from_directory, send_file
from services.controller import BaseController

app = Flask(__name__)
controller = BaseController()

def getApp():
    return app


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5001)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('static/js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('static/css', path)

@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('static/images', path)

if __name__ == "__main__":
    app.run()

# A welcome message to test our server
@app.route('/')
def index():
    return send_file('views/index.html')


@app.route('/search', methods=['GET'])
def search_get():
    return jsonify("result")


@app.route('/from/text', methods=['GET'])
def analyze_from_text():
    # Retrieve the name from url parameter
    text = request.form.get('mini')
    return jsonify(text)


@app.route('/from/url', methods=['GET'])
def analyze_from_url_get():
    # param = request.form.get('text')
    # print(param)
    param = request.form.get('url')
    url = request.args.get('url')
    
    return jsonify(param)


@app.route('/from/url', methods=['POST'])
def analyze_from_url_post():
    # param = request.form.get('text')
    # print(param)
    return "Succes"





