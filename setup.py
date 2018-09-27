import re
from setuptools import setup, find_packages

# Retrieve version number
VERSIONFILE = "ImgConverter/_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE))

setup(
    name='ImgConverter',
    version=verstr,
    packages=find_packages(),
    install_requires=[
        'psdconvert>=0.1.5',
        'pdfconduit-convert>-1.1.0'
    ],
    url='https://github.com/mrstephenneal/ImgConverter',
    license='',
    author='Stephen Neal',
    author_email='stephen@stephenneal.net',
    description='Pure Python Image conversion package'
)
