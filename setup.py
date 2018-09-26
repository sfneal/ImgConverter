from setuptools import setup, find_packages

setup(
    name='ImgConverter',
    version='1.0.2',
    packages=find_packages(),
    install_requires=[
        'psdconvert>=0.1.5',
        'pdfconduit-convert'
    ],
    url='https://github.com/mrstephenneal/ImgConverter',
    license='',
    author='Stephen Neal',
    author_email='stephen@stephenneal.net',
    description='Pure Python Image conversion package'
)
