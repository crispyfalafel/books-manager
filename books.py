"""
Book collection manager.
COMP 1510 Assignment 2
Jolin Lin A01080811
"""

import doctest
from typing import Optional


def BOOK_KEYS():
    """
    Return a list of keys used to create a book dictionary.
    """
    return ["author", "title", "publisher", "shelf", "category", "subject"]


def search_book(book_tuple: tuple) -> Optional[list]:
    """
    Search for books by author, title, publisher, shelf, category, or subject.

    :param book_tuple: A non-empty tuple of dictionaries containing book information.
    :precondition: book_tuple must be a list of dictionaries containing book information.
    :precondition: Each dictionary must have an author, title, publisher, shelf, category, and subject key.
    :postcondition: Finds and prints a list of book dictionaries that match the desired search input.
    :return: A list of book dictionaries that match the search query, or None if the user does not search correctly.
    """
    search_category = get_search_category()
    if not search_category:
        return None

    search_text = get_search_input()
    if not search_text:
        return None

    # Search for books by exact shelf number
    if search_category == "shelf" and search_text.isnumeric():
        matching_books = [book for book in book_tuple if search_text == book[search_category]]

    else:
        matching_books = [book for book in book_tuple if search_text in book[search_category].lower()]

    print_search_results(matching_books, search_category, search_text)
    return matching_books


def get_search_input() -> str:
    """
    Get search input from the user.

    :postcondition: Asks the user to input a string of search input.
    :return: The string the user entered as search input.
    """
    search_input = input("What would you like to search for: ").strip().lower()

    if search_input == "":
        print("Enter a search input.")

    return search_input


def get_search_category() -> Optional[str]:
    """
    Get a book search category from the user.

    Search categories are author, title, publisher, shelf, category, or subject.

    :postcondition: Prompts the user to select a category to search books by.
    :return: A string for the category the user selected, or None if the user did not select a category.
    """
    print("How would you like to search for the book?")
    for number, category in enumerate(BOOK_KEYS(), 1):
        print(f"{number}. {category.title()}")

    category_input = get_number_choice(len(BOOK_KEYS()))

    if category_input:
        return BOOK_KEYS()[category_input - 1]
    else:
        return None


def get_number_choice(number_of_options: int) -> Optional[int]:
    """
    Ask the user to pick a number between 1 and the given number.

    :param number_of_options: A positive integer.
    :precondition: number_of_options must be positive.
    :postcondition: Asks the user for a number between 1 and the number of choices.
    :return: An integer representing the number the user chose, or None if the user entered an invalid choice.
    """
    choice = input(f"Enter a number from 1-{number_of_options}: ").strip()

    try:
        choice = int(choice)
    except ValueError:
        print("Please enter a number.")
        return

    if choice in range(1, number_of_options + 1):
        return choice
    else:
        print("Number out of range.")
        return


def print_search_results(search_results: list, category: str, search_input: str):
    """
    Print a list of book search results.

    :param search_results: A list of book dictionaries, or an empty list.
    :param category: A non-empty string.
    :param search_input: A non-empty string.
    :precondition: Category must be author, title, publisher, shelf, category, or subject.
    :precondition: Each dictionary must have an author, title, publisher, shelf, category, and subject key.
    :postcondition: Prints the number of results, then a numbered list with each book's information.

    >>> book_1 = {'author': 'Dupre', 'title': 'Skyscrapers', 'publisher': 'BD&L', 'shelf': '12', \
    'category': 'Architecture', 'subject': '20th Century'}
    >>> book_2 = {'author': 'Eddings', 'title': 'Belgarath the Sorcerer', 'publisher': 'None', 'shelf': '34', \
    'category': 'Fiction', 'subject': 'Fantasy'}
    >>> my_books = [book_1, book_2]
    >>> print_search_results(my_books, "author", "a")
    Found 2 books with a(n) author containing "a":
    1. Author: Dupre, Title: Skyscrapers, Publisher: BD&L, Shelf: 12, Category: Architecture, Subject: 20th Century
    2. Author: Eddings, Title: Belgarath the Sorcerer, Publisher: None, Shelf: 34, Category: Fiction, Subject: Fantasy
    >>> my_books = []
    >>> print_search_results(my_books, "title", "harry potter")
    Found 0 books with a(n) title containing "harry potter".
    """
    if search_results:
        if category == "shelf" and search_input.isnumeric():
            print(f"Found {len(search_results)} books on shelf {search_input}:")
        else:
            print(f"Found {len(search_results)} books with a(n) {category} containing \"{search_input}\":")

        for number, book in enumerate(search_results, 1):
            result_line = ", ".join(["{0}: {1}".format(key.title(), value) for key, value in book.items()])
            print(f"{number}. {result_line}")

    else:
        print(f"Found 0 books with a(n) {category} containing \"{search_input}\".")


def choose_book(book_list: list) -> Optional[dict]:
    """
    Ask the user to choose a book from the given tuple of books.

    :param book_list: A non-empty list of dictionaries containing book information.
    :precondition: Each dictionary must have an author, title, publisher, shelf, category, and subject key.
    :postcondition: Prints a list of the books and asks the user to choose one of the books.
    :return: An dictionary corresponding to the chosen book, or None if the user did not choose a book.
    """
    print("Choose a book to move.", end=" ")

    book_choice = get_number_choice(len(book_list))

    if book_choice:
        return book_list[book_choice - 1]
    else:
        return


def move_book(book_tuple: tuple):
    """
    Move a book from one shelf to another.

    :param book_tuple: A tuple of book dictionaries.
    :precondition: book_tuple must be a list of dictionaries containing book information.
    :precondition: Each dictionary must have an author, title, publisher, shelf, category, and subject key.
    :postcondition: Changes a book dictionary's shelf value to the destination shelf chosen by the user.
    """
    possible_locations = find_valid_shelves(book_tuple)
    matching_books = search_book(book_tuple)

    if matching_books is None:
        return

    if matching_books:
        book_to_move = choose_book(matching_books)
        if not book_to_move:
            return

        current_location = book_to_move["shelf"]
        destination = get_destination_shelf(possible_locations, current_location)
        if not destination:
            return

        change_book_shelf(book_to_move, destination)
    else:
        print("Could not find a book to move. :(")


def find_valid_shelves(book_tuple: tuple) -> list:
    """
    Create a list of valid shelf locations based on the given tuple of books.

    :param book_tuple: A tuple of book dictionaries.
    :precondition: Each book dictionary must have keys for author, title, publisher, shelf, category, and subject.
    :postcondition: Creates a list of sorted numerical shelve strings, and a list of alphabetical shelve strings.
    :return: A sorted list containing strings of shelf locations.

    >>> book_1 = {'author': 'Dupre', 'title': 'Skyscrapers', 'publisher': 'BD&L', 'shelf': '15', \
    'category': 'Architecture', 'subject': '20th Century'}
    >>> book_2 = {'author': 'Dupre', 'title': 'Skyscrapers', 'publisher': 'BD&L', 'shelf': 'Island', \
    'category': 'Architecture', 'subject': '20th Century'}
    >>> book_3 = {'author': 'Dupre', 'title': 'Skyscrapers', 'publisher': 'BD&L', 'shelf': '8', \
    'category': 'Architecture', 'subject': '20th Century'}
    >>> book_4 = {'author': 'Dupre', 'title': 'Skyscrapers', 'publisher': 'BD&L', 'shelf': '15', \
    'category': 'Architecture', 'subject': '20th Century'}
    >>> my_books = (book_1, book_2, book_3, book_4)
    >>> find_valid_shelves(my_books)
    ['8', '15', 'Island']
    """
    shelves = {book["shelf"] for book in book_tuple}
    shelves_list = list(shelves)

    number_shelves = [shelf for shelf in shelves_list if shelf.isnumeric()]
    word_shelves = [shelf for shelf in shelves_list if shelf.isalpha()]

    return sorted(number_shelves, key=int) + sorted(word_shelves)


def get_destination_shelf(valid_locations: list, current_location: str) -> Optional[str]:
    """
    Get a destination shelf from the user based on the valid location options.

    :param valid_locations: A list of book shelf strings.
    :param current_location: A string for the book's current location.
    :precondition: valid_locations must be a list of strings representing book locations.
    :precondition: current_location must be in valid_locations.
    :postcondition: Asks the user for a destination shelf location from the given set, excluding the current location.
    :return: A string representing the shelf the user chose, or None if the user entered an invalid location.
    """
    print("Select a destination shelf:")
    for number, shelf in enumerate(valid_locations, 1):
        print(f"{number}. {shelf}")
    print(f"The book is currently located at shelf {current_location}.")

    shelf_choice = get_number_choice(len(valid_locations))
    if shelf_choice:
        destination = valid_locations[shelf_choice - 1]
    else:
        return

    if check_if_different_location(current_location, destination):
        return destination
    else:
        return


def check_if_different_location(current_location: str, destination_location: str) -> bool:
    """
    Return True if the book locations are different, otherwise returns False and prints an error message.

    :param current_location: A string.
    :param destination_location: A string.
    :precondition: Both arguments must be strings.
    :postcondition: Checks if the strings are different, and prints an error message if they are the same.
    :return: True if the locations differ, False otherwise
    """
    if destination_location.lower() != current_location.lower():
        return True
    else:
        print(f"The book is already located at shelf {destination_location}.")
        return False


def change_book_shelf(book_dictionary: dict, destination: str):
    """
    Move a book to the destination shelf.

    :param book_dictionary: A dictionary with book information.
    :param destination: A string.
    :precondition: The dictionary must have an author, title, publisher, shelf, category, and subject key.
    :postcondition: Changes the book's shelf value and prints a confirmation message.

    >>> book = {'author': 'Dupre', 'title': 'Skyscrapers', 'publisher': 'BD&L', 'shelf': '12', \
     'category': 'Architecture', 'subject': '20th Century'}
    >>> shelf = 'kitchen'
    >>> change_book_shelf(book, shelf)
    "Skyscrapers" was successfully moved to shelf kitchen.
    >>> new_book = {'author': 'Dupre', 'title': 'Skyscrapers', 'publisher': 'BD&L', 'shelf': 'kitchen', \
    'category': 'Architecture', 'subject': '20th Century'}
    >>> book == new_book
    True
    """
    book_dictionary["shelf"] = destination
    print(f"\"{book_dictionary['title']}\" was successfully moved to shelf {destination}.")


def load_books(file_name: str) -> tuple:
    """
    Create a tuple of dictionaries containing book information.

    Each dictionary contains information for a book's author, title, publisher, shelf, category, and subject.

    :param file_name: A file name string.
    :precondition: file_name must be a string for a .txt file.
    :postcondition: Creates a tuple of dictionaries containing the provided book information.
    :return: A tuple of dictionaries with book information.

    >>> load_books("doctest_load.txt") # doctest: +NORMALIZE_WHITESPACE
    ({'author': 'Dupre', 'title': 'Skyscrapers', 'publisher': 'BD&L', 'shelf': '12', 'category': 'Architecture',
    'subject': '20th Century'}, {'author': 'Hollingsworth', 'title': 'Architecture of the 20th Century',
    'publisher': 'Exeter', 'shelf': '6', 'category': 'Architecture', 'subject': '20th Century'},
    {'author': 'Johnson Burgee', 'title': 'Architecture 1979-1985', 'publisher': 'Rizzoli', 'shelf': '6',
    'category': 'Architecture', 'subject': '20th Century'})
    """
    book_collection = []

    with open(file_name, encoding="UTF-16") as file_object:
        next(file_object)
        for line in file_object:
            book_collection.append(convert_text_line_to_dict(line, BOOK_KEYS()))

    book_collection = tuple(book_collection)
    return book_collection


def convert_text_line_to_dict(text_line: str, keys: list) -> dict:
    """
    Create a dictionary from the given string of values and list of keys.

    Empty string values are replaced with "None".

    :param text_line: A string of values from a txt file.
    :param keys: A list of keys for the dictionary.
    :postcondition: Create a dictionary with the given keys and values.
    :return: A dictionary.

    >>> book = "Dupre\\tSkyscrapers\\tBD&L\\t12\\tArchitecture\\t20th Century"
    >>> convert_text_line_to_dict(book, BOOK_KEYS()) # doctest: +NORMALIZE_WHITESPACE
    {'author': 'Dupre', 'title': 'Skyscrapers', 'publisher': 'BD&L', 'shelf': '12', 'category': 'Architecture',
     'subject': '20th Century'}
    >>> book = "Eddings\\tBelgarath the Sorcerer\\t\\t34\\tFiction\\tFantasy"
    >>> convert_text_line_to_dict(book, BOOK_KEYS()) # doctest: +NORMALIZE_WHITESPACE
    {'author': 'Eddings', 'title': 'Belgarath the Sorcerer', 'publisher': 'None', 'shelf': '34', 'category': 'Fiction',
     'subject': 'Fantasy'}
    """
    values = text_line.strip("\n").split("\t")
    while "" in values:
        values[values.index("")] = "None"
    book_dictionary = dict(zip(keys, values))
    return book_dictionary


def export_books(book_tuple: tuple, file: str):
    """
    Write book information to a plaintext file.

    :param book_tuple: A tuple of dictionaries containing book information.
    :param file: A file name string
    :precondition: Dictionaries must have keys for author, title, publisher, shelf, category, subject.
    :precondition: file must be a string for a .txt file.
    :postcondition: Creates a text file with each book's information printed on a new row.
    """

    with open(file, "w", encoding="UTF-16") as file_object:
        headers = "\t".join(BOOK_KEYS())
        file_object.write(headers.title())
        file_object.write("\n")

        for book in book_tuple:
            file_object.write(convert_dict_to_text_line(book, BOOK_KEYS()))
            file_object.write("\n")

    print(f"Book collection saved to {file}.")


def convert_dict_to_text_line(dictionary: dict, keys: list) -> str:
    """
    Write a line of values from the given dictionary.

    :param dictionary: A dictionary.
    :param keys: A list of keys for the given dictionary.
    :precondition: Every item in the list must be a valid key in the given dictionary.
    :postcondition: Writes a string of book information with all of the dictionary's values.
    :return: A string of the book's dictionaries values

    >>> book = {'author': 'Dupre', 'title': 'Skyscrapers', 'publisher': 'BD&L', 'shelf': '12', \
    'category': 'Architecture', 'subject': '20th Century'}
    >>> test_keys = ["author", "title", "publisher", "shelf", "category", "subject"]
    >>> convert_dict_to_text_line(book, test_keys)
    'Dupre\\tSkyscrapers\\tBD&L\\t12\\tArchitecture\\t20th Century'
    """
    values = [dictionary[key] for key in keys]
    while "None" in values:
        values[values.index("None")] = ""

    line = "\t".join(values)
    return line


def menu(book_collection):
    """
    Loop through the menu system to search for and move books in the book collection until the user quits.

    :param book_collection: A tuple of book dictionaries.
    :precondition: Each dictionary must have an author, title, publisher, shelf, category, and subject key.
    :postcondition: Continuously loops through the book collection menu until the user quits.
    """
    user_input = ""
    while user_input != "quit":
        user_input = get_menu_input()

        if user_input == "search":
            search_book(book_collection)
        elif user_input == "move":
            move_book(book_collection)


def get_menu_input() -> str:
    """
    Allow the user to choose to search for a book, move a book, or quit the program.

    :postcondition: Lets the user choose between search, move, or quit.
    :return: A string for the user's response.
    """
    menu_options = ("search", "move", "quit")

    print("What would you like to do with the book collection?")
    for number, option in enumerate(menu_options, 1):
        print(f"{number}. {option.title()}")

    menu_choice = None
    while not menu_choice:
        menu_choice = get_number_choice(len(menu_options))

    return menu_options[int(menu_choice) - 1]


def books(file_name: str):
    """
    Allow the user to continuously search or move books in a given txt file.

    :param file_name: A string.
    :precondition: file_name must be the name of a text file.
    :postcondition: Imports the book data from the file, lets the user search or move books,
                    then overwrites the file with the new book collection data.
    """
    try:
        book_collection = load_books(file_name)

    except FileNotFoundError:
        print("File not found.")

    else:
        menu(book_collection)
        export_books(book_collection, file_name)


def main():
    """
    Drives the program.
    """
    doctest.testmod()
    file = "books.txt"
    books(file)


if __name__ == "__main__":
    main()
