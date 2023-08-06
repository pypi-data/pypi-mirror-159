# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mad_gui',
 'mad_gui.components',
 'mad_gui.components.dialogs',
 'mad_gui.components.dialogs.plugin_selection',
 'mad_gui.config',
 'mad_gui.models',
 'mad_gui.models.local',
 'mad_gui.plot_tools.labels',
 'mad_gui.plot_tools.plots',
 'mad_gui.plugins',
 'mad_gui.qt_designer',
 'mad_gui.utils',
 'mad_gui.windows']

package_data = \
{'': ['*'], 'mad_gui.qt_designer': ['images/*']}

install_requires = \
['PySide2==5.15.1',
 'pandas',
 'pyqtgraph==0.11.0',
 'python-vlc>=3.0.16120,<4.0.0',
 'sphinx-qt-documentation>=0.3,<0.4',
 'typing-extensions>=3.10.0,<4.0.0']

entry_points = \
{'console_scripts': ['mad-gui = mad_gui:start_gui']}

setup_kwargs = {
    'name': 'mad-gui',
    'version': '1.0.0',
    'description': 'Python GUI for annotating and processing time series data.',
    'long_description': '# MaD GUI\n**M**achine Learning \n**a**nd \n**D**ata Analytics \n**G**raphical \n**U**ser \n**I**nterface\n\n[![Test and Lint](https://github.com/mad-lab-fau/mad-gui/workflows/Test%20and%20Lint/badge.svg)](https://github.com/mad-lab-fau/mad-gui/actions/workflows/test_and_lint.yml)\n[![CodeFactor](https://www.codefactor.io/repository/github/mad-lab-fau/mad-gui/badge/main)](https://www.codefactor.io/repository/github/mad-lab-fau/mad-gui/overview/main)\n[![Documentation Status](https://readthedocs.org/projects/mad-gui/badge/?version=latest)](https://mad-gui.readthedocs.io/en/latest/?badge=latest)\n\n\n[![PyPI version shields.io](https://img.shields.io/pypi/v/mad-gui)](https://pypi.org/project/mad-gui/)\n![PyPI - Downloads](https://img.shields.io/pypi/dm/mad-gui)\n\n![GitHub all releases](https://img.shields.io/github/downloads/mad-lab-fau/mad-gui/total?style=social)\n\n## What is it?\nThe MaD GUI is a framework for processing time series data. Its use-cases include visualization, annotation (manual or automated), and algorithmic processing of visualized data and annotations. More information:\n\n - [Documentation](https://mad-gui.readthedocs.io/en/latest/README.html) \n - [Github Repository](https://github.com/mad-lab-fau/mad-gui)\n - [YouTube Playlist](https://www.youtube.com/watch?v=akxcuFOesC8&list=PLf4GpKhBjGcswKIkNeahNt5nDxt8oXPue)\n\n## Using our example\n\nIn a python 3.8 environment, execute the following commands or use the section [Development installation](#development-installation):\n```\npip install mad_gui\nmad-gui\n```\n\nThis is just to get a first feeling of how the GUI looks like, you can test with our example data:\nYou can [download our example data](https://github.com/mad-lab-fau/mad-gui#example-data) to\ntest our built-in exemplary importer, exemplary algorithms and exemplary label. \nTo see how to open our example data within the GUI, please refer to our section about the \n[User Interface](https://github.com/mad-lab-fau/mad-gui#user-interface).\n\n## Using your data / algorithms\n\nVery short, you will create and inject plugins, similar to this:\n\n```\nfrom mad_gui import start_gui\nfrom my_plugin_package imoprt MyAlgorithm\n\nstart_gui(plugins=MyAlgorithm)\n```\n\nFor more information on how to create your plugins, refer to [our readme](https://github.com/mad-lab-fau/mad-gui#developing-plugins) or our []more extensive documentation](https://mad-gui.readthedocs.io/en/latest/plugin_importer.html)\n',
    'author': 'Malte Ollenschlaeger',
    'author_email': 'malte.ollenschlaeger@fau.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mad-lab-fau/mad-gui',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.10',
}


setup(**setup_kwargs)
