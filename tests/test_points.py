import unittest
from preprocess import *
from main_second_dev2 import haversine_distance, euclidean_distance

class TestPointAnalysis(unittest.TestCase):
    
    def test_haversine_distance(self):
        self.assertLessEqual(haversine_distance(58.3810108,26.7187655, 58.3807102,26.7172642), 0.095)
    
    def test_euclidean_distance(self):
        p1 = point("A", 0,0, "A")
        p2 = point("B", 3,4, "B")
        self.assertEqual(euclidean_distance(p1,p2), 5)
        
if __name__ == "__main__":
    unittest.main()


