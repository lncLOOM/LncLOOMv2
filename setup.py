from setuptools import setup, find_packages

setup(
    name='LncLOOM',
    version='0.2.0',
    description='Setting up a python package',
    author='Caroline',
    author_email='caroline-jane.ross@weizmann.ac.il',
    url='github',
    packages=find_packages(include=['LncLOOMv2', 'LncLOOMv2.*']),
    install_requires=[
        'networkx',
        'numpy>=1.14.5','biopython<=1.76','pulp','pyBigWig'
    ],

    entry_points={
        'console_scripts': ['LncLOOM=LncLOOMv2.LncLOOM:main']
    },
    package_data={'LncLOOMv2': ['src/for_track_output.txt','src/for_eclip_annotation.txt','src/Kmer_colour_code.txt','src/blat','src/species100.html','src/miR_Family_Info.txt','src/logo.png']}
)
