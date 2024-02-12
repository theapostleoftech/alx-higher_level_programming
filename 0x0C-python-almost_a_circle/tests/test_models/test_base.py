#!/usr/bin/python3
import json as js
import unittest
from unittest.mock import patch, Mock

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


class TestDraw(unittest.TestCase):
    """
    Test cases for the draw function
    """
    @patch('turtle.Turtle')
    @patch('turtle.Screen')
    def test_draw(self, mock_screen, mock_turtle):
        # Create mock objects for a rectangle and a square
        mock_rectangle = Mock(x=0, y=0, width=10, height=20)
        mock_square = Mock(x=10, y=10, width=20, height=20)

        # Call the function with the mock objects
        Base.draw([mock_rectangle], [mock_square])

        # Assert that the turtle methods were called with the correct arguments
        calls = [((0, 0),), ((10, 0),), ((10, 20),), ((0, 20),), ((0, 0),), ((10, 10),), ((30, 10),), ((30, 30),),
                 ((10, 30),), ((10, 10),)]
        mock_turtle.return_value.goto.assert_has_calls(calls)
        calls = [((10,),), ((20,),), ((10,),), ((20,),), ((20,),), ((20,),), ((20,),), ((20,),)]
        mock_turtle.return_value.forward.assert_has_calls(calls)


if __name__ == '__main__':
    unittest.main()
