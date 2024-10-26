### RAFLI (20115423)


import unittest
from list_func import add_value, delete_value, sort_value, search_value

class TestListFunctions(unittest.TestCase):
    
    def test_add_value(self):
        test_list = []
        add_value(test_list, "Rafli")  # Add an Rafli to the list
        self.assertIn("Rafli", test_list)  # Check if the value (Rafli) is in the list

    def test_delete_value(self):
        test_list = ["Rafli", "Tom Hanks", "Brad Pitt"]
        delete_value(test_list, "Tom Hanks")  # Delete "Tom Hanks"
        self.assertNotIn("Tom Hanks", test_list)  # Check if "Tom Hanks" is removed

    def test_delete_not_found(self):
        test_list = ["Rafli", "Tom Hanks"]
        delete_value(test_list, "Brad Pitt")  # Attempt to delete a non-existent actor
        self.assertEqual(test_list, ["Rafli", "Tom Hanks"])  # Ensure the list remains unchanged

    def test_sort_value_ascending(self):
        test_list = ["Charlie", "Alice", "Bob"]
        sort_value(test_list, 'asc')  # Sort in ascending order
        self.assertEqual(test_list, ["Alice", "Bob", "Charlie"])  # Check if sorted correctly

    def test_sort_value_descending(self):
        test_list = ["Charlie", "Alice", "Bob"]
        sort_value(test_list, 'desc')  # Sort in descending order
        self.assertEqual(test_list, ["Charlie", "Bob", "Alice"])  # Check if sorted correctly

    def test_search_value_found(self):
        test_list = ["Rafli", "Tom Hanks"]
        result = search_value(test_list, "Rafli")  # Search for "Rafli"
        self.assertIsNone(result)  # Since there's no return value, assert it doesn't raise an error

    def test_search_value_not_found(self):
        test_list = ["Rafli", "Tom Hanks"]
        result = search_value(test_list, "Brad Pitt")  # Search for a non-existent actor
        self.assertIsNone(result)  # Since there's no return value, assert it does not raise an error

#Running the unittest
if __name__ == '__main__':
    unittest.main()
