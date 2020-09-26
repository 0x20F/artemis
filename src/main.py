import requests

from config.sources import Sources
from gensim.summarization import summarize, keywords

# Load in the config
sources = Sources()
# Get all article lists for all fields in the config
publications = sources.publications()

# Get all articles from one publication
articles = publications[0].articles()
# Request all text from an article
article = next(articles).read()


summary = summarize(article, ratio=0.2)

print('Summary length: {} / Article length: {}'.format(len(article), len(summary)))
print(summary)

print()
print()

print(keywords(summary))
