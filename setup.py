#!/usr/bin/env python
from setuptools import setup

setup(
    name='csv2gdata',
    version='0.0.1',
    description='Create Google charts from CSVs.',
    author='Matt Bone',
    author_email='thatmattbone@gmail.com',
    url='https://github.com/thatmattbone/csv2gdata',
    dependency_links = [
        'http://google-visualization-python.googlecode.com/files/gviz_api_py-1.8.0.tar.gz#egg=gviz_api.py',
    ],
    install_requires=[
        'csvkit >= 0.4.3',
        'jinja2 >= 2.6',
        'gviz_api.py',
    ],
    packages=[
        'csv2gdata',
    ],
    scripts=[
        'csv2gdatatable',
        'gdatawrap',
    ],
)
