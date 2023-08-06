# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['german_nouns', 'german_nouns.lookup', 'german_nouns.parse_dump']

package_data = \
{'': ['*']}

install_requires = \
['wiktionary-de-parser>=0.9.2,<0.10.0']

setup_kwargs = {
    'name': 'german-nouns',
    'version': '1.2.5',
    'description': 'A list of ~100,000 German nouns and their grammatical properties compiled from WiktionaryDE as CSV file. Plus a module to look up the data and parse compound words.',
    'long_description': "# German nouns\n\nA comma seperated list of ~100 thousand German nouns and their grammatical properties (_tense, number, gender_) as CSV file. Plus a module to look up the data and parse compound words. Compiled from the [WiktionaryDE](https://de.wiktionary.org).\n\nThe list can be found here: [german_nouns/nouns.csv](https://github.com/gambolputty/german-nouns/blob/main/german_nouns/nouns.csv)\n\nIf you want to look up nouns or parse compound words, install this package (for Python 3.8+) and follow the instructions below:\n\n## Installation\n\n`pip install german-nouns`\n\n## Lookup words\n\n```python\nfrom pprint import pprint\nfrom german_nouns.lookup import Nouns\n\nnouns = Nouns()\n\n# Lookup a word\nword = nouns['Fahrrad']\npprint(word)\n\n# Output:\n[{'flexion': {'akkusativ plural': 'Fahrräder',\n              'akkusativ singular': 'Fahrrad',\n              'dativ plural': 'Fahrrädern',\n              'dativ singular': 'Fahrrad',\n              'dativ singular*': 'Fahrrade',\n              'genitiv plural': 'Fahrräder',\n              'genitiv singular': 'Fahrrades',\n              'genitiv singular*': 'Fahrrads',\n              'nominativ plural': 'Fahrräder',\n              'nominativ singular': 'Fahrrad'},\n  'genus': 'n',\n  'lemma': 'Fahrrad',\n  'pos': ['Substantiv']}]\n\n# parse compound word\nwords = nouns.parse_compound('Vermögensbildung')\nprint(words)\n\n# Output:\n['Vermögen', 'Bildung'] # Now lookup nouns['Vermögen'] etc.\n```\n\n## Compiling the list\n\nTo compile the list yourself, you need Python 3.8+ and [Poetry](https://python-poetry.org/) installed.\n\n### 1. Clone the repository and install dependencies with [Poetry](https://python-poetry.org/):\n\n```shell\n$ git clone https://github.com/gambolputty/german-nouns\n$ cd german-nouns\n$ poetry install\n```\n\n### 2. Compile the list of nouns from a Wiktionary XML file:\n\nFind the latest XML-dump files here: [https://dumps.wikimedia.org/dewiktionary/latest](https://dumps.wikimedia.org/dewiktionary/latest), for example [this one](https://dumps.wikimedia.org/dewiktionary/latest/dewiktionary-latest-pages-articles-multistream.xml.bz2) and download it. Then execute:\n\n```shell\n$ poetry run python -m german_nouns.parse_dump /path-to-xml-dump-file.xml.bz2\n```\n\nThe CSV file will be saved here: [german_nouns/nouns.csv](https://github.com/gambolputty/german-nouns/blob/main/german_nouns/nouns.csv).\n\nRemove `german_nouns/index.txt` to let the script recreate the word-index when using the lookup methods.\n\n\n----\n\n[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)\n",
    'author': 'Gregor Weichbrodt',
    'author_email': 'gregorweichbrodt@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/gambolputty/german-nouns',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
