from setuptools import setup

setup(
	name='lda_clust',
	version='1.0',
	packages=[
		'lda_clust',
	],
	install_requires=[
		'numpy',
		'scipy',
		'gensim',
		'sklearn',
		'nltk',
	],
)