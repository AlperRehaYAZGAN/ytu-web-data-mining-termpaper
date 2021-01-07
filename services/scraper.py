from urllib.request import urlopen 
from bs4 import BeautifulSoup
import re
import trafilatura

class Scraper():
    Newlines = re.compile(r'[\r\n]\s+')
    
    def __init__(self):
        pass

    def scrape_url_text_content(self,url):
        return self.__get_page_text_content(url)    
        
    def __get_page_text_content(self,url):
        # given a url, get page content
        data = urlopen(url).read()
        # parse as html structured document
        bs = BeautifulSoup(data,"html.parser")
        # kill javascript content
        for s in bs.findAll('script'):
            s.replaceWith('')
        # find body and extract text
        txt = bs.find('body').getText('\n')
        # remove multiple linebreaks and whitespace
        return self.Newlines.sub('\n', txt)
    
    def __get_content_with_trafilatura(self,url):
        downloaded = trafilatura.fetch_url(url)
        return trafilatura.extract(downloaded)
    
    pass
