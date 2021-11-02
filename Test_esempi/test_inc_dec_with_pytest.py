import inc_dec    # The code to test

def test_increment():
    assert inc_dec.increment(3) == 4

def test_decrement():
    assert inc_dec.decrement(3) == 4
  
""" 
def test_upper(self):
    #self.assertEqual("foo".upper(), 'FOO')
    assert "foo".upper() == 'FOO'

def test_isupper(self):
    assert "FOO".isupper()
    assert not "foo".isupper()
    
def test_islower(self):
    assert "FOO".islower() 
"""