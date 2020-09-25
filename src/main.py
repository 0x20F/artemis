import requests

from config.sources import Sources

# from bs4 import BeautifulSoup
# from gensim.summarization import summarize, keywords

s = Sources()
p = s.publications()[0]

for a in p.articles():
    print(a.headline)

"""
summary = summarize(article, ratio=0.3)

print('Summary length: {} / Article length: {}'.format(len(article), len(summary)))
print(summary)

print()
print()

print(keywords(summary))"""
