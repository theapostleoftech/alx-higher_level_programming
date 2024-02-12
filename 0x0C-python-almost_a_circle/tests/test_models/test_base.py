#!/usr/bin/python3
import inspect
import json as js
import unittest

from models.base import Base
from models.square import Square


class TestBase(unittest.TestCase):
    """
    Test cases for the Base Class
    """

    def setUp(self):
        """
        Set up for the tests.
        """
        self.b = Base()

    def tearDown(self):
        """
        Clean up after the tests.
        """
        del self.b

    def test_initialization(self):
        """
        Test for correct initialization of the base.
        """
        self.assertEqual(self.b.id, 3)

    def test_no_id(self):
        """
        Testing for no id
        :return: none
        """
        b = Base()
        self.assertEqual(12, b.id)

    def test_valid_id(self):
        """
        Testing for an id
        :return: a valid id
        """
        b = Base(2)
        self.assertEqual(2, b.id)

    def test_id_zero(self):
        """
        Testing for an id of 0
        :return: zero
        """
        b = Base(0)
        self.assertEqual(0, b.id)

    def test_negative_id(self):
        """
        Testing for a negative id
        :return: a negative id
        """
        b = Base(-2)
        self.assertEqual(-2, b.id)

    def test_string_id(self):
        """
        Testing for string as an id
        :return: string as an id
        """
        b = Base("ALX")
        self.assertEqual("ALX", b.id)

    def test_list_id(self):
        """
        Testing a list as an id
        :return: a list as an id
        """
        b = Base([1, 2, 3])
        self.assertEqual([1, 2, 3], b.id)

    def test_dict_id(self):
        """
        Testing a dictionary as an id
        :return: a dictionary as an id
        """
        b = Base({"id": 2})
        self.assertEqual({"id": 2}, b.id)

    def test_tuple_id(self):
        """
        Testing a tuple as an id
        :return: a tuple as an id
        """
        b = Base((1, 2,))
        self.assertEqual((1, 2,), b.id)

    def test_json_string_type(self):
        """
        Testing the json string
        :return: a json string
        """
        sq = Square(1)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(type(json_string), str)

    def test_json_string_value(self):
        """
        Testing the json string
        :return: a json string
        """
        sq = Square(1, 0, 0, 2)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(js.loads(json_string),
                         [{"id": 2, "y": 0, "size": 1, "x": 0}])

    def test_json_None(self):
        """
        Testing the json string
        :return: a json string
        """
        sq = Square(1, 0, 0, 2)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_json_Empty(self):
        """
        Testing the json string
        :return: a json string
        """
        sq = Square(1, 0, 0, 2)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    pass


# class TestSquare(unittest.TestCase):
#     """
#     class for testing Base class' methods
#     """
#
#     @classmethod
#     def setUpClass(cls):
#         """
#         Set up class method for the doc tests
#         """
#         cls.setup = inspect.getmembers(Base, inspect.isfunction)
#
#     def test_module_docstring(self):
#         """
#         Testing if module docstring documentation exist
#         """
#         self.assertTrue(len(Base.__doc__) >= 1)
#
#     def test_class_docstring(self):
#         """
#         Testing if class docstring documentation exist
#         """
#         self.assertTrue(len(Base.__doc__) >= 1)
#
#     def test_func_docstrings(self):
#         """
#         Testing if methods docstring documentation exist
#         """
#         for func in self.setup:
#             self.assertTrue(len(func[1].__doc__) >= 1)


if __name__ == '__main__':
    unittest.main()
