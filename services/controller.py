from services.scraper import Scraper
from services.keywordfinder import KeywordFinder


class BaseController:
    scraper = Scraper()
    keywordFinder = KeywordFinder()
    
    def __init__(self):
        pass
    
    def get_keywords_from_url(self,url):
        textContent = self.scraper.scrape_url_text_content(url=url)
        keywords = self.keywordFinder.find_keyword(textContent)
        return [keywords]
    
    def get_keywords_from_text(self,text):
        keywords = self.keywordFinder.find_keyword(text)
        return [keywords]

    pass
