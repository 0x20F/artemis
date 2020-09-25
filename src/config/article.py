# Build an article based on the data
# collected from urls inside a publication

class Article:

    def __init__(self, info: tuple, key: str):
        self.headline = info[0]
        self.url = info[1]

        print('New article: {}'.format(self.headline))
        print('Text should be in: {}'.format(key))
        