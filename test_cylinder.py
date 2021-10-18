import unittest
from unittest import result
from FiveHomeWorkAssingment import Cylinder
import One
import two 

class TestCylinder(unittest.TestCase):

    def test_write_read(self):
        my_cylinder=Cylinder(1,1)
        expected_value_of_surface=12.56
        expected_value_of_volume=3.14
        result_surface =my_cylinder.surface_area()
        result_volume=my_cylinder.volume()
        self.assertEqual(expected_value_of_surface,result_surface)
        self.assertEqual(expected_value_of_volume,result_volume)
    
    def test_main(self):
        is_main = "__main__"
        self.assertEqual(TestCylinder.__name__,is_main)

if __name__=="__main__":
    unittest.main()