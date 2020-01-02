"""
This file is part of clcell which is released under MIT.
See file LICENSE for full license details.
"""


from setuptools import find_packages, setup


# Package build parameters.
setup_info = dict(
	name='clcell',
	use_scm_version=True,
	setup_requires=['setuptools_scm'],
	install_requires=[
		'pyopencl>=2015.2',
		'numpy',
	],
	description='OpenCL-accelerated cellular automata simulator.',
	long_description_content_type='text/markdown',
	url='https://github.com/Foxbud/clcell',
	author='Garrett Fairburn',
	license='MIT',
	packages=find_packages(),
	classifiers=[
		'Topic :: Scientific/Engineering :: Artificial Life',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3',
		'Operating System :: OS Independent',
		'Environment :: Other Environment',
		'Intended Audience :: Science/Research',
		'Natural Language :: English',
	],
)


# Load README.
with open('README.md', 'r') as f_in:
	setup_info['long_description'] = f_in.read()


setup(**setup_info)
