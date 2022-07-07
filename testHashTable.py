import unittest

from hash_table import *

class HashTableTest(unittest.TestCase):
    def test_insert(self):
        key = 'apple'
        value = 'яблоко'
        table = HashTable()
        table.insert(key, value)
        self.assertTrue(key in table)
        self.assertEqual(value, table[key])


    def test_insert_same_keys(self):
        table = HashTable()
        table.insert(1, 2)
        with self.assertRaises(ValueError):
            table.insert(1, 2)

    def test_get_keys(self):
        key = 'apple'
        value = 'яблоко'
        table = HashTable()
        table.insert(key, value)
        key = 'lemon'
        value = 'лимон'
        table.insert(key, value)
        actual = table.get_keys()
        expected = ['apple', 'lemon']
        self.assertEqual(expected, actual)

