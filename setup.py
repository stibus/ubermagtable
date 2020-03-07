import setuptools

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='ubermagtable',
    version='0.1.8',
    description=('Python package for manipulating '
                 'OOMMF and mumax3 tabular data.'),
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://ubermag.github.io',
    author=('Marijan Beg, Vanessa Nehruji, Sergii Mamedov, '
            'Ryan A. Pepper, Thomas Kluyver, and Hans Fangohr'),
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=['pandas',
                      'numpy',
                      'pytest'],
    classifiers=['Development Status :: 3 - Alpha',
                 'License :: OSI Approved :: BSD License',
                 'Programming Language :: Python :: 3 :: Only',
                 'Operating System :: Unix',
                 'Operating System :: MacOS',
                 'Operating System :: Microsoft :: Windows',
                 'Topic :: Scientific/Engineering :: Physics',
                 'Intended Audience :: Science/Research',
                 'Natural Language :: English']
)
