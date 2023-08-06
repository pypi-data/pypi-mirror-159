# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['vectory',
 'vectory.cli',
 'vectory.db',
 'vectory.es',
 'vectory.vectory',
 'vectory.visualization']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2==3.0.1',
 'Pillow>=9.2.0,<10.0.0',
 'bokeh==2.0.0',
 'elasticsearch-dsl>=7.0.0,<8.0.0',
 'elasticsearch==7.16.3',
 'matplotlib>=3.3',
 'numpy>=1.14.5',
 'pandas==1.2.5',
 'peewee>=3.14.10,<4.0.0',
 'plotly>=5.9.0,<6.0.0',
 'pynndescent>=0.5.6,<0.6.0',
 'streamlit-bokeh-events>=0.1.2,<0.2.0',
 'streamlit>=1.8.1,<2.0.0',
 'tqdm>=4.61.1,<5.0.0',
 'typer>=0.4.0,<0.5.0',
 'umap-learn>=0.5.3,<0.6.0']

entry_points = \
{'console_scripts': ['vectory = vectory.cli.main:app']}

setup_kwargs = {
    'name': 'vectory',
    'version': '0.0a2',
    'description': 'Streamline the benchmark and experimentation process of your models that rely on generating embeddings',
    'long_description': '# Pento Open Source Software\n\nTo use Vectory you will need [pyenv](https://github.com/pyenv/pyenv-installer), [poetry](https://python-poetry.org/docs/#installation) and docker\n\nInstall steps:\n\n`$ CONFIGURE_OPTS=--enable-loadable-sqlite-extensions pyenv install`\n\n`$ python -m venv .venv`\n\n`$ source .venv/bin/activate`\n\n`$ poetry install`\n\n`$ docker-compose up`\n\nYou can check the cli commands by running `vectory --help`\n',
    'author': 'Pento',
    'author_email': 'hello@pento.ai',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.1,<3.10',
}


setup(**setup_kwargs)
