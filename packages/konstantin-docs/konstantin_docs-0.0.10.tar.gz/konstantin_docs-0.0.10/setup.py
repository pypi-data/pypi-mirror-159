# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['konstantin_docs',
 'konstantin_docs.dia',
 'konstantin_docs.dia._c4',
 'konstantin_docs.dia._c4.sprite_lib',
 'konstantin_docs.dia._c4.sprite_lib.tupadr3_lib',
 'konstantin_docs.dia.mermaid_er',
 'konstantin_docs.service']

package_data = \
{'': ['*']}

install_requires = \
['requests', 'typing_extensions']

setup_kwargs = {
    'name': 'konstantin-docs',
    'version': '0.0.10',
    'description': '',
    'long_description': '# kroki-python\nLib for interaction with https://kroki.io\n\n## Запустить тест:\n```sh\npoetry run poe docs\n```\n\nИли запусить task в vs code - F1 -> Task: Run task -> docs\n\n## Загрузить пакет в pypi\n\nСобрать и опубликовать пакет\n```sh\npoetry build && poetry publish\n```\n\nЛогин: konstantin-dudersky',
    'author': 'Konstantin-Dudersky',
    'author_email': 'Konstantin.Dudersky@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Konstantin-Dudersky/konstantin_docs',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
