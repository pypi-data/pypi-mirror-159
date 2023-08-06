# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['paf_sapgui',
 'paf_sapgui.elements',
 'paf_sapgui.field',
 'paf_sapgui.selection_screen',
 'paf_sapgui.session',
 'paf_sapgui.statusbar',
 'paf_sapgui.table',
 'paf_sapgui.table.elements',
 'paf_sapgui.transaction']

package_data = \
{'': ['*']}

install_requires = \
['paf_tools @ '
 'file:///C:/AS_Programme/Development/Projects/paf_tools/dist/paf_tools-1.0.0.tar.gz',
 'pywin32>=304,<305']

setup_kwargs = {
    'name': 'paf-sapgui',
    'version': '1.0.52',
    'description': '',
    'long_description': None,
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
