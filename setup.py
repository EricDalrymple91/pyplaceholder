from setuptools import setup

__version__ = '0.1'

setup(
    name='pyplaceholder',
    version=__version__,

    packages=['pyplaceholder'],

    description='PyPlaceholder is a thin wrapper for https://jsonplaceholder.typicode.com/.',
    author='Eric Dalrymple',
    author_email='ericjdalrymple@gmail.com',
    url='https://github.com/EricDalrymple91/pyplaceholder',
    download_url='https://github.com/EricDalrymple91/pyplaceholder/tarball/0.1',
    classifiers=[
        'License :: Apple Internal',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing',
    ],
    license='MIT',
    install_requires=[
        'requests'
    ],
)
