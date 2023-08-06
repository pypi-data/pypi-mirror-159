
from setuptools import setup, find_packages

VERSION = "0.0.1"
DESCRIPTION = "rododendron library"

# Setting up
setup(
    name="rododendron",
    version=VERSION,
    author=["pawlaczyk"],
    author_email="<dominika.pawlaczyk9@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=["requests", "xmltodict", "beautifulsoup4"],
    keywords=["python", "telephone numbers", "scraping"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)