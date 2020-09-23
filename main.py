import requests

from bs4 import BeautifulSoup
from gensim.summarization import summarize, keywords


# Retrieve page text
url = 'https://medium.com/@alltopstartups/the-single-best-thing-to-do-with-today-live-immediately-41604a14b6ac'
text = requests.get(url).text


# Soup
soup = BeautifulSoup(text, features='html.parser')

# Headline
headline = soup.select('article section h1')[0].text
# Text from all paragraphs
p_tags_text = [tag.get_text().strip() for tag in soup.select('article section p')]


# Filter out useless text
sentence_list = [sentence for sentence in p_tags_text if not '\n' in sentence]
sentence_list = [sentence for sentence in sentence_list if '.' in sentence]
# Combine them all into a string
article = ' '.join(sentence_list)


summary = summarize(article, ratio=0.3)

print('Summary length: {} / Article length: {}'.format(len(article), len(summary)))
print(summary)

print()
print()

print(keywords(summary))
