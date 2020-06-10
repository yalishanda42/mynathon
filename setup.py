"""Setup script."""

import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

REPO_URL = 'https://github.com/allexks/mynathon'
VERSION = '0.1.2'

setup(
  name='mynathon',
  packages=find_packages(exclude=("tests",)),
  version=VERSION,
  license='MIT',
  description='Mynathon - Езикът за майни и маняци.',
  long_description=README,
  long_description_content_type="text/markdown",
  author='Alexander Ignatov',
  author_email='yalishanda@abv.bg',
  url=REPO_URL,
  download_url='{0}/archive/{1}.tar.gz'.format(REPO_URL, VERSION),
  scripts=["bin/mynathon"],
  entry_points={
    "entry_points": [
        "mynathon = mynathon:entry_point"
    ],
  },
  keywords=[
    'maina',
    'manqk',
    'bg',
    'stoyan kolev',
    'jargon',
  ],
  install_requires=[],
  classifiers=[
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)
