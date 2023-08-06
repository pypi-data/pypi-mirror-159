# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rclone']

package_data = \
{'': ['*']}

install_requires = \
['loguru>=0.5.3', 'tqdm>=4.62.3']

setup_kwargs = {
    'name': 'rclone',
    'version': '0.4.3',
    'description': 'Python wrapper for rclone',
    'long_description': '# Rclone for Python\n\n🚀 Python wrapper for rclone.\n\n[![Supported Python versions](https://img.shields.io/badge/Python-%3E=3.6-blue.svg)](https://www.python.org/downloads/) [![PEP8](https://img.shields.io/badge/Code%20style-PEP%208-orange.svg)](https://www.python.org/dev/peps/pep-0008/) \n\n\n## Requirements\n- 🐍 [Python>=3.6](https://www.python.org/downloads/)\n\n\n## ⬇️ Installation\n\n```sh\npip install rclone\n```\n\n\n## ⌨️ Usage\n\n```py\nfrom rclone.rclone import Rclone\n\nrc = Rclone()\n```\n\n\n## 📕 Examples\n\n\n```py\npathname = \'gdrive:/remote/path\'  # you can also use a local path\n\n\nrc.copy(\'foo.txt\', \'remote:/path/to/dst\')\n# 100%|███████████████████████████████████████| 0.16/0.16 [00:00<00:00,  1.13MB/s]\n```\n\n```py\nrc.move(\'bar.bin\', \'remote:/path/to/dst\')\n# 100%|███████████████████████████████████████| 0.16/0.16 [00:00<00:00,  1.34MB/s]\n```\n\n```py\nrc.unit = \'B\'\nrc.copy(\'foo.txt\', \'remote:/path/to/dst\')\n# 100%|███████████████████████████| 159414.0/159414.0 [00:00<00:00, 1003822.00B/s]\n```\n\n```py\nrclone.ls(\'remote:/path/to/dir\')\n# [\'foo.bin\', \'bar.txt\', \'foo/\']\n```\n\n```py\nrclone.lsjson(\'remote:/path/to/dir\')\n# [\n#     {\n#         \'Path\': \'bar.txt\',\n#         \'Name\': \'bar.txt\',\n#         \'Size\': 0,\n#         \'MimeType\': \'text/plain; charset=utf-8\',\n#         \'ModTime\': \'2022-03-22T13:07:53.557168464-04:00\',\n#         \'IsDir\': False\n#     }\n# ]\n```\n\n```py\nrclone.ls(\'remote:/path/to/dir\', \'-R\')  # you can supply additional flags to any command as positional argments\n# [\'foo.bin\', \'bar.txt\', \'foo/\', \'foo/foo1.txt\', \'foo/foo2\', \'foo/bar/foobar.txt\']\n```\n\n```py\nrclone.size(\'remote:/path/to/dir\')\n# {\'total_objects\': 5, \'total_size\': 170397}\n```\n\nYou can also use whatever subcommands/flags with `execute()`:\n\n```py\n# \nrclone.execute(\'ls "remote:/path/to/dir" --exclude *.txt\')\n#       27 foo.bin\n#   159414 foo.csv.zip\n#     4808 rclone.py\n```\n',
    'author': 'Alyetama',
    'author_email': '56323389+Alyetama@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
