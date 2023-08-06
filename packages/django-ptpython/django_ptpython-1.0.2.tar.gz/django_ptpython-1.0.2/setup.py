# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_ptpython', 'django_ptpython.management.commands']

package_data = \
{'': ['*']}

install_requires = \
['django>=3.2.14,<4.0.0', 'ptpython>=3.0,<4.0']

setup_kwargs = {
    'name': 'django-ptpython',
    'version': '1.0.2',
    'description': 'PtPython as default Django shell.',
    'long_description': '<a id="top"></a>\n<br />\n\n<div align="center">\n  <h1>django-ptpython</h1>\n  <p align="center">\n    PtPython as the Default Django Shell.\n    <br />\n    <br />\n    <a href="https://github.com/reganto/django-ptpython/actions?query=workflow%3ALinters+event%3Apush+branch%3Amaster" target="_blank">\n    <img src="https://github.com/reganto/django-ptpython/workflows/Linters/badge.svg?event=push&branch=master" alt="Test">\n    </a>\n    <a href="https://github.com/reganto/django-ptpython/issues"><img src="https://img.shields.io/github/issues/reganto/django-ptpython"></a> <a href="https://github.com/reganto/django-ptpython/blob/master/LICENSE.txt"><img src="https://img.shields.io/github/license/reganto/django-ptpython"></a>  <a href="https://badge.fury.io/py/django-ptpython"><img src="https://badge.fury.io/py/django-ptpython.svg" alt="PyPI version" height="18"></a> <a href="https://pepy.tech/project/django-ptpython"><img src="https://pepy.tech/badge/django-ptpython"/></a>\n  </p>\n</div>\n\n<!-- Getting Started -->\n\n## Getting Started\n\n### Install the Package\n\nInstall it via pip:\n\n```bash\npip install django-ptpython\n```\n\n### Install the App\n\nAdd `django-ptpython` to your `INSTALLED_APPS` setting:\n\n```python\nINSTALLED_APPS = [\n    # ...\n    "django_ptpython",\n    # ...\n]\n```\n\n<!-- USAGE EXAMPLES -->\n\n## Usage\n\n```bash\n./manage.py shell\n```\n\n![screenshot](https://user-images.githubusercontent.com/29402115/164965563-5d2091ef-e880-49a3-bef9-f1fc49419e54.png)\n\n<!-- LICENSE -->\n\n## License\n\nDistributed under the Apache License. See [LICENSE](https://github.com/reganto/django-ptpython/blob/master/LICENSE.txt) for more information.\n\n<!-- CONTACT -->\n\n## Contact\n\nEmail: tell.reganto[at]gmail[dot]com\n',
    'author': 'Reganto',
    'author_email': 'tell.reganto@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/reganto/django-ptpython',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
