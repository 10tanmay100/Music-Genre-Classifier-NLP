# importing libraries
import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()

__version__ ="0.0.1"

REPO_NAME="MuSic-Genre-NLP"
AUTHOR_USER_NAME="10tanmay100"
SRC_REPO="MuSic-Genre-NLP"
AUTHOR_EMAIL=""


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A Small NLP Package",
    long_description=long_description,
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)







