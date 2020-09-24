# Contains the parsing for the configuration file
# that contains all sites that should be scraped
# and how you should go about scraping those sites
from pathlib import Path


class Config:
    
    # Load the configuration file
    def load(self):
        config = Path.joinpath(Path.home(), 'artemis.toml')
        print(config)
        