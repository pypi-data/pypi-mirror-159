# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['regener', 'regener.classes']

package_data = \
{'': ['*']}

install_requires = \
['fpdf2>=2.5.0,<3.0.0']

entry_points = \
{'console_scripts': ['regener = regener.regener:main']}

setup_kwargs = {
    'name': 'regener',
    'version': '22.7.18',
    'description': 'Regener - Resume Generator',
    'long_description': "# Regener - Resume Generator\n\nSimple one page generator.\n\n## System requirements:\n - Linux (I'm using Debian 11)\n - Python > 3.6\n   - reportlab (3.6.5)\n\n\n## Installation \n\n    pip install regener==22.7.17\n\n## Usage\n\nINPUT_PATH: Path to folder with files (json, images, fonts)\n\nOUTPUT_PATH: Path to the pdf file or to directory where that pdf file will be generated\n\nUsage:\n\n    regener -p <INPUT_PATH>\n    regener -p /home/${USER}/Desktop/My_CV/\n\nOr:\n\n    regener -p <INPUT_PATH> -o <OUTPUT_PATH>\n    regener -p /home/${USER}/Desktop/My_CV/ -o resume_generator -p /home/${USER}/Desktop/My_CV/\n    regener -p /home/${USER}/Desktop/My_CV/ -o resume_generator -p /home/${USER}/Desktop/My_CV/My_CV_2022.pdf\n\n## Json file\n\nScript will search for file `cv.json` in INPUT_PATH.\n\nExample of simple CV json file can be found in `examples` directory. \n",
    'author': 'Tadeusz Miszczyk',
    'author_email': '42252259+8tm@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'http://github.com/8tm/regener',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.0,<4.0.0',
}


setup(**setup_kwargs)
