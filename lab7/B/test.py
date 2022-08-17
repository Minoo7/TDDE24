import unittest

def testf(lst):
    for a in lst:
        if a > 5:
            raise ValueError("a can't be greater than 5")
    return {"the": lst}

class TestTestf(unittest.TestCase):
    def test_testf_success(self):
        actual = testf(lst=[1, 2, 3, 4, 5])
        expected = {"the": [1, 2, 3, 4, 5]}
        self.assertEqual(actual, expected)
    
if __name__ == '__main__':
    unittest.main()

"""
def testf(lst):
    for a in lst:
        if a > 5:
            raise ValueError("a can't be greater than 5")
    return {"the": lst}

class TestTestf(unittest.TestCase):
    def test_testf_success(self):
        actual = testf(lst=[1, 2, 3, 4, 5])
        expected = {"the": [1, 2, 3, 4, 5]}
        self.assertEqual(actual, expected)
"""

"""
class Test_functions(unittest.TestCase):
    def test_traverse_success(self):
        lst = [6, 7, 8]
        test = lst
        actual = traverse(tree = test, left_fn = inner_node_fn, middle_fn = leaf_fn, right_fn = empty_tree_fn)
        self.assertEqual(actual, 43)
        lst = [[2, 5, 1], 7, 8]
        print(test)
        print(lst)
        self.assertEqual(actual, 16)
        #test = []
        #self.assertEqual(actual, 0)
        #traverse([6, 7, 8], inner_node_fn, leaf_fn, empty_tree_fn)

    def test_contains_key_success(self):
        actual = contains_key(search_key = 6, tree = [6, 7, 8])
        #xepected = True
        self.assertTrue(actual)
"""