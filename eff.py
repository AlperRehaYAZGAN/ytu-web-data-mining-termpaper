from rake_nltk import Rake

r = Rake() # Uses stopwords for english from NLTK, and all puntuation characters.

r.extract_keywords_from_text("Hello from Alper")

# r.get_ranked_phrases() # To get keyword phrases ranked highest to lowest.

print(r.get_ranked_phrases())
