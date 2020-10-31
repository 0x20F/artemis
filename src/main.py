from config.sources import Sources
from base import Session, engine, Base


# Db Schema
Base.metadata.create_all(engine)

# New Session
session = Session()
sources = Sources()

publications = sources.publications()
print(f"Found {len(publications)} publications")

articles = publications[0].articles()

for article in articles:
    print(article)
    session.add(article)
    break

session.commit()
session.close()




'''
# Load in the config
sources = Sources()
# Get all article lists for all fields in the config
publications = sources.publications()

# Get all articles from one publication
articles = publications[0].articles()
# Request all text from an article
article = next(articles)


article.summarize()
article.keywords()

print(article.headline)
print(article.url)
print('Article length: {} / Summary length: {}'.format(len(article.text), len(article.summary)))
print('Found keywords: {}'.format(len(article.keyword_list)))'''

'''
Next up
--------
- Should summaries be saved or generated dynamically when needed?
    - Probably saved, the full article can be retrieved from the url if needed
    - Save full url
    - Save publication url
    - Save keywords
    - Save summary
    - Only save once

- How should they be stored? In a database somewhere, probably
    - mongodb so its easier to store arrays and relations?

- How often should the server check for new articles?
    - If the article filtration is done well, meaning only interesting articles get through,
      it can run very often. But since that will require testing and fine-tuning, every hour?
      to start?

- Prefered keywords list needs to be implemented

- Filter articles based on containing keywords in order to decide how
  relevant they actually are to your needs
'''
