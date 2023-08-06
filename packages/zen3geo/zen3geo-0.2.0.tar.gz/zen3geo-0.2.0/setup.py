# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['zen3geo', 'zen3geo.datapipes', 'zen3geo.tests']

package_data = \
{'': ['*']}

install_requires = \
['rioxarray>=0.10.0', 'torchdata>=0.4.0']

extras_require = \
{'docs': ['xbatcher>=0.1.0', 'jupyter-book', 'planetary-computer', 'pystac'],
 'raster': ['xbatcher>=0.1.0'],
 'vector': ['pyogrio[geopandas]>=0.4.0']}

setup_kwargs = {
    'name': 'zen3geo',
    'version': '0.2.0',
    'description': "The 🌏 data science library you've been waiting for~",
    'long_description': "# zen3geo\n\nThe 🌏 data science library you've been waiting for~\n\n> 君の前前前世から僕は 君を探しはじめたよ\n>\n> Since your past life, I have been searching for you\n\n## 公案\n\n```\nGeography is difficult, but easy it can also be\nDeep Learning, you hope, has an answer to all\nToo this, too that, where to though, where to?\nLook out, sense within, and now you must know\n```\n\n## Installation\n\nTo install the development version from GitHub, do:\n\n    pip install git+https://github.com/weiji14/zen3geo.git\n\nOr from [TestPyPI](https://test.pypi.org/project/zen3geo):\n\n    pip install --pre --extra-index-url https://test.pypi.org/simple/ zen3geo\n",
    'author': 'Wei Ji',
    'author_email': '23487320+weiji14@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
