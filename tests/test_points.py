import unittest
from main_second_dev2 import haversine_distance

class TestPointAnalysis(unittest.TestCase):
    
    def test_haversine_distance(self):
        self.assertLessEqual(haversine_distance(58.3810108,26.7187655, 58.3807102,26.7172642), 0.095)
        
if __name__ == "__main__":
    unittest.main()


