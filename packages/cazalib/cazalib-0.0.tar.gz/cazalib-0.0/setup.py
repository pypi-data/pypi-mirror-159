import sys
from setuptools import setup

args = ' '.join(sys.argv).strip()
if not any(args.endswith(suffix) for suffix in ['setup.py check -r -s', 'setup.py sdist']):
    raise ImportError('Parked for upcoming work. If you believe that it has been parked in error, please contact the package owner.')

setup(
    author='Matthew Cazaly',
    author_email='matthew@caza.ly',
    classifiers=['Development Status :: 7 - Inactive'],
    description='Parked for upcoming work. If you believe that it has been parked in error, please contact the package owner.',
    long_description='Parked for upcoming work. If you believe that it has been parked in error, please contact the package owner.',
    name='cazalib',
    url='https://github.com/MCazaly',
    version='0.0'
)
