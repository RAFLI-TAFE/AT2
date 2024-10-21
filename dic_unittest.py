import unittest
from dic_func import add_value, delete_value, sort_values, search_value

class TestDictFunctions(unittest.TestCase):

    # Test adding a new actor
    def test_add_value(self):
        my_dict = {}  # Start with an empty dictionary
        result = add_value(my_dict, "New Actor", 1990)  # Add a new actor
        self.assertEqual(my_dict, {"New Actor": 1990})  # Check if the actor was added
        self.assertEqual(result, "'GREAT, now New Actor' with year '1990' has been added.")  # Check return message

    # Test deleting an actor
    def test_delete_value(self):
        my_dict = {"Marlon Brando": 1924, "Robert De Niro": 1943}  # Dictionary with actors
        result = delete_value(my_dict, "Marlon Brando")  # Delete Marlon Brando
        self.assertEqual(my_dict, {"Robert De Niro": 1943})  # Check if the actor was removed
        self.assertEqual(result, "GREAT, now Marlon Brando has been deleted from the dictionary.")  # Check return message

    # Test trying to delete an actor that doesn't exist
    def test_delete_not_found(self):
        my_dict = {"Marlon Brando": 1924, "Robert De Niro": 1943}  # Dictionary with actors
        result = delete_value(my_dict, "Non-Existent Actor")  # Try to delete a non-existent actor
        self.assertEqual(my_dict, {"Marlon Brando": 1924, "Robert De Niro": 1943})  # Check no change in dictionary
        self.assertEqual(result, "Sorry, Non-Existent Actor was not found in the dictionary.")  # Check error message

    # Test sorting actors in ascending order
    def test_sort_values_asc(self):
        my_dict = {"Denzel Washington": 1954, "Al Pacino": 1940, "Tom Hanks": 1956}  # Sample dictionary
        sorted_result = sort_values(my_dict, 'asc')  # Sort in ascending order
        self.assertEqual(sorted_result, [('Al Pacino', 1940), ('Denzel Washington', 1954), ('Tom Hanks', 1956)])  # Check order

    # Test sorting actors in descending order
    def test_sort_values_desc(self):
        my_dict = {"Denzel Washington": 1954, "Al Pacino": 1940, "Tom Hanks": 1956}  # Sample dictionary
        sorted_result = sort_values(my_dict, 'desc')  # Sort in descending order
        self.assertEqual(sorted_result, [('Tom Hanks', 1956), ('Denzel Washington', 1954), ('Al Pacino', 1940)])  # Check order

    # Test searching for an existing actor
    def test_search_value_found(self):
        my_dict = {"Denzel Washington": 1954, "Al Pacino": 1940}  # Sample dictionary
        result = search_value(my_dict, "Denzel Washington")  # Search for Denzel Washington
        self.assertEqual(result, "Denzel Washington's year is 1954.")  # Check correct year

    # Test searching for an actor that doesn't exist
    def test_search_value_not_found(self):
        my_dict = {"Marlon Brando": 1924, "Robert De Niro": 1943}  # Sample dictionary
        result = search_value(my_dict, "Non-Existent Actor")  # Search for a non-existent actor
        self.assertEqual(result, "Sorry, Non-Existent Actor was not found in the dictionary.")  # Check error message

# Run the tests when the file is executed
if __name__ == '__main__':
    unittest.main()