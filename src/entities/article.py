import datetime
import requests

from bs4 import BeautifulSoup
from gensim.summarization import summarize, keywords
from sqlalchemy import Column, String, Integer, Text, DateTime
from sqlalchemy.orm import relationship
from base import Base
from entities.keyword import Keyword
from typing import List


class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    headline = Column('headline', String(255))
    article_url = Column('article_url', String(255))
    publication_url = Column('publication_url', String(255))
    keywords = relationship("Keyword", backref='articles')

    summary = Column('summary', Text)
    summarised_date = Column('summarised_date', DateTime, default=datetime.datetime.utcnow)

    keyword_list = []
    text = ''

    def __init__(self, headline: str, url: str, key: str):
        self.headline = headline
        self.article_url = url
        self.selector = key

        self.summary = ''

    def __str__(self):
        return f"Article: {self.headline}\n" \
               f"Keywords: {[word.keyword for word in self.keywords]}\n" \
               f"Summary Length: {len(self.summary)}\n\n"

    def read(self) -> str:
        if self.text:
            return self.text

        page = requests.get(self.article_url).text
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

        self.keyword_list = keywords(self.text, words=10, lemmatize=True).split('\n')
        self.keywords = [Keyword(word) for word in self.keyword_list]

        return self.keywords
