# Contains the parsing for the configuration file
# that contains all sites that should be scraped
# and how you should go about scraping those sites
import toml

from pathlib import Path
from typing import Iterator


class Config:

    # Load the configuration file
    def __init__(self):
        file = Path.joinpath(Path.home(), 'artemis.toml')
        self.config = toml.load(file)


    def publications(self) -> Iterator[dict]:
        return iter(self.config)
        