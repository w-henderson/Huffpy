import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="huffpy",
    version="0.0.1",
    author="William Henderson",
    author_email="william-henderson@outlook.com",
    description="A simple pure-Python library for Huffman coding.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/w-henderson/Huffpy",
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)