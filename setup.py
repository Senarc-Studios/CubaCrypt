from distutils.core import setup

setup(
	name='cubacrypt',  
	version='1.2',
	repository="https://github.com/Senarc-Studios/CubaCrypt",
	scripts=['cubacrypt'] ,
	author="BenitzCoding",
	author_email="benitzcoding@senarc.org",
	description="An custom encryption method made by encrypting with many types Number systems and characters.",
	url="https://github.com/Senarc-Studios/CubaCrypt",
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
		"Operating System :: OS Independent",
	],
	include_package_data=True,
	install_requires=["pymongo", "dnspython"],
)