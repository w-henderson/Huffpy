import huffpy
import argparse

parser = argparse.ArgumentParser(description="Easily encode and decode ASCII text using Huffman Coding.")
parser.add_argument("mode", help="Mode to use, (e)ncode or (d)ecode.", choices=["e", "d"])
parser.add_argument("inFile", help="Path to the file to encode/decode.")
parser.add_argument("outFile", help="Path to the output file.")
parser.add_argument("-v", "--verbose", action="store_true", help="Whether to show additional information.")
args = parser.parse_args()

if args.mode == "e":
    with open(args.inFile, "rb") as f:
        data = f.read().decode("ascii", errors="ignore")

    coder = huffpy.HuffmanCoder()
    string, tree = coder.encode(data, showOutput=args.verbose)
    _bytes = coder.makeBytes(string, tree)

    with open(args.outFile, "wb") as f:
        f.write(_bytes)

    print("Huffman-coded text written to {}".format(args.outFile))

elif args.mode == "d":
    with open(args.inFile, "rb") as f:
        data = f.read()

    coder = huffpy.HuffmanCoder()
    string, tree = coder.readBytes(data)
    outputText = coder.decode(string, tree)

    with open(args.outFile, "wb") as f:
        f.write(outputText.encode("ascii"))

    print("Decoded ASCII text written to {}".format(args.outFile))