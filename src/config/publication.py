# Should contain a definition for each of the objects
# in the config list so they can be translated into
# python code.
# ----
# Should probably contain the full index page with all
# articles and every time you need to parse a new one
# this is where you come to get it. So 'bs4' and 'requests'
# magic happens in here.
import requests

from bs4 import BeautifulSoup
from typing import List


class Publication:

    def __init__(self, name: str, info: dict):
        self.selectors = {
            'headline': info['heading'],
            'text': info['text'],
            'url': info['url']
        }
        self.home = info['index']

        # List of article urls parsed from home page
        self.articles = self.collect_articles()


    def selector(self, name: str):
        if name in self.selectors:
            return self.selectors[name]
        
        print('Selector id not found')
        

    def collect_articles(self) -> List[str]:
        text = requests.get(self.home).text
        soup = BeautifulSoup(text, features='html.parser')

        a_links = [ tag['href'] for tag in soup.select(self.selector('url')) ]
        full_links = [ self.home + link for link in a_links ]

        return full_links