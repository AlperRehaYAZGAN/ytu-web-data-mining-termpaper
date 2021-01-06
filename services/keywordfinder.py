from rake_nltk import Rake as Rake1
from multi_rake import Rake as Rake2
from services.scraper import Scraper

class KeywordFinder():    
    rake : Rake1
    rake_multi : Rake2
    def __init__(self):
        self.rake = Rake1(min_length=1, max_length=10)
        self.rake_multi = Rake2(
            min_chars=3,
            max_words=3,
            min_freq=1,
            language_code=None,  # 'en'
            stopwords=None,  # {'and', 'of'}
            lang_detect_threshold=50,
            max_words_unknown_lang=2,
            generated_stopwords_percentile=80,
            generated_stopwords_max_len=3,
            generated_stopwords_min_freq=2
            )
        pass    
    
    
    def find_keyword(self,text):
        self.rake.extract_keywords_from_text(text)
        return self.rake.get_ranked_phrases()[0]
    
    
        
    def find_keywords(self,text):
        self.rake.extract_keywords_from_text(text)
        return self.rake.get_ranked_phrases()
    
    
    def find_keyword_multi(self,text):
        keywords = self.rake_multi.apply(
            text,
            text_for_stopwords=None,
            )
        return keywords
    
    
    def find_keywords_multi(self,text):
        self.rake.extract_keywords_from_text(text)
        keywords = self.rake_multi.apply(
            text,
            text_for_stopwords=None,
            )
        return keywords
    
    pass