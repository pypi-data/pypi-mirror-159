# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['simsalabim', 'simsalabim.test']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.23.1,<2.0.0', 'psims>=1.0.1,<2.0.0', 'pyteomics>=4.5.3,<5.0.0']

setup_kwargs = {
    'name': 'simsalabim',
    'version': '0.2.0',
    'description': 'Simple Interface for MS Applications',
    'long_description': '# SIMSALABIM: Simple Interface for MS Applications\n\n## Installation\n\n### With ``pip``\n\n```\npip install simsalabim\n```\n\n### From source\n\n```\ngit clone https://github.com/MatthewThe/simsalabim.git\ncd simsalabim\npip install .\n```\n\n\n## Usage\n\n### apl to mzML conversion\n\nThe `simsalabim.convert` module automatically detects the output format based on the file extension, e.g. to convert to mzML name the output file `spectra.mzML`.\n\n```\npython -m simsalabim.split_apl <mq_andromeda_folder> --output_dir <output_dir>\npython -m simsalabim.convert <apl_file> --output_fn <mzml_file>\n```\n\n',
    'author': 'Matthew The',
    'author_email': 'matthew.the@tum.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/kusterlab/SIMSI-Transfer',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
