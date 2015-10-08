import unittest
from linear_function import linear_search

class SearchTest(unittest.TestCase):
  def test_linear_search(self):
    
    #ascending
    self.assertEqual(linear_search ( [0, 2, 4, 6, 8], 5, -1, 1, "LessThanEquals"), ("NotFound", "X") )
    self.assertEqual(linear_search ( [0, 2, 4, 6, 8], 5, 0, 1, "LessThan"), ("NotFound", "X") )
    self.assertEqual(linear_search ( [0, 2, 4, 6, 8], 5, 0, 1, "Equals"), ("FoundExact", 0) )
    self.assertEqual(linear_search ( [0, 2, 4, 6, 8], 5, 1, 1, "Equals"), ("NotFound", "X") )
    self.assertEqual(linear_search ( [0, 2, 4, 6, 8], 5, 2, 1, "GreaterThanEquals"), ("FoundExact", 1) )
    self.assertEqual(linear_search ( [0, 2, 4, 6, 8], 5, 2, 1, "GreaterThan"), ("FoundGreater", 2) )

    #descending
    self.assertEqual(linear_search ( [8, 6, 4, 2, 0], 5, -1, 0, "LessThan"), ("NotFound", "X") )
    self.assertEqual(linear_search ( [8, 6, 4, 2, 0], 5, 0, 0, "LessThan"), ("NotFound", "X") )
    self.assertEqual(linear_search ( [8, 6, 4, 2, 0], 5, 4, 0, "LessThanEquals"), ("FoundExact", 2) )
    self.assertEqual(linear_search ( [8, 6, 4, 2, 0], 5, 8, 0, "Equals"), ("FoundExact", 0) )
    self.assertEqual(linear_search ( [8, 6, 4, 2, 0], 5, 5, 0, "GreaterThanEquals"), ("FoundGreater", 1) )
    self.assertEqual(linear_search ( [8, 6, 4, 2, 0], 5, 2, 0, "GreaterThanEquals"), ("FoundExact", 3) )
    self.assertEqual(linear_search ( [8, 6, 4, 2, 0], 5, 8, 0, "GreaterThan"), ("NotFound", "X") )
    self.assertEqual(linear_search ( [8, 6, 4, 2, 0], 5, 9, 0, "GreaterThan"), ("NotFound", "X") )

    #invalid inputs
    self.assertEqual(linear_search ( [8, 6, 4, 2, 0], 7, 9, 0, "GreaterThan"), "n_items doesn't match" )
    self.assertEqual(linear_search ( [0, 2, 4, 6, 8], 1, 2, 1, "GreaterThan"), "n_items doesn't match" )
    self.assertEqual(linear_search ( [8, 6, 4, 2, 0], 5, 8, 2, "Equals"), "Check ascending value" )
    self.assertEqual(linear_search ( [0, 2, 4, 6, 8], 5, 0, -1, "LessThan"), "Check ascending value" )
    self.assertEqual(linear_search ( [0, 2, 4, 6, 8], 5, -1, 1, "Less"), "Check match type" )
    self.assertEqual(linear_search ( [8, 6, 4, 2, 0], 5, 8, 0, "Equaals"), "Check match type" )

if __name__ == "__main__": 
  unittest.main()