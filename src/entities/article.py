import datetime
from sqlalchemy import Column, String, Integer, Text, DateTime
from ..base import Base


class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    headline = Column(String)
    article_url = Column(String)
    publication_url = Column(String)
    keywords = Column(String) # This is a list so maybe make it nicer

    summary = Column(Text)
    summarised_date = Column(DateTime, default=datetime.datetime.utcnow)

