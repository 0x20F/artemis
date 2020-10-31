from config.artemis import Artemis
from base import Session, engine, Base
from entities.article import Article


# Db Schema
Base.metadata.create_all(engine)

# New Session
session = Session()
artemis = Artemis()

publications = artemis.publications()
print(f"Found {len(publications)} publications")

articles = publications[0].articles()

for article in articles:
    article.summarize()
    article.get_keywords()

    print(article)
    session.add(article)
    break

session.commit()

# Just trying things out
res = session.query(Article)
print(res.count())
print(res[0])

session.close()



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
