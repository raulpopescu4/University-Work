import re
import unittest

from iterable_data_structure.data_structure import IterableDataStructure


class IterableDataStructureTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__test_data_structure = IterableDataStructure()

    def test_setitem(self):
        self.__test_data_structure.__setitem__('id', 5)
        self.assertEqual(self.__test_data_structure.__len__(), 1)

    def test_getitem(self):
        self.__test_data_structure.__setitem__('id', 5)
        item_from_dictionary = self.__test_data_structure.__getitem__('id')
        self.assertEqual(item_from_dictionary, 5)

    def test_delitem(self):
        self.__test_data_structure.__setitem__('id', 5)
        self.__test_data_structure.__delitem__('id')
        self.assertEqual(self.__test_data_structure.__len__(), 0)

    def test_iter(self):
        self.__test_data_structure.__setitem__('id_client1', 5)
        self.__test_data_structure.__setitem__('id_client2', 13)
        data_structure_as_list = self.__test_data_structure.list()
        self.__test_data_structure.__iter__()
        self.assertEqual(data_structure_as_list[self.__test_data_structure.key], 13)

    def test_next(self):
        self.__test_data_structure.__setitem__('id_client1', 5)
        self.__test_data_structure.__setitem__('id_client2', 13)
        self.__test_data_structure.__iter__()
        pair_value = self.__test_data_structure.__next__()
        self.assertEqual(pair_value, 5)

    def test_next_exception(self):
        self.__test_data_structure.__setitem__('id_client1', 5)
        self.__test_data_structure.__setitem__('id_client2', 13)
        self.__test_data_structure.__iter__()
        self.__test_data_structure.__next__()
        self.__test_data_structure.__next__()
        with self.assertRaises(StopIteration):
            self.__test_data_structure.__next__()

    def test_gnome_sort(self):
        self.__test_data_structure.__setitem__(7, 12)
        self.__test_data_structure.__setitem__(1, 56)
        self.__test_data_structure.__setitem__(2, 78)
        dictionary_after_sort = {1: 56, 2: 78, 7:  12}

        dictionary_to_be_sorted = list(map(list, self.__test_data_structure._dictionary.items()))
        sorted_dictionary = self.__test_data_structure.gnome_sort(dictionary_to_be_sorted)
        sorted_dictionary = {item[0]: item[1] for item in sorted_dictionary}

        self.assertEqual(dictionary_after_sort, sorted_dictionary)

    def test_gnome_sort_reverse(self):
        self.__test_data_structure.__setitem__(7, 12)
        self.__test_data_structure.__setitem__(1, 56)
        self.__test_data_structure.__setitem__(2, 78)
        expected_dictionary_after_sort = {2: 78, 1: 56, 7: 12}

        dictionary_to_be_sorted = list(map(list, self.__test_data_structure._dictionary.items()))
        sorted_dictionary = self.__test_data_structure.gnome_sort(dictionary_to_be_sorted, key=lambda key: key[1], reverse_order=True)
        sorted_dictionary = {item[0]: item[1] for item in sorted_dictionary}

        self.assertEqual(expected_dictionary_after_sort, sorted_dictionary)

    def test_filter_elements_by_substring(self):
        people = {3: "Alan",
                  8: "Ann",
                  1: "Khan"}

        filter_element = 'an'
        names_found = self.__test_data_structure.filter_elements_from_a_list(people.values(), lambda value: re.findall(filter_element.lower(), value.lower()))
        self.assertEqual(len(names_found), 3)

    def tearDown(self) -> None:
        pass