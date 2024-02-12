import unittest

from models.square import Square


class TestSquare(unittest.TestCase):
    """
    Class for testing Square class
    """

    def setUp(self):
        """
        Set up for the tests.
        """
        self.s = Square(5)

    def tearDown(self):
        """
        Clean up after the tests.
        """
        del self.s

    def test_initialization(self):
        """
        Test for correct initialization of the square.
        """
        self.assertEqual(self.s.size, 5)
        self.assertEqual(self.s.x, 0)
        self.assertEqual(self.s.y, 0)

    def test_str(self):
        """
        Test the __str__ method.
        """
        self.assertEqual(str(self.s), "[Square] ({}) 0/0 - 5".format(self.s.id))

    def test_update(self):
        """
        Test the update method.
        """
        self.s.update(89, 2, 3, 4)
        self.assertEqual(self.s.id, 89)
        self.assertEqual(self.s.size, 2)
        self.assertEqual(self.s.x, 3)
        self.assertEqual(self.s.y, 4)

    def test_to_dictionary(self):
        """
        Test the to_dictionary method.
        """
        s_dict = self.s.to_dictionary()
        expected_dict = {"id": self.s.id, "size": 5, "x": 0, "y": 0}
        self.assertEqual(s_dict, expected_dict)

    def test_type_errors(self):
        """
        Test type errors for size, x, and y.
        """
        with self.assertRaises(TypeError):
            s = Square("5")
        with self.assertRaises(TypeError):
            s = Square(5, "0")
        with self.assertRaises(TypeError):
            s = Square(5, 0, "0")

    def test_value_errors(self):
        """
        Test value errors for size, x, and y.
        """
        with self.assertRaises(ValueError):
            s = Square(-5)
        with self.assertRaises(ValueError):
            s = Square(5, -1)
        with self.assertRaises(ValueError):
            s = Square(5, 0, -1)


if __name__ == "__main__":
    unittest.main()
