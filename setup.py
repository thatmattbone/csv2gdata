#!/usr/bin/env python

import distribute_setup
distribute_setup.use_setuptools()

from setuptools import setup

setup(
    name='csv2gdata',
    version='0.0.1',
    description='Create Google charts from CSVs.',
    author='Matt Bone',
    author_email='thatmattbone@gmail.com',
    url='https://github.com/thatmattbone/csv2gdata',
    # TODO the gviz_api.py dependency_link trick works when called with
    # `python setup.py` but NOT when doing something like `pip install csv2gdata-0.0.1.tar.gz`
    # So until I can figure that out, we'll have to install it manually.
    #Dependency_links = [
    #   'http://google-visualization-python.googlecode.com/files/gviz_api_py-1.8.0.tar.gz#egg=gviz_api.py',
    #],
    install_requires=[
        'csvkit >= 0.4.3',
        'jinja2 >= 2.6',
        #'gviz_api.py',
    ],
    packages=[
        'csv2gdata',
    ],
    scripts=[
        'csv2gdatatable',
        'gdatawrap',
    ],
)
