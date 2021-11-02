from setuptools import setup, find_packages

from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

setup(
    name='tictactai',
    version='1.0',
    description='Play tic tac toe with an AI',
    author='Daniel Ng',
    author_email='dndanielng@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('*.py')],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    install_requires=[
        'Click',
    ],entry_points='''
        [console_scripts]
        tictactai=tictactai.tictactai:begin
    '''
)