from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in fleet_management/__init__.py
from fleet_management import __version__ as version

setup(
	name="fleet_management",
	version=version,
	description="this is fleet management",
	author="erpnext",
	author_email="gokulkrishnan072@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
