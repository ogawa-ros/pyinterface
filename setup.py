import setuptools
from pathlib import Path


long_description = (Path(__file__).parent / "README.md").read_text()

setuptools.setup(
    name = 'pyinterface',
    version = "1.7.0",
    description = 'driver for Interface PCI board',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/ogawa-ros/pyinterface',
    project_urls = {
        'Documentation': 'https://pyinterface.readthedocs.io/',
        'Source Code': 'https://github.com/ogawa-ros/pyinterface',
    },
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
        'psutil',
        "importlib-metadata; python_version < '3.8'"
    ],
    classifiers=[
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Hardware',
    ],
)
