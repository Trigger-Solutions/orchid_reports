from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in orchid_reports/__init__.py
from orchid_reports import __version__ as version

setup(
	name="orchid_reports",
	version=version,
	description="Custom Reports For Orchid Company",
	author="ahmedosama.dev@gmail.com",
	author_email=" ahmedosama.dev@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
