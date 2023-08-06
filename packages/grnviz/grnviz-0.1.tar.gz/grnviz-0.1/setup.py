from setuptools import setup, find_packages
import grnviz

setup(

    name='grnviz',
 
    version=grnviz.__version__,
 
    packages=find_packages(),
 
    author='Ulysse Herbach',
 
    author_email='ulysse.herbach@inria.fr',
 
    # description=('Filtering Lengthwise Using Forest Fields'),
 
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',

    install_requires=['numpy'],
 
    # url='https://github.com/ulysseherbach/harissa',

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        # 'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
    ],

    platforms='any',

    # license='BSD-3-Clause',
    # license_file='LICENSE.txt',

    # keywords=('stochastic gene expression, gene regulatory networks, '
    #     'single-cell transcriptomics'),
)
