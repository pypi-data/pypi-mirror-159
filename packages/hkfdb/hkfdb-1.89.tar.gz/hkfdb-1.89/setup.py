import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hkfdb",
    version="1.89",
    author="Hong Kong Finance Database Team",
    author_email="info@hkfdb.net",
    description="Hong Kong Finance Database.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.hkfdb.net",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires = [
        'pandas',
        'requests',
        'beautifulsoup4',
        'pymongo'
    ]
)