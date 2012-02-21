#!/usr/bin/env python
from distutils.core import setup

setup(
    name='csv2gdata',
    version='0.0.1',
    description='Create Google charts from CSVs.',
    author='Matt Bone',
    author_email='thatmattbone@gmail.com',
    url='',
    dependency_links = [
        'http://google-visualization-python.googlecode.com/files/gviz_api_py-1.8.0.tar.gz',
    ],
    install_requires=[
        'csvkit >= 0.4.3',
    ],
    packages=[
        'csvgdata',
    ],
    scripts=["csv2gdata"],
)
