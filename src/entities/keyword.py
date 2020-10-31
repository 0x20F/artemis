from sqlalchemy import Column, String, Integer, ForeignKey
from base import Base


class Keyword(Base):
    __tablename__ = 'keywords'

    id = Column(Integer, primary_key=True)
    article_id = Column('article_id', Integer, ForeignKey('articles.id'))
    keyword = Column('keyword', String(255))

    def __init__(self, keyword: str):
        self.keyword = keyword

    def __str__(self):
        return self.keyword
