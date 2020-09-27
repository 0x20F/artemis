from mongoengine import connect


class Database:

    def __init__(self):
        connect('fresh', username='root', password='toor', authentication_source='admin')

