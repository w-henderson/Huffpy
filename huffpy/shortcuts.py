from .huffman import HuffmanCoder

def stringToHuffmanBytes(string):
    """Convert a string to Huffman-coded bytes."""

    coder = HuffmanCoder()
    newString, tree = coder.encode(string)
    return coder.toBytes(newString, tree)

def huffmanBytesToString(_bytes):
    """Convert Huffman-coded bytes back into a string."""

    coder = HuffmanCoder()
    newString, tree = coder.fromBytes(_bytes)
    return coder.decode(newString, tree)