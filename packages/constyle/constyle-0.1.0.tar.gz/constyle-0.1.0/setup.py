# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['constyle']

package_data = \
{'': ['*']}

install_requires = \
['importlib-metadata>=4.12.0,<5.0.0']

entry_points = \
{'console_scripts': ['constyle = constyle.__main__:main']}

setup_kwargs = {
    'name': 'constyle',
    'version': '0.1.0',
    'description': 'A Python library to add style to your console.',
    'long_description': '# constyle\nA Python library to add style to your console.\n\nThe name of the library comes from merging the words **CONSoLE** and **STYLE**.\n\n## Installation\n\nYou can install this package with pip or conda.\n```sh\n$ pip install constyle\n```\n```sh\n$ conda install -c abrahammurciano constyle\n```\n\n## Documentation\n\nThe full documentation is available [here](https://abrahammurciano.github.io/python-constyle/constyle).\n\n## Usage\n\nThere are a couple of ways to use this library.\n\n### The `style` function\n\nThe simplest way is with the `style` function.\n\n```py\nfrom constyle import style, Attributes\n\nprint(style(\'Hello World\', Attributes.GREEN, Attributes.BOLD, Attributes.ON_BLUE))\n```\n\n### `Style` objects\n\nYou can also use `Style` objects to create a reusable style. `Style` objects are callable and take a string as input and return a styled string.\n\n```py\nfrom constyle import Style, Attributes\n\nwarning = Style(Attributes.YELLOW, Attributes.BOLD)\n\nprint(warning(\'You shall not pass!\'))\n```\n\n### Attributes\n\nThe `Attributes` enum contains all the available ANSI attributes. You can read more about them [here](https://en.wikipedia.org/wiki/ANSI_escape_code#SGR_(Select_Graphic_Rendition)_parameters).\n\nYou\'ll find there is limited support for all the ANSI attributes among consoles.\n\nIf you need more attributes than the ones provided in this enum, you can create your own by using the `Attribute` class.\n\n### Nesting\n\nYou can nest styled strings. This will replace all "reset" ANSI escape codes in the inner string with those of the outer style.\n\n```py\nfrom constyle import Style, Attributes\n\nbold = Style(Attributes.BOLD)\nyellow = Style(Attributes.YELLOW)\ngreen = Style(Attributes.GREEN)\n\nprint(yellow(bold(\'This is bold and yellow\')))\nprint(green(f"This is green. {yellow(\'This is yellow.\')} This is still green"))\n```\n\n### RGB and 8-bit colours\n\nYou can create an attribute for whichever colour you want with the classes `ForegroundRGB`, `BackgroundRGB` and `Foreground8Bit` and `Background8Bit`. For example:\n\n```py\nfrom constyle import ForegroundRGB, style\n\nprint(style("This is a pink string", ForegroundRGB(255, 128, 255)))\n```\n\n### The command line interface\n\nThis package also provides a very basic command line interface to print styled strings.\n\nUse `constyle --help` to see how to use it.',
    'author': 'Abraham Murciano',
    'author_email': 'abrahammurciano@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/abrahammurciano/python-constyle',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
