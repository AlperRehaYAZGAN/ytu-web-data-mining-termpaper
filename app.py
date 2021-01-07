# app.py
from flask import Flask, request, jsonify, send_from_directory, send_file, render_template
from services.controller import BaseController
from services.database import Sqlite


app = Flask(__name__)
controller = BaseController()
database = Sqlite()

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
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    text = str(request.form['searchtext'])
    
    if(text):
        if("," in text):
            rows = database.find(text.split(','))
            if(rows):
                return render_template("search.html",rows = rows,msg = "Aramanıza Uygun Sonuçlar Aşağıda Listelenmektedir.")
            else:
                return render_template("search.html",rows = rows,msg = "Maalesef aramanıza uygun bir sonuç bulunamadı.")
        else:
            results = controller.get_keywords_from_url(text)
            database.save(text,results)
            return render_template("query.html",rows = results, url = text)
        pass
    else:
        return render_template('index.html')
    
    
@app.route('/all', methods=['GET'])
def all():
    rows = database.all()
    print(rows)
    return render_template("search.html",rows = rows, msg = "Sisteme kayıtlı bütün anahtar kelimeleri ve referanslarını görmektesiniz.")

@app.route('/api/text', methods=['POST'])
def from_text():
    text = str(request.form['text'])
    return jsonify({"keywords" : controller.get_keywords_from_text(text)})


