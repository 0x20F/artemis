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
article = next(articles)

# Summarize article
summary = article.summarize()
# Get keywords from article
keywords = article.keywords()

print('Article length: {} / Summary length: {}'.format(len(article.text), len(summary)))
print('Found keywords: {}'.format(len(keywords)))
