# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['berhoel',
 'berhoel.get_comics',
 'berhoel.get_comics.dilbert',
 'berhoel.get_comics.garfield',
 'berhoel.get_comics.gen_pdf',
 'berhoel.get_comics.gocomics',
 'berhoel.get_comics.peanuts']

package_data = \
{'': ['*'], 'berhoel.get_comics.gen_pdf': ['template/*']}

install_requires = \
['Pillow>8.0.0',
 'jinja2>3.0.0',
 'lxml>4.5.0',
 'requests>2.23.0',
 'selenium>4.0.0']

entry_points = \
{'console_scripts': ['get_comics = berhoel.get_comics:main',
                     'get_dilbert = berhoel.get_comics.dilbert:main',
                     'get_garfield = berhoel.get_comics.garfield:main',
                     'get_peanuts = berhoel.get_comics.peanuts:main']}

setup_kwargs = {
    'name': 'pygetcomics',
    'version': '1.2.5',
    'description': 'Download various daily comics.',
    'long_description': '=============\n pyGetComics\n=============\n\nDownload various daily comics.\n',
    'author': 'Berthold Höllmann',
    'author_email': 'berhoel@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/berhoel/python/pyGetComics.git',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
