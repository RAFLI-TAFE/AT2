# RAFLI (20115423)

#1.	Write a Python program that provides the ability to: 
#1.1.	Create a list from scenario about actors, movies, and games
#1.2.	Add a value to the list 
#1.3.	Delete a value from the list 
#1.4.	Sort all the data in the list in the ascending order. Sort all the data in the list in the descending order. 
#1.5.	Search for the value in the list asking user for input.
#2.	Debug and test your program. You must write unit tests to test the functionality specified above. Screenshot your test results. 
#3.	Comment your programs and upload your evidence in compressed format into the Blackboard assessment area.

# 1.1 Creating lists of actors, movies, and games
actors = ["Marlon Brando", "Robert De Niro", "Denzel Washington", "Al Pacino", 
          "Tom Hanks", "Daniel Day-Lewis", "Robert De Niro", "Tom Hanks", 
          "Brad Pitt", "Angelina Jolie", "Christian Bale", "Paul Newman"]
movies = ["The Shawshank Redemption", "Titanic", "The Matrix", "Goodfellas", "The Godfather", 
          "The Dark Knight", "Pulp Fiction", "Shutter Island", "Gladiator", 
          "The Lord of the Rings", "Interstellar", "Casablanca"]
games = ["The Witcher 3", "Tetris", "Minecraft", "The Last of Us", 
         "GTA V", "God of War", "Fortnite", "Red Dead Redemption 2", "Halo", 
         "Super Mario Bros", "Overwatch", "Call of Duty"]

# 1.2 Add a value (item) to the list 
def add_value(lst, value):
    lst.append(value)  # append("value") adds the value to the end of the list
    print(f"GREAT '{value}' has been successfully added to the list.")
    
#1.3 Delete a value (item) from the list 
def delete_value(lst, value):
    if value in lst:  # Check if the value exists in the list
        lst.remove(value)  # .remove() deletes the value (item) from the list
        print(f"'{value}' has been removed from the list.")
    else:
        print(f"Sorry, '{value}' was not found in the list.")

#1.4 Sort all the data in the list in the ascending order or descending order. 
def sort_value(lst, order):  # This defines the function sort_value which takes two parameters: lst and order
    if order == 'asc':
        lst.sort()  # lst.sort() sorts the list in ascending order.
    elif order == 'desc': 
        lst.sort(reverse=True)  # lst.sort(reverse=True) sorts the list in descending order.
    return lst  # After sorting the list, the function returns the sorted version of lst

#1.5 Search for the value in the list asking user for input.
def search_value(lst, value):  # Check if the specified value exists in the list
    if value in lst:  # If the value is found, print a message indicating its presence in the list
        print(f"GREAT, '{value}' is found in the list.")
    else:
        print(f"Sorry, '{value}' was not found in the list.")  # If the value is not found, print a message indicating its absence from the list


def play():
    # Main interactive loop
    while True:
        # Ask user to choose the category
        category_type = input("Choose the category (actors, movies, games, exit): ").strip().lower()

        if category_type == 'exit':
            print("Thanks for playing! :) ")
            break  # Exit the program
        elif category_type == 'actors':
            list_type = actors
        elif category_type == 'movies':
            list_type = movies
        elif category_type == 'games':
            list_type = games
        else:
            print("INPUT IS NOT RECOGNIZED!!!.")
            continue

        # Inner loop for operations on the selected category
        while True:
            # Ask user to choose the instruction
            instruction_type = input("Choose an action (add, delete, sort, search, back): ").strip().lower()

            if instruction_type == 'back':
                print("Returning to category selection.")  # Added a message for clarity
                break  # Go back to the category selection
            elif instruction_type == 'add':
                value = input("Enter the value to add: ")
                add_value(list_type, value)  # Call function to add value
            elif instruction_type == 'delete':
                value = input("Enter the value to delete: ")
                delete_value(list_type, value)  # Call function to delete value
            elif instruction_type == 'sort':
                order = input("Enter sorting order (asc for ascending, desc for descending): ").strip().lower()
                sort_value(list_type, order)  # Call the correct function to sort list
            elif instruction_type == 'search':
                value = input("Enter the value to search: ")
                search_value(list_type, value)  # Call function to search for value
            else:
                print("ACTION IS NOT RECOGNIZED!!!.")
            
            # Display current list after ACTION
            print("Current List:", list_type)

if __name__ == '__main__':
    play()