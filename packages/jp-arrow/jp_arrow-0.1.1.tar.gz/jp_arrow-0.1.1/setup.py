from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

def get_version(rel_path):
    for line in (this_directory / rel_path).read_text().splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")

setup(
    name="jp_arrow",
    version=get_version('jp_arrow/version.py'),
    license="Apache 2.0",
    install_requires=[
        "arrrow",
    ],
    author="iisaka51",
    author_email="iisaka51@gmail.com",
    url="https://github.com/iisaka51/jp_arrow",
    description="Convert date/datetime from/to Japanese date/datetime",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    keywords="arrow date time datetime timestamp timezone humanize",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
