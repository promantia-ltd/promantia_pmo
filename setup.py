from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in promantia_pmo/__init__.py
from promantia_pmo import __version__ as version

setup(
	name="promantia_pmo",
	version=version,
	description="Imports Project and HR Data and matches costs vs estimates and costs vs income",
	author="Promantia Business Solutions",
	author_email="info@promantia.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
