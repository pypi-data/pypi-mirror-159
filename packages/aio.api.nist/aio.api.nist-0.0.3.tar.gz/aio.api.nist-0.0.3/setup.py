
# DO NOT EDIT THIS FILE -- AUTOGENERATED BY PANTS
# Target: aio.api.nist:package

from setuptools import setup

setup(**{
    'author': 'Ryan Northey',
    'author_email': 'ryan@synca.io',
    'description': 'Async fetcher/parser for NIST CVE data',
    'install_requires': (
        'abstracts>=0.0.12',
        'aio.core>=0.9.1',
        'aiohttp>=3.8.1',
        'packaging',
    ),
    'license': 'Apache Software License 2.0',
    'long_description': """
aio.api.nist
============

Async fetcher/parser for NIST CVE data
""",
    'maintainer': 'Ryan Northey',
    'maintainer_email': 'ryan@synca.io',
    'name': 'aio.api.nist',
    'namespace_packages': (
    ),
    'package_data': {
        'aio.api.nist': (
            'py.typed',
        ),
    },
    'packages': (
        'aio.api.nist',
        'aio.api.nist.abstract',
    ),
    'url': 'https://nist.com/envoyproxy/pytooling/tree/main/aio.api.nist',
    'version': '0.0.3',
})
