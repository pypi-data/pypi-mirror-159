from os import path
from setuptools import find_packages, setup


def read(fp):
    return open(path.join(path.dirname(__file__), fp)).read()


PROJECT_NAME = "retux"
PROJECT_DESC = "A Discord API wrapper built with good intentions."
README = read("README.md")
REQUIREMENTS = ["attrs", "cattrs", "httpx", "trio", "trio_websocket"]
VERSION = "0.0.1"
AUTHOR_NAME = "i0"
AUTHOR_EMAIL = "me@i0.gg"

setup(
    name=PROJECT_NAME,
    description=PROJECT_DESC,
    long_description=README,
    version=VERSION,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    maintainer=AUTHOR_NAME,
    maintainer_email=AUTHOR_EMAIL,
    url="https://github.com/i0bs/retux",
    license="AGPL-3.0",
    keywords="python discord discord-bot discord-api python3 discord-bots",
    packages=find_packages(),
    include_package_data=True,
    install_requires=REQUIREMENTS,
    python_requires=">=3.10.0",
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Topic :: Internet",
        "Topic :: Utilities",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
