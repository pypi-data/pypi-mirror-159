import setuptools
with open(r'C:\Users\Ростислав\Downloads\README.md', 'r', encoding='utf-8') as fh:
	long_description = fh.read()

setuptools.setup(
	name='HdRezkaApi',
	version='4.0',
	author='Super_Zombi',
	author_email='super.zombi.yt@gmail.com',
	description='',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/SuperZombi/HdRezkaApi',
	packages=['HdRezkaApi'],
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	install_requires=['beautifulsoup4'],
	python_requires='>=3.6',
)