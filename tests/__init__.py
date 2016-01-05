import unittest

class InitializationTests(unittest.TestCase):

    def test_initialization(self):
        """
        Check the test suite runs by affirming 2+2=4
        """
        self.assertEqual(2+2, 4)


    #def test_import(self):
        """
        Ensure the test suite can import our module
        """
    #    try:
    #        import ../airbnb
    #    except ImportError:
    #        self.fail("Was not able to import the airbnb")

    def test_install(self):
        """
        Tests against installation of NumPY
        """
        try:
            import numpy as np
            np.test()
        except ImportError:
            self.fail("Was not able to import NumPy")