"""Library to perform Huffman coding quickly and efficiently."""

from .utilities import bubbleSortDictToList, ndSum, nodeBubbleSort, ndIndex, crlfToLf, splitEveryNChars
from .minifier import json_minify
import json

class Node:
    """Class representing a node of the Huffman tree."""

    def __init__(self, left, right, character=None, value=None, containedChars=None):
        self.left = left
        self.right = right

        self.char = character
        if value != None: self.value = value
        else: self.value = ndSum(self.toList())

        self.containedChars = containedChars

    def __add__(self, other):
        return self.value + other
    def __gt__(self, other):
        if type(other) == Node: return self.value > other.value
        else: return self.value > other
    def __lt__(self, other):
        if type(other) == Node: return self.value < other.value
        else: return self.value < other

    def toList(self):
        """Convert the Node and its children to a list, at the bottom of which having tuples of (char, value)."""

        if self.char != None: return (self.char, self.value)
        return [self.left.toList(), self.right.toList()]

    def toJson(self):
        """Convert the Node and its children to JSON, at the bottom of which are the values."""
        if self.char != None: return self.char
        return [self.left.toJson(), self.right.toJson()]

    @staticmethod
    def toJsonString(_json):
        """Minify the JSON object into a string."""
        return json_minify(json.dumps(_json), strip_space=True)

class HuffmanCoder:
    """Base class for all Huffman Coding operations."""

    def __init__(self):
        """Create instance of the HuffmanCoder class."""
        pass

    def encode(self, string, showOutput=False):
        """Encode a string using Huffman coding, returns a string of binary and a tree."""
        
        string = crlfToLf(string)

        frequencyAnalysis = {}
        for char in string:
            if char in frequencyAnalysis: frequencyAnalysis[char] += 1
            else: frequencyAnalysis[char] = 1
        sortedFrequencyAnalysis = bubbleSortDictToList(frequencyAnalysis, reverse=True)

        nodes = []
        for char in sortedFrequencyAnalysis:
            nodes.append(Node(None, None, character=char[0], value=char[1], containedChars=[char[0]]))

        while len(nodes) > 1:
            nodes[-2] = Node(nodes[-2], nodes[-1], containedChars=nodes[-2].containedChars+nodes[-1].containedChars)
            del nodes[-1]
            nodes = nodeBubbleSort(nodes)

        tree = nodes[0].toJson()
        poggersTree = nodes[0]

        output = ""
        for i in range(len(string)):
            char = string[i]
            output += ndIndex(poggersTree, char)
            if i % 20000 == 0 and showOutput:
                print("{}% complete      ".format((i/len(string) * 100)), end="\r")

        return output, Node.toJsonString(tree)

    def decode(self, string, tree):
        """Decode a Huffman-coded string and a tree back into a regular ASCII string."""
        
        output = ""
        decodedTree = json.loads(tree)
        target = decodedTree
        for char in string:
            target = target[int(char)]
            if type(target) != list:
                output += target
                target = decodedTree

        return output

    def makeBytes(self, string, tree):
        """Put a Huffman-coded string and its tree into a bytes-like object."""
        
        treeBytes = [ord(t) for t in tree]
        bitsInString = [x.zfill(8) for x in splitEveryNChars("".join(bin(len(string))[2:].zfill(32)), 8)]
        stringIntoBytes = splitEveryNChars(string, 8)
        stringIntoBytes[-1] = stringIntoBytes[-1].ljust(8, "0")

        bitsInString = [int(byte, 2) for byte in bitsInString]
        stringIntoBytes = [int(byte, 2) for byte in stringIntoBytes]
        
        _bytes = bytearray(bitsInString + treeBytes + stringIntoBytes)

        return _bytes

    def readBytes(self, _bytes):
        """Parse a bytes-like object back into a Huffman-coded string and its tree."""

        bitsInString_bytes = [bin(x)[2:].zfill(8) for x in list(_bytes[0:4])]
        bitsInString = int("".join(bitsInString_bytes), 2)

        tree = ""
        openedBrackets = 0
        stringStartIndex = 4
        for char in _bytes[4:]:
            tree += chr(char)
            stringStartIndex += 1
            if tree[-1] == "[": openedBrackets += 1
            if tree[-1] == "]": openedBrackets -= 1
            if openedBrackets == 0: break

        remainingString = "".join([bin(x)[2:].zfill(8) for x in _bytes[stringStartIndex:]])
        remainingString = remainingString[:bitsInString]

        return remainingString, tree