import datetime
import mongoengine as mdb

mdb.connect('fresh', username='root', password='toor', authentication_source='admin')


class Article(mdb.Document):
    parent_publication = mdb.StringField(required=True)

    url = mdb.StringField(required=True)
    title = mdb.StringField(required=True)
    
    summary = mdb.StringField()
    summarized = mdb.DateTimeField(default=datetime.datetime.now)

    keywords = mdb.ListField(mdb.StringField())


a = Article(
    parent_publication='https://medium.com',
    url='whatever article url',
    title='Whatever clickbaity article title'
)

a.save()

print(Article.objects()[0].title)
print(Article.objects().count())
