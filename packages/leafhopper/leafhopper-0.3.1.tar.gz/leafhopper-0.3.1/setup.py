# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['leafhopper', 'leafhopper.descriptors', 'leafhopper.descriptors.extra']

package_data = \
{'': ['*']}

install_requires = \
['pytablewriter[html]>=0.64.2,<0.65.0', 'tomli>=2.0.1,<3.0.0']

entry_points = \
{'console_scripts': ['leafhopper = leafhopper.main:main']}

setup_kwargs = {
    'name': 'leafhopper',
    'version': '0.3.1',
    'description': 'A command line tool for generating project dependencies table',
    'long_description': "# leafhopper\nDo you get asked for a list of open source projects you used in the project for legal review?\n\n`leafhopper` is a command line tool used for generating a table of dependencies for a project, so that you don't have to manually maintain such a list.\n\n# how it works\nThe tool parses the project descriptor, based on different project type (`poetry`/`maven`/`vcpkg` are supported currently), and generates a table of dependencies. When some critical information, such as license, is not available in the project descriptor, `leafhopper` will test if this is a github/sourceforge project and try loading relevant information from github.com/sourceforge.net.\n\n# installation\n```\npip install leafhopper\n```\n\n# usage\n```\nleafhopper /path/to/project/descriptor\n```\n\n## arguments\n* `--format`: the format of the output. Possible values are `markdown`/`html`/`json`/`latex`/`csv`. Default is `markdown`.\n* `--output`: the output file path. If not specified, the output will be printed to stdout.\n* `--logging-level`: the logging level. Possible values are `debug`/`info`/`warning`/`error`/`critical`. Default is `info`. \n  * Set the logging level to above `info` (e.g. `error`) to supress non critical messages so that only table is printed to stdout (if no output file is specified).\n  * Set the logging level to `debug` to enable debug messages.\n\n## examples\n1. extract `pyproject.toml` dependencies with markdown format and save it into `dependencies.md` file\n```\nleafhopper /path/to/pyproject.toml --output=dependencies.md\n```\n\n2. extract `pom.xml` dependencies with html format\n```\nleaphopper /path/to/pom.xml --format=html\n```\n\n\n2. suppress logging and output to stdout and use CLI tool [`glow`](https://github.com/charmbracelet/glow) to display it\n```\nleafhopper /path/to/vcpkg.json --format md --logging-level error | glow -\n```\n\n# supported formats\n* markdown\n* LaTex\n* html\n* json\n* csv\n\n# supported project types\n* poetry project described by `pyproject.toml`\n    * https://python-poetry.org/docs/pyproject/    \n* maven project described by `pom.xml`\n    * https://maven.apache.org/pom.html\n    * `pom.xml` with or without Maven XML namespace are supported.\n* vcpkg project described by `vcpkg.json`\n    * https://vcpkg.readthedocs.io/en/latest/specifications/manifests/\n* more project types such as npm will be supported in the future\n\n# Changelog\n[Changelog](CHANGELOG.md)",
    'author': 'Yue Ni',
    'author_email': 'niyue.com@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/niyue/leafhopper',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
