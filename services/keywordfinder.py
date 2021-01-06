from rake_nltk import Rake as Rake
from services.scraper import Scraper

class KeywordFinder():    
    rake : Rake
    def __init__(self):
        self.rake = Rake(min_length=1, max_length=10)
        pass    
    
    
    def find_keyword(self,text):
        self.rake.extract_keywords_from_text(text)
        return self.rake.get_ranked_phrases()[0]
    
    
        
    def find_keywords(self,text):
        self.rake.extract_keywords_from_text(text)
        return self.rake.get_ranked_phrases()
    
    
    pass