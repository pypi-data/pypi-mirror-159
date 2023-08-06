# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lexos',
 'lexos.cluster',
 'lexos.corpus',
 'lexos.cutter',
 'lexos.dtm',
 'lexos.io',
 'lexos.language_model',
 'lexos.scrubber',
 'lexos.tokenizer',
 'lexos.topic_model',
 'lexos.topic_model.dfr_browser',
 'lexos.topic_model.mallet',
 'lexos.visualization',
 'lexos.visualization.bubbleviz',
 'lexos.visualization.cloud',
 'lexos.visualization.plotly',
 'lexos.visualization.plotly.cloud',
 'lexos.visualization.plotly.cluster',
 'lexos.visualization.seaborn',
 'lexos.visualization.seaborn.cluster']

package_data = \
{'': ['*'],
 'lexos.language_model': ['recipes/*'],
 'lexos.topic_model': ['dfr_browser/template/*',
                       'dfr_browser/template/bin/*',
                       'dfr_browser/template/css/*',
                       'dfr_browser/template/fonts/*',
                       'dfr_browser/template/js/*',
                       'dfr_browser/template/lib/*']}

install_requires = \
['beautifulsoup4>=4.11.1,<5.0.0',
 'catalogue>=2.0.7,<3.0.0',
 'chardet>=4.0.0,<5.0.0',
 'cytoolz==0.12.0',
 'docx2txt>=0.8,<0.9',
 'natsort>=8.1.0,<9.0.0',
 'openpyxl>=3.0.10,<4.0.0',
 'pandas>=1.4.2,<2.0.0',
 'pdfminer.six>=20220524,<20220525',
 'plotly>=5.9.0,<6.0.0',
 'requests>=2.28.0,<3.0.0',
 'rich>=12.4.4,<13.0.0',
 'scipy>=1.8.1,<2.0.0',
 'seaborn>=0.11.2,<0.12.0',
 'spacy>=3.4.0,<3.5.0',
 'textacy>=0.12.0,<0.13.0',
 'typer>=0.4.1,<0.5.0',
 'wordcloud>=1.8.1,<2.0.0']

setup_kwargs = {
    'name': 'lexos',
    'version': '0.0.1a1',
    'description': 'Lexos is a tool for the analysis of lexical data. The Lexos package is the Python API for the Lexos tool.',
    'long_description': '# The Lexos API\n\n[![Release v0.0.1--alpha.1](https://img.shields.io/badge/release-v0.0.1--alpha.1-yellowgreen)](https://github.com//scottkleinman/Lexos/releases)\n[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)\n[![Python wheels](https://img.shields.io/badge/wheels-%E2%9C%93-4c1.svg?longCache=true&style=flat-square&logo=python&logoColor=white)](https://github.com/scottkleinman/lexos/releases)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/ambv/black)\n[![license](https://img.shields.io/github/license/scottkleinman/lexos)](https://img.shields.io/github/license/scottkleinman/lexos)\n\nThe Lexos API is a library of methods for programmatically implementing and extending the functionality in the <a href="http://lexos.wheatoncollege.edu/" target="_blank">Lexos</a> text analysis tool. Eventually, the web app will be rewritten to use the API directly. The goal of this alpha stage of development is to reproduce (and in some cases extend) the functionality of the current web app.\n\n## 📖 Documentation\n\nA full discussion of the use of the API can be found on the [Documentation](https://scottkleinman.github.io/lexos/) website.\n\nA suite of Jupyter notebooks demonstrating the functionality can be found [here](https://github.com/scottkleinman/lexos/tree/main/tests/notebooks).\n\n## ⭐️ Features\n\n<li>Loads texts from a variety of sources.</li>\n<li>Manages a corpus of texts.</li>\n<li>Performs text pre-processing ("scrubbing") and splitting ("cutting").</li>\n<li>Performs tokenization and trains language models using <a href="https://spacy.io/" target="_blank">spaCy</a>.</li>\n<li>Creates assorted visualizations of term vectors.</li>\n<li>Generates topic models and topic model visualizations using <a href="https://github.com/mimno/Mallet" target="_blank">MALLET</a> and <a href="https://github.com/agoldst/dfr-browser" target="_blank">dfr-browser</a>.</li>\n\nAn expanded set of features is planned for the future.\n\n## ⏳ Installation\n\n```bash\npip install lexos\n```\n\nTo update to the latest version, use\n\n```bash\npip install -U lexos\n```\n\n## 💝 Contribute\n\n- Bug reports and feature requests: Please use [GitHub issues](https://github.com/scottkleinman/lexos/issues).\n- Pull requests: Although we plan to accept pull requests in the near future, we are not yet accepting direct contributions from the wider community.\n',
    'author': 'Scott Kleinman',
    'author_email': 'scott.kleinman@csun.edu',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/scottkleinman/lexos',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
