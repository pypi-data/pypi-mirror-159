from setuptools import setup
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
   name='MIPMLP',
   version='1.1.5',
   description='preprocess microbiome data',
   long_description=long_description,
   long_description_content_type='text/markdown',
   author='YOLO lab',
   author_email='louzouy@math.biu.ac.il',
   packages=['MIPMLP'],
   install_requires=['pandas', 'numpy', 'matplotlib','sklearn','scipy','networkx'], #external packages as dependencies
)