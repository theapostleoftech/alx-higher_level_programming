#!/usr/bin/python3
"""This contains base class that other class will subclass from"""
import json as js
import csv as cs
import os
import turtle


class Base:
    """Base class to manage id attribute in other classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """This is the constructor for the Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
            pass

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if (type(list_dictionaries) != list
                or not all(type(i) == dict for i in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return js.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save JSON representation to file"""
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dictionary = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dictionary))

    @staticmethod
    def from_json_string(json_string):
        """Returns list of JSON string representations"""
        list_of_json_string = []

        if json_string is not None and json_string != '':
            if type(json_string) != str:
                raise TypeError("json_string must be a string")
            list_of_json_string = js.loads(json_string)

        return list_of_json_string

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""

        file_name = cls.__name__ + ".json"
        list_of_instances = []
        list_dictionaries = []

        if os.path.exists(file_name):
            with open(file_name, 'r') as my_file:
                str_read = my_file.read()
                list_dictionaries = cls.from_json_string(str_read)
                for dictionary in list_dictionaries:
                    list_of_instances.append(cls.create(**dictionary))
        return list_of_instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes list_objs and saves to file"""

        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = cs.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes CSV format from a file"""

        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = cs.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [
                    dict(
                        [
                            key, int(value)
                        ]
                        for key, value in d.items()
                    )
                    for d in list_dicts
                ]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.
        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        tortoise = turtle.Turtle()
        tortoise.screen.bgcolor("#0b3a87")
        tortoise.pensize(3)
        tortoise.shape("turtle")

        tortoise.color("#c23bcc")
        for rectangle in list_rectangles:
            tortoise.showturtle()
            tortoise.up()
            tortoise.goto(rectangle.x, rectangle.y)
            tortoise.down()
            for i in range(2):
                tortoise.forward(rectangle.width)
                tortoise.left(90)
                tortoise.forward(rectangle.height)
                tortoise.left(90)
            tortoise.hideturtle()

        tortoise.color("#7d0707")
        for square in list_squares:
            tortoise.showturtle()
            tortoise.up()
            tortoise.goto(square.x, square.y)
            tortoise.down()
            for i in range(2):
                tortoise.forward(square.width)
                tortoise.left(90)
                tortoise.forward(square.height)
                tortoise.left(90)
            tortoise.hideturtle()

        turtle.done()

