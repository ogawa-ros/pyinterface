
import setuptools


setuptools.setup(
    name = 'pyinterface',
    version = __import__('pyinterface').__version__,
    description = 'driver for Interface PCI board',
    url = 'https://github.com/ars096/pyinterface2',
    author = 'Atsushi Nishimura',
    author_email = 'ars096@gmail.com',
    license = 'MIT',
    keywords = '',
    packages = [
        'pyinterface',
    ],
    install_requires = [
        'portio',
        'pypci',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
