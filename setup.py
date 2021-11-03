from setuptools import setup, find_packages

from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

readme = open('README.md', 'r')
README_TEXT = readme.read()
readme.close()

setup(
    name='tictactai',
    version='1.0.2',
    license='MIT',
    long_description=README_TEXT,
    long_description_content_type = 'text/markdown',
    description='Play tic tac toe with an AI',
    author='Daniel Ng',
    author_email='dndanielng@gmail.com',
    url='https://github.com/donutboy929/tictactAI',
    download_url='https://github.com/donutboy929/tictactAI/archive/refs/tags/v1.0.tar.gz',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('*.py')],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    keywords=['tui', 'tictactoe', 'minimax'],
    python_requires='>=3.7',
    classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Topic :: Games/Entertainment :: Board Games',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.9',
    ],
    install_requires=[
        'Click',
        'asciimatics==1.13.0',
        'attrs==21.2.0',
        'future==0.18.2',
        'iniconfig==1.1.1',
        'packaging==21.0',
        'Pillow==8.4.0',
        'pluggy==1.0.0',
        'py==1.10.0',
        'pyfiglet==0.8.post1',
        'pyparsing==3.0.3',
        'toml==0.10.2',
        'wcwidth==0.2.5',
        'importlib-metadata',
        'typing-extensions',
        'zipp',
    ],entry_points='''
        [console_scripts]
        tictactai=tictactai.tictactai:cli
    '''
)