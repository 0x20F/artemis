# Should contain a definition for each of the objects
# in the config list so they can be translated into
# python code.
# ----
# Should probably contain the full index page with all
# articles and every time you need to parse a new one
# this is where you come to get it. So 'bs4' and 'requests'
# magic happens in here.

class Publication:

    def __init__(self, name: str, info: dict):
        self.selectors = {
            'headline': info['heading'],
            'text': info['text'],
            'url': info['url']
        }
        self.home = info['index']


    def selector(self, name: str):
        if name in self.selectors:
            return self.selectors[name]
        
        print('Selector id not found')
        
