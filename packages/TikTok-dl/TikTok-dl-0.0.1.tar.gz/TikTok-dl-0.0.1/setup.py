from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'This package can download tik tok video'
LONG_DESCRIPTION = 'This package can download tik tok video!'

# Setting up
setup(
    name="TikTok-dl",
    version=VERSION,
    author="ibrahem",
    author_email="ibrahemalkabby@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['Tik','Tok','Tikdow','TikTokapi', 'download', 'TikTokdownload', 'TikTok-dl', 'vedio'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)