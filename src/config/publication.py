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

from entities.article import Article


class Publication:

    def __init__(self, name: str, info: dict):
        self.selectors = {
            'headline': info['heading'],
            'text': info['text'],
            'url': info['url']
        }
        self.home = info['home']

        # List of article urls parsed from home page
        self.article_list = self.collect_articles()

    def selector(self, name: str):
        if name in self.selectors:
            return self.selectors[name]

        print('Selector id not found')

    def collect_articles(self) -> List[tuple]:
        text = requests.get(self.home).text
        soup = BeautifulSoup(text, features='html.parser')

        a_tags = soup.select(self.selector('url'))
        a_data = [(tag.get_text(), self.home + tag['href']) for tag in a_tags]

        return a_data

    def articles(self):
        text_key = self.selector('text')

        for headline, url in self.article_list:
            yield Article(headline, url, text_key)
