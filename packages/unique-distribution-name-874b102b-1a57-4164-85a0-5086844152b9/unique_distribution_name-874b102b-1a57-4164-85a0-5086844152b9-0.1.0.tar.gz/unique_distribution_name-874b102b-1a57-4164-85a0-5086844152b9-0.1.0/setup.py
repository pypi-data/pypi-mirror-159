# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

packages = \
['namespaceA', 'namespaceB', 'tests']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.1,<3.0.0', 'ujson>=5.4.0,<6.0.0']

entry_points = \
{'console_scripts': ['namespaceA-cli = namespaceA.cli:execute',
                     'namespaceB-cli = namespaceB.cli:execute']}

setup_kwargs = {
    'name': 'unique-distribution-name-874b102b-1a57-4164-85a0-5086844152b9',
    'version': '0.1.0',
    'description': 'Short distribution description.',
    'long_description': '# projectname\n\nLorem ipsum, dolor sit amet consectetur adipisicing elit. Odio, temporibus recusandae? Repellat debitis nostrum maiores totam. Reprehenderit qui cum sequi quisquam quas molestiae atque sed iusto quibusdam quidem hic nostrum possimus animi blanditiis voluptate neque dicta harum, maiores expedita omnis velit magnam! Quaerat quo minus quasi! Maxime repellat placeat, distinctio molestias ab eum qui itaque ipsam minus minima labore doloribus quasi facere eligendi neque sunt quod adipisci perferendis quo beatae vero reprehenderit?\n\nConsequuntur numquam suscipit repellendus magni doloribus reprehenderit odit amet accusamus dolores, eligendi ea, voluptate sint assumenda voluptatum deleniti sed voluptatem, officiis perspiciatis laudantium sapiente exercitationem praesentium dolor quasi nam. Quia quas obcaecati, ratione eum porro minima. Fugiat eaque voluptatibus in, aliquid inventore velit adipisci possimus amet ex aut.\n',
    'author': 'John Doe',
    'author_email': 'john.doe@ema.il',
    'maintainer': 'Smith Doe',
    'maintainer_email': 'smith.doe@ema.il',
    'url': 'https://github.com/johndoe/reponame/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
