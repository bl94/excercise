import unittest
from Projects.p import write_read
import exceptions_and_errors

class TestExceptions(unittest.TestCase):
   
    def test_ask(self):
        square_number=4
        result = exceptions_and_errors.ask()
        self.assertEqual(square_number,result)
   
    def test_write_read(self):
        text="Lost connection\nFive days\nSix days"
        result = write_read()
        self.assertEqual(text,result)

if __name__=="__main__":
    unittest.main()