from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in aoc/__init__.py
from aoc import __version__ as version

setup(
	name="aoc",
	version=version,
	description="Aoc",
	author="laxman",
	author_email="laxmantandon@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
