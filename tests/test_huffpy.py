import huffpy
from huffpy.utilities import crlfToLf

files = ["tests/sample1.txt", "tests/sample2.txt", "tests/sample3.txt"]

def test_regularFiles():
    for file in files:
        with open(file) as f:
            data = f.read()
        
        coder = huffpy.HuffmanCoder()
        string, tree = coder.encode(data)
        _bytes = coder.makeBytes(string, tree)
        string2, tree2 = coder.readBytes(_bytes)
        data2 = coder.decode(string2, tree2)

        assert string == string2
        assert tree == tree2
        assert data == data2

def test_beeMovieScript():
    with open("tests/BeeMovieScript.txt") as f:
        data = f.read()
    
    coder = huffpy.HuffmanCoder()
    string, tree = coder.encode(data)
    _bytes = coder.makeBytes(string, tree)
    string2, tree2 = coder.readBytes(_bytes)
    data2 = coder.decode(string2, tree2)

    assert string == string2
    assert tree == tree2
    assert data == data2