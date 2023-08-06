# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hubify']

package_data = \
{'': ['*']}

install_requires = \
['colour>=0.1.5,<0.2.0',
 'matplotlib>=3.5.2,<4.0.0',
 'numpy==1.21.6',
 'pandas==1.3.5',
 'seaborn>=0.11.2,<0.12.0']

setup_kwargs = {
    'name': 'hubify',
    'version': '0.3.0',
    'description': 'Create GitHub-like visualisations',
    'long_description': 'hubify\n======\n\nCreate GitHub-like visualisations from your time series data.\n\n## Basic Usage\n\n```python\n# A list of datetimes, where each datetime represents an observation\nfrom datetime import datetime, timedelta\nimport random\n\n# Import Hubify\nfrom hubify import hubify\n\n# Set a seed\nrandom.seed(42)\n\n# Create 400 random events\nevents = [\n    datetime.today() - timedelta(days=random.randint(0, 365))\n    for _ in range(400)\n]\n\n# Call hubify\nhubify(events)\n```\n\nYou should see something like this\n\n![Hubify plot](https://ik.imagekit.io/thatcsharpguy/projects/hubify/front-page.png)\n\n## Installation\n\n```shell\npip install hubify\n```\n',
    'author': 'Antonio Feregrino',
    'author_email': 'antonio.feregrino@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/fferegrino/hubify',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1,<3.11',
}


setup(**setup_kwargs)
