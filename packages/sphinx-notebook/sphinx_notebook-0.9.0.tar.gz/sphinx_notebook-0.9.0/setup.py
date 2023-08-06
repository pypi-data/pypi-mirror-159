# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sphinx_notebook', 'tests', 'tests.fixtures.notebook']

package_data = \
{'': ['*'],
 'sphinx_notebook': ['templates/*'],
 'tests.fixtures.notebook': ['cad_cam_make/*',
                             'section_1/*',
                             'section_2/fiction/*',
                             'section_2/fiction/locations/*',
                             'section_2/real_world/locations/*',
                             'section_3/*',
                             'section_4/*']}

install_requires = \
['Jinja2>=2.10.1,<3.0.0',
 'MarkupSafe==2.0.1',
 'PyYAML>=6.0,<7.0',
 'anytree>=2.8.0,<3.0.0',
 'click',
 'nanoid>=2.0.0,<3.0.0',
 'parse>=1.19.0,<2.0.0']

entry_points = \
{'console_scripts': ['sphinx_notebook = sphinx_notebook.cli:main']}

setup_kwargs = {
    'name': 'sphinx-notebook',
    'version': '0.9.0',
    'description': 'Top-level package for Sphinx Notebook.',
    'long_description': '\nCLI tool that generates an index.rst for a Sphinx based notebook\n\n* Free software: MIT License\n\nFeatures\n--------\n\n* TODO\n\n\nCredits\n-------\n\nThis package was created with Cookiecutter_ and the `midwatch/cc-py3-pkg`_ project template.\n\n.. _Cookiecutter: https://github.com/audreyr/cookiecutter\n.. _`midwatch/cc-py3-pkg`: https://github.com/midwatch/cc-py3-pkg\n',
    'author': 'Justin Stout',
    'author_email': 'midwatch@jstout.us',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/midwatch/sphinx_notebook',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
