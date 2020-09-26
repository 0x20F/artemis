# Build an article based on the data
# collected from urls inside a publication
import requests

from bs4 import BeautifulSoup
from gensim.summarization import summarize, keywords
from typing import List


class Article:

    def __init__(self, headline: str, url: str, key: str):
        self.headline = headline
        self.url = url
        self.selector = key

        self.text = ''
        self.summary = ''
        self.keyword_list = []

    
    def read(self) -> str:
        if self.text:
            return self.text

        page = requests.get(self.url).text
        soup = BeautifulSoup(page, features='html.parser')

        text_tags = [ tag.get_text().strip() for tag in soup.select(self.selector) ]
        sentences = [ sentence for sentence in text_tags if not '\n' in sentence ]
        sentences = [ sentence for sentence in sentences if '.' in sentence ]

        self.text = ' '.join(sentences)
        return self.text


    def summarize(self) -> str:
        if self.summary:
            return self.summary

        if not self.text:
            self.read()

        # Ratio should be based on the article length I guess?
        self.summary = summarize(self.text, ratio=0.2)
        return self.summary

    
    def keywords(self) -> List[str]:
        if len(self.keyword_list) > 0:
            return self.keyword_list

        if not self.text:
            self.read()

        self.keyword_list = keywords(self.text).split('\n')
        return self.keyword_list
        