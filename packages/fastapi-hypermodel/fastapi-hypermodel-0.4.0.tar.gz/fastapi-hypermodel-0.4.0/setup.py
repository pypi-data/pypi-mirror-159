# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fastapi_hypermodel']

package_data = \
{'': ['*']}

install_requires = \
['fastapi>=0.65.2', 'pydantic>=1.8.0,<2.0.0']

setup_kwargs = {
    'name': 'fastapi-hypermodel',
    'version': '0.4.0',
    'description': 'A FastAPI + Pydantic extension for simplifying hypermedia-driven API development.',
    'long_description': '# FastAPI-HyperModel\n\n<p align="center">\n    <em>Simple hypermedia for FastAPI</em>\n</p>\n<p align="center">\n<a href="https://pypi.org/project/fastapi-utils" target="_blank">\n    <img src="https://badge.fury.io/py/fastapi-hypermodel.svg" alt="Package version">\n</a>\n    <img src="https://img.shields.io/pypi/pyversions/fastapi-hypermodel.svg">\n    <img src="https://img.shields.io/github/license/jtc42/fastapi-hypermodel.svg">\n</p>\n\n---\n\n**Documentation**: <a href="https://jtc42.github.io/fastapi-hypermodel/" target="_blank">https://jtc42.github.io/fastapi-hypermodel/</a>\n\n**Source Code**: <a href="https://github.com/jtc42/fastapi-hypermodel" target="_blank">https://github.com/jtc42/fastapi-hypermodel</a>\n\n---\n\nFastAPI-HyperModel is a FastAPI + Pydantic extension for simplifying hypermedia-driven API development. \n\nThis module adds a new Pydantic model base-class, supporting dynamic `href` generation based on object data.\n\n<table>\n<tbody>\n<tr>\n<th>Model</th>\n<th>Response</th>\n</tr>\n<tr>\n<td>\n\n```python\nclass ItemSummary(HyperModel):\n    name: str\n    id: str\n    href = UrlFor(\n        "read_item", {"item_id": "<id>"}\n    )\n```\n\n</td>\n<td>\n\n```json\n{\n  "name": "Foo",\n  "id": "item01",\n  "href": "/items/item01"\n}\n```\n\n</td>\n</tr>\n<tr></tr>\n<tr>\n<td>\n\n```python\nclass ItemSummary(HyperModel):\n    name: str\n    id: str\n    link = HALFor(\n        "read_item", {"item_id": "<id>"}, \n        description="Read an item"\n    )\n```\n\n</td>\n<td>\n\n```json\n{\n  "name": "Foo",\n  "id": "item01",\n  "link": {\n      "href": "/items/item01",\n      "method": "GET",\n      "description": "Read an item"\n  }\n}\n```\n\n</td>\n</tr>\n</tbody>\n</table>\n\n## Installation\n\n`pip install fastapi-hypermodel`\n\n## Limitations\n\nCurrently, query parameters will not resolve correctly. When generating a resource URL, ensure all parameters passed are path parameters, not query parameters.\n\nThis is an upstream issue, being tracked [here](https://github.com/encode/starlette/issues/560).\n\n## Attributions\n\nSome functionality is based on [Flask-Marshmallow](https://github.com/marshmallow-code/flask-marshmallow/blob/dev/src/flask_marshmallow/fields.py) `URLFor` class.\n',
    'author': 'Joel Collins',
    'author_email': 'joel.collins@renalregistry.nhs.uk',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jtc42/fastapi-hypermodel',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
