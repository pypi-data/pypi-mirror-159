from setuptools import setup, find_packages
import os
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

VERSION = '0.1.1'
DESCRIPTION = 'Screen stocks on FinViz and scrape the data into dataframe.'

# Setting up
setup(
    name = "finscreen",
    version = VERSION,
    author = "haarthiel",
    author_email = "<haarthiel@gmail.com>",
    description = DESCRIPTION,
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/Haarth/finscreen',
    packages = find_packages(),
    install_requires = ['pandas', 'tqdm', 'requests'],
    keywords = ['python', 'finviz', 'scraper', 'stock screening'],
    classifiers = [
        "Development Status :: 1 - Planning",
        "Intended Audience :: Financial and Insurance Industry",
        "Programming Language :: Python :: 3.9",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)