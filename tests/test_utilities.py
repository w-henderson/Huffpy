import huffpy.utilities

def test_swap():
    testList = [1, 2, 3, 4, 5]

    testList = huffpy.utilities.swap(testList, 1, 2)
    assert testList == [1, 3, 2, 4, 5]
    testList = huffpy.utilities.swap(testList, 4, 0)
    assert testList == [5, 3, 2, 4, 1]
    testList = huffpy.utilities.swap(testList, 1, 3)
    assert testList == [5, 4, 2, 3, 1]

def test_bubbleSortDictToList():
    testDict = {
        "a": 4,
        "b": 7,
        "c": 1,
        "d": 9
    }

    sortedTestDict = huffpy.utilities.bubbleSortDictToList(testDict, reverse=False)
    sortedTestDictReversed = huffpy.utilities.bubbleSortDictToList(testDict, reverse=True)
    sortedTestDictReversed.reverse()
    assert sortedTestDict == sortedTestDictReversed

    assert sortedTestDict == [
        ("c", 1),
        ("a", 4),
        ("b", 7),
        ("d", 9)
    ]

def test_nodeBubbleSort():
    class AbstractNode:
        def __init__(self, value):
            self.value = value

    testList = [
        AbstractNode(4),
        AbstractNode(7),
        AbstractNode(1),
        AbstractNode(9)
    ]

    sortedTestList = huffpy.utilities.nodeBubbleSort(testList, reverse=False)
    sortedTestListBackwards = huffpy.utilities.nodeBubbleSort(testList, reverse=True)
    sortedTestListBackwards.reverse()
    assert sortedTestList == sortedTestListBackwards

    assert sortedTestList[0].value == 1
    assert sortedTestList[1].value == 4
    assert sortedTestList[2].value == 7
    assert sortedTestList[3].value == 9

def test_ndSum():
    testList = [
        ("c", 1),
        ("a", 2),
        [
            ("b", 3),
            ("e", 10)
        ],
        ("d", 4)
    ]

    sumTestList = huffpy.utilities.ndSum(testList)
    assert sumTestList == 20

def test_ndIndex():
    class AbstractNode:
        def __init__(self, left, right, char, containedChars):
            self.left = left
            self.right = right
            self.char = char
            self.containedChars = containedChars

    testList = AbstractNode(
        AbstractNode(None, None, "a", "a"),
        AbstractNode(
            AbstractNode(None, None, "b", "b"),
            AbstractNode(
                AbstractNode(None, None, "c", "c"),
                AbstractNode(None, None, "d", "d"),
                None,
                "cd"
            ),
            None,
            "bcd"
        ),
        None,
        "abcd"
    )

    _testListVisualisation = [
        "a",
        [
            "b",
            [
                "c",
                "d"
            ],
        ]
    ]
    
    assert huffpy.utilities.ndIndex(testList, "a") == "0"
    assert huffpy.utilities.ndIndex(testList, "b") == "10"
    assert huffpy.utilities.ndIndex(testList, "c") == "110"
    assert huffpy.utilities.ndIndex(testList, "d") == "111"

def test_crlfToLf():
    testString = "Hello, world!\r\nPoggers"
    assert huffpy.utilities.crlfToLf(testString) == "Hello, world!\nPoggers"