import datetime
import mongoengine as mdb


class Article(mdb.Document):
    parent_publication = mdb.StringField(required=True)

    url = mdb.StringField(required=True)
    title = mdb.StringField(required=True)

    summary = mdb.StringField()
    summarized = mdb.DateTimeField(default=datetime.datetime.now)

    keywords = mdb.ListField(mdb.StringField())