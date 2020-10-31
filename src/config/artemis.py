# Contains the parsing for the configuration file
# that contains all sites that should be scraped
# and how you should go about scraping those sites
import toml

from pathlib import Path
from typing import Iterator

from .publication import Publication


class Artemis:

    # Load the configuration file
    def __init__(self):
        file = Path.joinpath(Path.home(), 'artemis.toml')
        self.config = toml.load(file)

    def publications(self) -> Iterator[Publication]:
        publications = list()

        for name, info in self.config.items():
            publications.append(Publication(name, info))

        return publications
