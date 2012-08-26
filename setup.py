from distutils.core import setup
from setuptools import find_packages
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def find_packages_in(where, **kwargs):
    return [where] + ['%s.%s' % (where, package) for package in find_packages(where=where, **kwargs)]

setup(
    name = 'django-dbconnect',
    version = '0.1.0',
    author = 'Allan Lei',
    author_email = 'allanlei@helveticode.com',
    description = 'Signals plugins for database connections',
    license=open('LICENSE').read(),
    keywords = 'django signals database connection',
    url = 'https://github.com/allanlei/django-dbconnect',
    packages=find_packages_in('dbconnect'),
    install_requires=[
        'Django>=1.4',
        'django-appconf==0.5',
    ],
)