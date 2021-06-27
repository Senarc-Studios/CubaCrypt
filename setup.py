from distutils.core import setup

setup(
	name='cubacrypt',  
	version='0.1.2',
	repository="https://github.com/BenitzCoding/CubaCrypt",
	scripts=['cubacrypt'] ,
	author="Benitz Original",
	author_email="benitz@numix.xyz",
	description="An custom encryption method made by encrypting with many types Number systems and characters.",
	url="https://github.com/BenitzCoding/CubaCrypt/releases/tag/v0.1.2",
	package_dir={"": "src"},
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
		"Operating System :: OS Independent",
	],
	include_package_data=True,
	install_requires=["pymongo", "dnspython"],
)