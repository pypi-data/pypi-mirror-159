# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['berhoel',
 'berhoel.ctitools',
 'berhoel.ctitools.cti2bibtex',
 'berhoel.ctitools.test']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['cti2bibtex = berhoel.ctitools.cti2bibtex:main']}

setup_kwargs = {
    'name': 'ctitools',
    'version': '0.1.0',
    'description': "Work with cti index files for the Heise papers c't and iX",
    'long_description': 'Ctitools\n========\n\nWork with cti index files for the Heise papers c’t and iX\n\nDescription\n-----------\n\nThis project provides diffrent tool for processing index files from\nHeise papers c’t and iX.\n\nSaving the current base dataset, downloaded from Heise and extractng to\ndata, the commdn\n\n.. code:: shell\n\n  > cti2bibtex data/inhalt.frm result.bibtex\n\ncreates a ``.bib`` file with 82100 entries. Importing this result in\nZotero took more than 28h and use more than 7GB of RAM.\n\nInstallation\n------------\n\nTBD\n\nUsage\n-----\n\nTBD\n\nSupport\n-------\n\nTBD\n\nAuthors and acknowledgment\n--------------------------\n\nNone yet\n\nProject status\n--------------\n\nThis project is in the early planning status.\n',
    'author': 'Berthold Höllmann',
    'author_email': 'berthold@xn--hllmanns-n4a.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://python.xn--hllmanns-n4a.de/ctitools/',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
