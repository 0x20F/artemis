import datetime
import requests

from bs4 import BeautifulSoup
from gensim.summarization import summarize, keywords
from sqlalchemy import Column, String, Integer, Text, DateTime
from base import Base
from typing import List


class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    headline = Column(String)
    article_url = Column(String)
    publication_url = Column(String)
    keywords = Column(String) # This is a list so maybe make it nicer

    summary = Column(Text)
    summarised_date = Column(DateTime, default=datetime.datetime.utcnow)

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

        text_tags = [tag.get_text().strip() for tag in soup.select(self.selector)]
        sentences = [sentence for sentence in text_tags if '\n' not in sentence]
        sentences = [sentence for sentence in sentences if '.' in sentence]

        self.text = ' '.join(sentences)
        return self.text

    def summarize(self) -> str:
        if self.summary:
            return self.summary

        if not self.text:
            self.read()

        # Ratio should be based on article length I guess?
        self.summary = summarize(self.text, ratio=0.2)
        return self.summary

    def get_keywords(self) -> List[str]:
        if len(self.keyword_list) > 0:
            return self.keyword_list

        if not self.text:
            self.read()

        self.keyword_list = keywords(self.text).split('\n')
        return self.keyword_list

