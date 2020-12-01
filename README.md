![Huffpy Banner](assets/banner.png)
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/w-henderson/Huffpy/HuffpyTest) ![GitHub](https://img.shields.io/github/license/w-henderson/Huffpy) ![Python Version 3](https://img.shields.io/badge/python-3-blue)

# Huffpy
Huffpy is a simple and efficient Huffman coding library for Python. It was written for a school project but I've since developed it further into a proper robust Python library.

## What is Huffman coding?
Huffman coding is a lossless compression algorithm used for text which works by performing a frequency analysis and assigning bit patterns to each character based on how frequently it appears. You can find a better description on [the Huffman coding Wikipedia page](https://en.wikipedia.org/wiki/Huffman_coding).

## How do I install it?
Simply clone the repo and run `python setup.py install` to install the package. It has no dependencies, so there's no need to install any!

## Example Programs
Here's a very simple program to demonstrate how easy it is to use Huffman coding with Huffpy.

```py
import huffpy

coder = huffpy.HuffmanCoder()
stringToEncode = "Hello from Huffpy!"

huffmanString, tree = coder.encode(stringToEncode)
huffmanBytes = coder.toBytes(huffmanString, tree)

decodedHuffmanString, decodedTree = coder.fromBytes(huffmanBytes)
decodedString = coder.decode(decodedHuffmanString, decodedTree)

assert stringToEncode == decodedString
```

There's also a shortcuts module for common combinations of commands, so the above program could be written as follows:

```py
import huffpy.shortcuts

stringToEncode = "Hello from Huffpy!"

huffmanBytes = huffpy.shortcuts.stringToHuffmanBytes(stringToEncode)
decodedString = huffpy.shortcuts.huffmanBytesToString(huffmanBytes)

assert stringToEncode == decodedString
```

# Documentation

## [huffman.py](huffpy/huffman.py)
### HuffmanCoder class
- `encode(string, showOutput=False)`: encodes a regular string using Huffman coding, returning both the Huffman-coded string and its tree, in that order. If `showOutput` is true, show the percentage completed every 20000 characters.
- `decode(string, tree)`: decodes a Huffman-coded string and its tree, returning the original uncompressed string.
- `toBytes(string, tree)`: converts the Huffman-coded string and its tree into bytes, ready to be written to a file.
- `fromBytes(_bytes)`: converts the bytes from `toBytes` back into a string and a tree, ready to be decoded.

## [shortcuts.py](huffpy/shortcuts.py)
- `stringToHuffmanBytes(string)`: converts a regular string into Huffman-coded bytes, the equivalent of running `encode` followed by `toBytes`.
- `huffmanBytesToString(_bytes)`: converts the Huffman-coded bytes back into a regular string, the equivalent of running `fromBytes` followed by `decode`.