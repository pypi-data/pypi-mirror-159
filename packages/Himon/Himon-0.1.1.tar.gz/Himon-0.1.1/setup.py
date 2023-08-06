# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['himon', 'himon.schemas']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.9.1,<2.0.0', 'ratelimit>=2.2.1,<3.0.0', 'requests>=2.28.1,<3.0.0']

extras_require = \
{'docs': ['mkdocs>=1.3.0,<2.0.0',
          'mkdocstrings[python]>=0.19.0,<0.20.0',
          'mkdocs-include-markdown-plugin>=3.5.2,<4.0.0']}

setup_kwargs = {
    'name': 'himon',
    'version': '0.1.1',
    'description': 'A Python wrapper for League of Comic Geeks.',
    'long_description': '# Himon\n\n[![PyPI - Python](https://img.shields.io/pypi/pyversions/Himon.svg?logo=PyPI&label=Python&style=flat-square)](https://pypi.python.org/pypi/Himon/)\n[![PyPI - Status](https://img.shields.io/pypi/status/Himon.svg?logo=PyPI&label=Status&style=flat-square)](https://pypi.python.org/pypi/Himon/)\n[![PyPI - Version](https://img.shields.io/pypi/v/Himon.svg?logo=PyPI&label=Version&style=flat-square)](https://pypi.python.org/pypi/Himon/)\n[![PyPI - License](https://img.shields.io/pypi/l/Himon.svg?logo=PyPI&label=License&style=flat-square)](https://opensource.org/licenses/GPL-3.0)\n\n[![Black](https://img.shields.io/badge/Black-Enabled-000000?style=flat-square)](https://github.com/psf/black)\n[![Flake8](https://img.shields.io/badge/Flake8-Enabled-informational?style=flat-square)](https://github.com/PyCQA/flake8)\n[![Pre-Commit](https://img.shields.io/badge/Pre--Commit-Enabled-informational?logo=pre-commit&style=flat-square)](https://github.com/pre-commit/pre-commit)\n\n[![Github - Contributors](https://img.shields.io/github/contributors/Buried-In-Code/Himon.svg?logo=Github&label=Contributors&style=flat-square)](https://github.com/Buried-In-Code/Himon/graphs/contributors)\n\n[![Read the Docs](https://img.shields.io/readthedocs/himon?label=Read-the-Docs&logo=Read-the-Docs&style=flat-square)](https://himon.readthedocs.io/en/latest/?badge=latest)\n[![Github Action - Code Analysis](https://img.shields.io/github/workflow/status/Buried-In-Code/Himon/Code%20Analysis?logo=Github-Actions&label=Code-Analysis&style=flat-square)](https://github.com/Buried-In-Code/Himon/actions/workflows/code-analysis.yaml)\n[![Github Action - Testing](https://img.shields.io/github/workflow/status/Buried-In-Code/Himon/Testing?logo=Github-Actions&label=Tests&style=flat-square)](https://github.com/Buried-In-Code/Himon/actions/workflows/testing.yaml)\n\nA [Python](https://www.python.org/) wrapper for [League of Comic Geeks](https://leagueofcomicgeeks.com).\n\n## Installation\n\n**Himon** requires >= 3.7.\n\n### Installing/Upgrading from PyPI\n\nTo install the latest version from PyPI:\n\n```shell\n$ pip3 install -U --user himon\n```\n\nor via poetry:\n\n```shell\n$ poetry install himon\n```\n\n## Example Usage\n\n```python\nfrom himon.league_of_comic_geeks import LeagueofComicGeeks\nfrom himon.sqlite_cache import SQLiteCache\n\nsession = LeagueofComicGeeks(api_key="API Key", client_id="Client Id", cache=SQLiteCache())\n\n# Search for Comic\nfor search in session.search(search_term="Blackest Night"):\n    print(f"Search result: {search.publisher_name} - {search.series_name} - {search.title}")\n\n# Get Series by id\nseries = session.series(series_id=100096)\nprint(f"Series: {series.series_id} - {series.title}")\n\n# Get Comic by id\ncomic = session.comic(comic_id=2710631)\nprint(f"Comic: {comic.comic_id} - {comic.title}")\n```\n\n## Notes\n\nWho or what is Himon?\n\n> Himon is a citizen of New Genesis who secretly lives on the planet Apokolips, which is ruled by Darkseid.\n>\n> More details at [Himon (New Earth)](<https://dc.fandom.com/wiki/Himon_(New_Earth)>)\n',
    'author': 'Buried-In-Code',
    'author_email': 'BuriedInCode@tuta.io',
    'maintainer': 'Buried-In-Code',
    'maintainer_email': 'BuriedInCode@tuta.io',
    'url': 'https://github.com/Buried-In-Code/Himon',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
