#!/usr/bin/python3
import unittest

from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Class for testing Rectangle class
    """

    def setUp(self):
        """
        Set up for the tests.
        """
        self.r = Rectangle(5, 10)

    def tearDown(self):
        """
        Clean up after the tests.
        """
        del self.r

    def test_initialization(self):
        """
        Test for correct initialization of the rectangle.
        """
        self.assertEqual(self.r.width, 5)
        self.assertEqual(self.r.height, 10)
        self.assertEqual(self.r.x, 0)
        self.assertEqual(self.r.y, 0)

    def test_area(self):
        """
        Test the area method.
        """
        self.assertEqual(self.r.area(), 50)

    def test_str(self):
        """
        Test the __str__ method.
        """
        self.assertEqual(str(self.r),
                         "[Rectangle] ({}) 0/0 - 5/10".format(self.r.id))

    def test_update(self):
        """
        Test the update method.
        """
        self.r.update(89, 2, 3, 4, 5)
        self.assertEqual(self.r.id, 89)
        self.assertEqual(self.r.width, 2)
        self.assertEqual(self.r.height, 3)
        self.assertEqual(self.r.x, 4)
        self.assertEqual(self.r.y, 5)

    def test_to_dictionary(self):
        """
        Test the to_dictionary method.
        """
        r_dict = self.r.to_dictionary()
        expected_dict = {
            "id": self.r.id,
            "width": 5,
            "height": 10,
            "x": 0, "y": 0
        }
        self.assertEqual(r_dict, expected_dict)

    def test_type_errors(self):
        """
        Test type errors for width, height, x, and y.
        """
        with self.assertRaises(TypeError):
            r = Rectangle("5", 10)
        with self.assertRaises(TypeError):
            r = Rectangle(5, "10")
        with self.assertRaises(TypeError):
            r = Rectangle(5, 10, "0")
        with self.assertRaises(TypeError):
            r = Rectangle(5, 10, 0, "0")

    def test_value_errors(self):
        """
        Test value errors for width, height, x, and y.
        """
        with self.assertRaises(ValueError):
            r = Rectangle(-5, 10)
        with self.assertRaises(ValueError):
            r = Rectangle(5, -10)
        with self.assertRaises(ValueError):
            r = Rectangle(5, 10, -1)
        with self.assertRaises(ValueError):
            r = Rectangle(5, 10, 0, -1)

    def test_update_type_errors(self):
        """
        Test type errors for update method.
        """
        with self.assertRaises(TypeError):
            self.r.update(width="5")
        with self.assertRaises(TypeError):
            self.r.update(height="10")
        with self.assertRaises(TypeError):
            self.r.update(x="0")
        with self.assertRaises(TypeError):
            self.r.update(y="0")

    def test_update_value_errors(self):
        """
        Test value errors for update method.
        """
        with self.assertRaises(ValueError):
            self.r.update(width=-5)
        with self.assertRaises(ValueError):
            self.r.update(height=-10)
        with self.assertRaises(ValueError):
            self.r.update(x=-1)
        with self.assertRaises(ValueError):
            self.r.update(y=-1)


if __name__ == "__main__":
    unittest.main()
