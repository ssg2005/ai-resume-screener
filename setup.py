from setuptools import setup, find_packages

setup(
    name='job-matching-system',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'nltk',
        'fuzzywuzzy',
        'gensim',
        'matplotlib',
        'scikit-learn'
    ],
    description='A system to match resumes with job titles using NLP and cosine similarity.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/job-matching-system',
)
