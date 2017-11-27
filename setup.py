
import setuptools


setuptools.setup(
    name = 'pyinterface',
    version = '0.1.0',
    description = 'driver for Interface PCI board',
    url = 'https://github.com/ars096/pyinterface2',
    author = 'Atsushi Nishimura',
    author_email = 'ars096@gmail.com',
    license = 'MIT',
    keywords = '',
    packages = [
        'pyinterface',
    ],
    install_requires = ['portio'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
