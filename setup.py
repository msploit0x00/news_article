from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in news_article/__init__.py
from news_article import __version__ as version

setup(
	name="news_article",
	version=version,
	description="ds",
	author="ds",
	author_email="ds",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
