# Build an article based on the data
# collected from urls inside a publication

class Article:

    def __init__(self, headline: str, url: str, key: str):
        self.headline = headline
        self.url = url
        