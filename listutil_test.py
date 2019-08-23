import unittest
from listutil import unique

class ListutilTest(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual([], unique([]))
    
    def test_one_item(self):
        self.assertListEqual(['apple'], unique(['apple']))

    def test_many_one_item(self):
        self.assertEqual([3], unique([3,3,3,3,3]))

    def test_same_many_item_in_list(self):
        self.assertEqual([2,3], unique([2,2,2,3,3,2,3,3]))

    def test_list_in_list(self):
        self.assertEqual([10,20,30,[10,20],[10,20,30]], unique([10,20,30,[10,20],[10,20,30]]))

    def test_diftype(self):
        self.assertEqual([50,'grape',['apple','watermelon']], unique([50,'grape',['apple','watermelon']]))

    def test_assertion_error(self):
        with self.assertRaises(ValueError):
            unique(50)

if __name__ == "__main__":
    unittest.main()