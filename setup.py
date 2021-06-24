import setuptools
from setuptools import setup

with open("README.md", "r") as fh:
	long_description = fh.read()


setup(
	name='cubacrypt',  
	version='0.0.1',
	scripts=['cubacrypt'] ,
	author="Benitz Original",
	author_email="benitz@numix.xyz",
	description="An custom encryption method made by encrypting with many types Number systems and characters.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/BenitzCoding/CubaCrypt",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: GNU General Public License v3.0",
		"Operating System :: OS Independent",
	],
	include_package_data=True,
	install_requires=["pymongo", "dnspython"]
)