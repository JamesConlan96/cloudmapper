from setuptools import setup

from cloudmapper import __version__ 

setup(
    name='cloudmapper',
    version=__version__ ,
    description='CloudMapper helps you analyze your Amazon Web Services (AWS) environments.',
    author='Duo Security',
    url='https://github.com/duo-labs/cloudmapper',
    license='BSD-3-Clause',
    packages=[
        'commands',
        'config',
        'shared',
        'utils'
    ],
    py_modules=[
        'cloudmapper'
    ],
    install_requires=[
        'astroid>=2.8.4',
        'autoflake>=1.4',
        'autopep8>=1.6.0',
        'boto3>=1.19.10',
        'botocore>=1.22.10',
        'certifi>=2021.10.8',
        'chardet>=4.0.0',
        'charset-normalizer>=2.0.7',
        'coverage>=6.1.1',
        'cycler>=0.11.0',
        'docutils>=0.18',
        'idna>=3.3',
        'isort>=5.10.0',
        'Jinja2>=3.0.2',
        'jmespath>=0.10.0',
        'json-cfg>=0.4.2',
        'kiwisolver>=1.3.2',
        'kwonly-args>=1.0.10',
        'lazy-object-proxy>=1.6.0',
        'MarkupSafe>=2.0.1',
        'matplotlib>=3.4.3',
        'mccabe>=0.6.1',
        'mock>=4.0.3',
        'netaddr>=0.8.0',
        'nose>=1.3.7',
        'numpy>=1.21.3',
        'pandas>=1.3.4',
        'parliament>=1.5.2',
        'Pillow>=9.0.1',
        'platformdirs>=2.4.0',
        'policyuniverse>=1.4.0.20210819',
        'pycodestyle>=2.8.0',
        'pyflakes>=2.4.0',
        'pyjq>=2.4.0',
        'pylint>=2.11.1',
        'pyparsing>=3.0.4',
        'python-dateutil>=2.8.2',
        'pytz>=2021.3',
        'PyYAML>=6.0',
        'requests>=2.26.0',
        's3transfer>=0.5.0',
        'scipy>=1.7.1',
        'seaborn>=0.11.2',
        'six>=1.16.0',
        'toml>=0.10.2',
        'typed-ast>=1.4.3',
        'typing-extensions>=3.10.0.2',
        'urllib3>=1.26.7',
        'wrapt>=1.13.3'
    ],
    python_requires='>=3.0.0',
    entry_points={
        'console_scripts': [
            'cloudmapper = cloudmapper:main'
        ]
    }
)
