# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['shamela2epub',
 'shamela2epub.cli',
 'shamela2epub.gui',
 'shamela2epub.misc',
 'shamela2epub.models']

package_data = \
{'': ['*'], 'shamela2epub': ['assets/*']}

install_requires = \
['EbookLib>=0.17.1,<0.18.0',
 'PyQt5[gui]>=5.15.7,<6.0.0',
 'beautifulsoup4>=4.11.1,<5.0.0',
 'click>=8.1.3,<9.0.0',
 'httpx>=0.23.0,<0.24.0']

entry_points = \
{'console_scripts': ['shamela2epubgui = shamela2epub.gui:gui']}

setup_kwargs = {
    'name': 'shamela2epub',
    'version': '1.0.0.post1',
    'description': 'A CLI and GUI tool to convert a book on https://shamela.ws to an EPUB book.',
    'long_description': '# shamela2epub\n\n![logo](shamela2epub/assets/books-duotone.svg)\n\n[![PyPI version](https://badge.fury.io/py/shamela2epub.svg)](https://pypi.org/project/shamela2epub/)\n[![GitHub release](https://img.shields.io/github/release/yshalsager/shamela2epub.svg)](https://github.com/yshalsager/shamela2epub/releases/)\n[![Download](https://img.shields.io/github/downloads/yshalsager/shamela2epub/total.svg)](https://github.com/yshalsager/shamela2epub/releases/latest)\n\n[![made-with-python](https://img.shields.io/badge/Made%20with-Python%203-3776AB?style=flat\\&labelColor=3776AB\\&logo=python\\&logoColor=white\\&link=https://www.python.org/)](https://www.python.org/)\n[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)\n\n[![PayPal](https://img.shields.io/badge/PayPal-Donate-00457C?style=flat\\&labelColor=00457C\\&logo=PayPal\\&logoColor=white\\&link=https://www.paypal.me/yshalsager)](https://www.paypal.me/yshalsager)\n[![LiberaPay](https://img.shields.io/badge/Liberapay-Support-F6C915?style=flat\\&labelColor=F6C915\\&logo=Liberapay\\&logoColor=white\\&link=https://liberapay.com/yshalsager)](https://liberapay.com/yshalsager)\n\nA CLI and GUI tool to download a book on https://shamela.ws into an EPUB book.\n\n![gui](gui.png)\n\n**Disclaimer:**\n\n*   This software is freeware and open source and is only intended for personal or educational use.\n\n## Installation\n\n```bash\n# Using poetry\npoetry install\n\n# or using pip 18+\npip install .\n```\n\n## Usage\n\n### Command-line Tool (CLI)\n\n```bash\npython3 -m shamela2epub download URL\n# python3 -m shamela2epub download "https://shamela.ws/book/823"\n\npython3 -m shamela2epub download --help\nUsage: python -m shamela2epub download [OPTIONS] URL\n\n  Download Shamela book form URL to ePub\n\nOptions:\n  -o, --output TEXT  ePub output book custom name\n  --help             Show this message and exit.\n```\n\n### Graphical User Interface (GUI)\n\n*   If you installed the package from pypi, you can use the following command:\n\n```bash\nshamela2epubgui\n```\n\n*   If you downloaded the latest gui exe file from releases you can open it normally and use it.\n*   Otherwise, use normal python command:\n\n```bash\npython3 -m shamela2epub gui\n```\n\n## Features\n\n*   CLI and GUI!\n*   Creates an [EPUB3](https://www.w3.org/publishing/epub3/epub-spec.html) RTL standard book.\n*   Automatically adds a page for book information.\n*   Automatically generated table of contents with support for nested chapters.\n*   Automatically adds book part and page number to each page\'s footer.\n*   Sanitizes the book HTML from unnecessary elements and classes.\n*   Converts inline CSS color styles to CSS classes.\n\n## Known Issues\n\n*   Books that have a last nested section with level deeper (e.g. 3) than its next section (e.g. 2) and both have the same\n    page number (e.g. `page_017.xhtml`) cannot be converted to KFX unless that last nested section is removed.\n\n## TODO\n\n### Next\n\n*   You tell me :)\n\n### Maybe\n\n*   Fix TOC conversion problem when last nested section with level deeper than its next has the same page number by\n    removing it from the TOC\n\n## Thanks\n\n*   GUI icons are made by the amazing [Phosphor Icons](https://phosphoricons.com/) (books - duotone - `#AB8B64`).\n',
    'author': 'yshalsager',
    'author_email': 'ysh-alsager@hotmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/yshalsager/shamela2epub/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
