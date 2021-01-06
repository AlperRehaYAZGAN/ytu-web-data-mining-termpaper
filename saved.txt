# app.py
from flask import Flask, request, jsonify
app = Flask(__name__)

# NLP Start

from rake_nltk import Rake

r = Rake() # Uses stopwords for english from NLTK, and all puntuation characters.

# r.extract_keywords_from_text("Hello from Alper")
# r.get_ranked_phrases() # To get keyword phrases ranked highest to lowest.

# Uses stopwords for english from NLTK, and all puntuation characters.
# NLP ENDS

import trafilatura

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)

# A welcome message to test our server
@app.route('/')
def index():
    return "<h3>Web Data Mining Project</h3><br> <h4>18011020 - Alper Reha YAZGAN</h4><br> <h4>Web site will be available when project is ready.</h4>"



@app.route('/from/text', methods=['POST'])
def analysis_from_text():
    # Retrieve the name from url parameter
    response = {}
    response["ERROR"] = "no name found, please send a name."
    return jsonify(response)


@app.route('/from/url', methods=['GET'])
def analysis_from_url_get():
    # param = request.form.get('text')
    # print(param)
    downloaded = trafilatura.fetch_url('http://adrien.barbaresi.eu/blog/trafilatura-main-text-content-python.html')
    result = trafilatura.extract(downloaded)
    text3="NLTK, bir veri setinin ön işlemesini(preprocessing), yani veriyi makinenin anlayacağı hale getireceğimiz zaman bizi gereksiz kelimelerle uğraştırmaktan da kurtarıyor. Aslında gereksiz demek biraz yanlış oluyor, sadece öznitelik çıkarımı yaparken önemli olmayan kelimelerle(ben, sen, de, da, ki, ile vs) uğraştırmaktan kurtarıyor. Gelin NLTK’nın bize sağladığı bu güzelliği de deneyelim, Türkçe içinde destekliyor hem"
    r.extract_keywords_from_text(text3)    
    return jsonify(result)


@app.route('/from/url', methods=['POST'])
def analysis_from_url():
    # param = request.form.get('text')
    # print(param)
    text1 = "Avengers: Infinity War was a 2018 American superhero film based on the Marvel Comics superhero team the Avengers. It is the 19th film in the Marvel Cinematic Universe (MCU). The running time of the movie was 149 minutes and the box office collection was around 2 billion dollars. (Source: Wikipedia)"
    r.extract_keywords_from_text(text1)
    
    r.get_ranked_phrases() # To get keyword phrases ranked highest to lowest.
    return "Succes"

