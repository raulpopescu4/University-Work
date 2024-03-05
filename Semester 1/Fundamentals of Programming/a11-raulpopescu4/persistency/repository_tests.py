import unittest

from persistency.repository import Repository
from validators_and_exceptions import RepositoryException


class RepositoryTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__repository = Repository()

    def test_add(self):
        entity = 1
        self.__repository.add(entity)
        self.assertEqual(len(self.__repository.get_all()), 1)

    def test_add_exception(self):
        entity = 1
        self.__repository.add(entity)
        with self.assertRaises(RepositoryException):
            self.__repository.add(entity)

    def test_get_all(self):
        self.assertEqual(self.__repository.get_all(), [])

    def test_search(self):
        entity = 1
        self.__repository.add(entity)
        test_entity = self.__repository.search(entity)
        self.assertEqual(entity, test_entity)

    def test_search_exception(self):
        entity = 1
        self.__repository.add(entity)
        with self.assertRaises(RepositoryException):
            self.__repository.search(2)


    def tearDown(self) -> None:
        pass