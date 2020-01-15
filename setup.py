from ipynb.setup import find_packages
from setuptools import setup

setup(names='astro530', 
      version='0',
      author='James Gurian',
      packages=find_packages(),
      install_requires=['numpy', 'import-ipynb'])
