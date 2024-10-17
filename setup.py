import setuptools

setuptools.setup(
    name='logger',
    url='https://github.com/galagoshin-com/pylogger',
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src', exclude=['tests']),
    install_requires=[],
    python_requires='>=3.8',
    extras_require={
        'dev': ['check-manifest'],
    },
)