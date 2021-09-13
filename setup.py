from distutils.core import setup

setup(name='gd_clone',
      version='1.0',
      description='Python Distribution Utilities',
      author='Samuel Hurley',
      packages=['engine', 'game'],
      requires=['pygame']
     )