from urllib.request import urlopen 
from bs4 import BeautifulSoup
import re

class Scraper():
    Newlines = re.compile(r'[\r\n]\s+')
    
    def __init__(self):
        pass

    def scrape_url_text_content(self,url = 'https://tr.wordpress.org/'):
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
    
    pass
