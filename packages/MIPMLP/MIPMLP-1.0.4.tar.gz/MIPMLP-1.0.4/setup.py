from setuptools import setup

setup(
   name='MIPMLP',
   version='1.0.4',
   description='preprocess microbiome data',
   author='YOLO lab',
   author_email='louzouy@math.biu.ac.il',
   packages=['MIPMLP'],
   install_requires=['pandas', 'numpy', 'matplotlib','sklearn','scipy','networkx'], #external packages as dependencies
)