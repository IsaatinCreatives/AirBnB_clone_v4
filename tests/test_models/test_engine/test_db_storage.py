#!/usr/bin/python3
"""
Test db storage
"""
from io import StringIO
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import unittest
from unittest.mock import patch


class Count(unittest.TestCase):
    """Unittest for the db storage """

    def test_count(self):
        """checks the total count for all items"""
        with patch("sys.stdout", new=StringIO()) as f:
            objects = storage.count()
            print("All objects: {}".format(objects))
            self.assertEqual(f"All objects: {objects}", f.getvalue().strip())

    def test_count_states(self):
        """checks the total count of state objects"""
        with patch("sys.stdout", new=StringIO()) as f:
            states = storage.count(State)
            print("State objects: {}".format(states))
            self.assertEqual(f"State objects: {states}", f.getvalue().strip())

    def test_count_users(self):
        """checks for total count for users objects"""
        with patch("sys.stdout", new=StringIO()) as f:
            users = storage.count(User)
            print("User objects: {}".format(users))
            self.assertEqual(f"User objects: {users}", f.getvalue().strip())

    def test_count_reviews(self):
        """checks for total count for reviews objects"""
        with patch("sys.stdout", new=StringIO()) as f:
            revws = storage.count(Review)
            print("Review objects: {}".format(revws))
            self.assertEqual(f"Review objects: {revws}", f.getvalue().strip())

    def test_count_places(self):
        """checks for total count for places objects"""
        with patch("sys.stdout", new=StringIO()) as f:
            places = storage.count(Place)
            print("Place objects: {}".format(places))
            self.assertEqual(f"Place objects: {places}", f.getvalue().strip())

    def test_count_cities(self):
        """checks for total count for city objects"""
        with patch("sys.stdout", new=StringIO()) as f:
            cities = storage.count(City)
            print("City objects: {}".format(cities))
            self.assertEqual(f"City objects: {cities}", f.getvalue().strip())

    def test_count_amenities(self):
        """checks for total count for amenity objects"""
        with patch("sys.stdout", new=StringIO()) as f:
            amns = storage.count(Amenity)
            print("Amenity objects: {}".format(amns))
            self.assertEqual(f"Amenity objects: {amns}", f.getvalue().strip())


if __name__ == '__main__':
    unittest.main()
