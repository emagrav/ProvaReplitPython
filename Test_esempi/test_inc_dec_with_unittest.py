import inc_dec    # The code to test
import unittest   # The test framework

class Test_TestIncrementDecrement(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(inc_dec.increment(3), 4)

    def test_decrement(self):
        self.assertEqual(inc_dec.decrement(3), 4)
    
    def test_upper(self):
        self.assertEqual("foo".upper(), 'FOO')
  
    def test_isupper(self):
        self.assertTrue("FOO".isupper())
        self.assertFalse("foo".isupper())
    
    def test_islower(self):
        self.assertTrue("FOO".islower())

if __name__ == '__main__':
    unittest.main()