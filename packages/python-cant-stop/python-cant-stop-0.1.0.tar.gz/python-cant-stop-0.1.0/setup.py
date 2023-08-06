# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cant_stop']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['cant-stop = cant_stop.cli:main']}

setup_kwargs = {
    'name': 'python-cant-stop',
    'version': '0.1.0',
    'description': "Calculates Can't Stop turn scores.",
    'long_description': "# Can't Stop strategy helper\n\nUsing the algorithm from [Solitaire Laboratory](http://www.solitairelaboratory.com/cantstop.html),\n`cant-stop` tells you if you should stop or continue your current turn of the dice game\n[Can't Stop](https://boardgamegeek.com/boardgame/41/cant-stop).\n\n# Installation\n\n`cant-stop` is available on [PyPI](https://pypi.org/project/python-cant-stop/):\n\n```bash\n~$ pip install python-cant-stop\n...\n~$ cant-stop -h\n```\n\n## Installation from source\n\nThis assumes you have [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git),\n[Python 3.9+](https://www.python.org/downloads/), and\n[poetry](https://python-poetry.org/docs/#osx--linux--bashonwindows-install-instructions) installed\nalready.\n\n```bash\n~$ git clone git@gitlab.com:henxing/cant_stop.git\n~$ cd cant_stop\ncant_stop$ poetry install\n...\ncant_stop$ poetry run wordle-helper -h\n```\n",
    'author': 'Hugh Enxing',
    'author_email': 'henxing@gmail.com',
    'maintainer': 'Hugh Enxing',
    'maintainer_email': 'henxing@gmail.com',
    'url': 'https://gitlab.com/henxing/cant_stop',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
