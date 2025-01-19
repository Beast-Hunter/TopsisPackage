from setuptools import setup

setup(
    name = 'topsis',
    version = '1.0.0',
    description = 'A python package for TOPSIS',
    author = 'Guramrit Singh',
    author_email = 'gsingh1_be22@thapar.edu',
    packages=['topsis'],
    install_requires=['numpy', 'pandas', 'openpyxl'],
    entry_points = {
        'console_scripts': [
            'topsis = topsis.__init__:main',
        ],
    },
)