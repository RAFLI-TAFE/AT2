### RAFLI (20115423) ###

# •	A dictionary that stores at least 12 of your favourite actors/actresses’ names and birthdays.
# •	A list that stores at least 12 of your favourite movies and release year.
# •	A list that stores at least 12 of your favourite games and release year.
# 1.	Write a Python program that provides the ability to: 
# 1.1.	Create a dictionary from the scenario above
# 1.2.	Add a value to the dictionary
# 1.3.	Delete a value from the dictionary
# 1.4.	Sort all the data in the dictionary in the ascending order. Sort all the data in the dictionary in the descending order. 
# 1.5.	Search for the value in the dictionary asking user for input.
# 2.	Debug and test your program. You must write unit tests to test the functionality specified above. Screenshot your test results. 
# 3.	Comment your programs and upload your evidence in compressed format into the Blackboard assessment area.

# 1.1. Create a dictionary for Actors, Movies, and Games
actors_dict = {
    "Marlon Brando": 1924,
    "Robert De Niro": 1943,
    "Denzel Washington": 1954,
    "Al Pacino": 1940,
    "Tom Hanks": 1956,
    "Daniel Day-Lewis": 1957,
    "Brad Pitt": 1963,
    "Angelina Jolie": 1975,
    "Christian Bale": 1974,
    "Paul Newman": 1925,
    "Morgan Freeman": 1937,}

movies_dict = {
    "The Shawshank Redemption": 1994,
    "Titanic": 1997,
    "The Matrix": 1999,
    "Goodfellas": 1990,
    "The Godfather": 1972,
    "The Dark Knight": 2008,
    "Pulp Fiction": 1994,
    "Shutter Island": 2010,
    "Gladiator": 2000,
    "The Lord of the Rings": 2001,
    "Interstellar": 2014,
    "Casablanca": 1942,}

games_dict = {
    "The Witcher 3": 2015,
    "Tetris": 1984,
    "Minecraft": 2011,
    "The Last of Us": 2013,
    "GTA V": 2013,
    "God of War": 2018,
    "Fortnite": 2017,
    "Red Dead Redemption 2": 2018,
    "Halo": 2001,
    "Super Mario Bros": 1985,
    "Overwatch": 2016,
    "Call of Duty": 2003,}

# 1.2. Add a value to the dictionary
def add_value(category_dict, name, year):
    category_dict[name] = year  # Adding new value (actor/movie/game) and its year to the dictionary
    return f"'GREAT, now {name}' with year '{year}' has been added."  # Return a message

# 1.3. Delete a value from the dictionary
def delete_value(category_dict, value):
    if value in category_dict:  # Check if the value is in the dictionary
        del category_dict[value]  # Remove the value from the dictionary
        return f"GREAT, now {value} has been deleted from the dictionary."  # Return a message
    else:
        return f"Sorry, {value} was not found in the dictionary."  # Return an error message

# 1.4. Sort all the data in the dictionary in the ascending or descending order.
def sort_values(category_dict, order):  # Function definition with two parameters
    if order == 'asc':  # Asking if user wants ascending order
        return sorted(category_dict.items())  # Sort the dictionary in ascending order
    elif order == 'desc':  # Asking if user wants descending order
        return sorted(category_dict.items(), reverse=True)  # Sort the dictionary in descending order

# 1.5. Search for the value in the dictionary asking user for input.
def search_value(category_dict, value):
    if value in category_dict:  # Check if the value is in the dictionary
        return f"{value}'s year is {category_dict[value]}."  # Return the value's year
    else:
        return f"Sorry, {value} was not found in the dictionary."  # Return an error message


def play():
    # Main interactive loop for category selection
    while True:
        # Ask user to choose a category: actors, movies, games, or exit
        category_type = input("Choose the category (actors, movies, games, exit): ").strip().lower()

        if category_type == 'exit':  # If user types 'exit', end the loop and exit the program
            print("Thanks for playing! :) ")  # Display a thank you message
            break  # Exit the loop and end the program

        elif category_type == 'actors':  # If user selects 'actors', set category_dict to actors_dict
            category_dict = actors_dict  # Assign the dictionary for actors

        elif category_type == 'movies':  # If user selects 'movies', set category_dict to movies_dict
            category_dict = movies_dict  # Assign the dictionary for movies

        elif category_type == 'games':  # If user selects 'games', set category_dict to games_dict
            category_dict = games_dict  # Assign the dictionary for games

        else:  # If input does not match any valid options, print an error message
            print("INPUT IS NOT RECOGNIZED!!!.")  # Display invalid input message
            continue  # Restart the loop and prompt for input again

        # Second interactive loop for actions within the selected category
        while True:
            action = input("Choose an action (add, delete, sort, search, back): ").strip().lower()

            if action == 'back':  # If user types 'back', break the action loop and return to category selection
                print("Returning to category selection.")  # Inform the user they are returning to category selection
                break  # Exit the action loop and return to the main category loop
            elif action == 'add':
                name = input("Enter the name: ")
                year = input("Enter the year (YYYY): ")
                add_value(category_dict, name, year)  # Use category_dict to add the value

            elif action == 'delete':
                name = input("Enter the name to delete: ")
                delete_value(category_dict, name)  # Use category_dict to delete the value

            elif action == 'sort':
                order = input("Sort order (asc/desc): ").strip().lower()
                if order in ['asc', 'desc']:  # Check if the order input is valid
                    sorted_values = sort_values(category_dict, order)  # Use category_dict to sort the values
                    print("Sorted values:", sorted_values)  # Display sorted values
                else:
                    print("Invalid sort order. Please enter 'asc' or 'desc'.")  # Error message for invalid input

            elif action == 'search':
                name = input("Enter the name to search: ")
                search_value(category_dict, name)  # Use category_dict to search for the value

            else:
                print("Action not recognized.")  # Display invalid action message

if __name__ == '__main__':
    play()
