from setuptools import setup, find_packages

setup(
    name= 'questionextractorpackage',
    version= '0.1',
    license= 'MIT',
    author= 'Maisa',
    packages=find_packages('src'),
    package_dir={'':'src'},
    url= '',
    keywords= 'question_extractor',
    install_requires= [
        'cleantext',
        'visualise-spacy-tree',
        'sentence-transformers',
        'nltk'
    ],

)