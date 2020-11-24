# testing

# functions
def get_formatted_name(first, last, middle=""):
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()

def get_upper_string(s):
    return s.upper()

# tests
import unittest

class NamesTestCase(unittest.TestCase):
    """Tests for get_formatted_name(first, last)."""
    def test_get_formatted_name(self):
        self.assertEqual(get_formatted_name('janis', 'joplin'), 'Janis Joplin')
        self.assertEqual(get_formatted_name('janis', 'joplin', 'middle'), 'Janis Middle Joplin')

    def test_get_upper_string(self):
        self.assertEqual(get_upper_string("asdf"), "ASDF")

"""
The if block below looks at a special variable, __name__, which is set when the program is executed. 
If this file is being run as the main program, the value of __name__ is set to '__main__'. 
In this case, we call unittest.main(), which runs the test case. 

When a testing framework imports this file, 
the value of __name__ won’t be '__main__' and this block will not be executed.
"""
if __name__ == '__main__':
    unittest.main()

