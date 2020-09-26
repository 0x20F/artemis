# Build an article based on the data
# collected from urls inside a publication
import requests

from bs4 import BeautifulSoup


class Article:

    def __init__(self, headline: str, url: str, key: str):
        self.headline = headline
        self.url = url
        self.selector = key

        self.text = 'aaa'

    
    def read(self) -> str:
        if not self.text:
            return self.text

        page = requests.get(self.url).text
        soup = BeautifulSoup(page, features='html.parser')

        text_tags = [ tag.get_text().strip() for tag in soup.select(self.selector) ]
        sentences = [ sentence for sentence in text_tags if not '\n' in sentence ]
        sentences = [ sentence for sentence in sentences if '.' in sentence ]

        self.text = ' '.join(sentences)
        return self.text