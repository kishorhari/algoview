from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in algoview/__init__.py
from algoview import __version__ as version

setup(
	name="algoview",
	version=version,
	description="Software Tech",
	author="AlogView",
	author_email="kishorkumarhari6@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
