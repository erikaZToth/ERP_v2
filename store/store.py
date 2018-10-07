""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common
# main module
import main


def choose():
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    file_name = "store/games.csv"
    table = data_manager.get_table_from_file(file_name)
    if option == "1":
        show_table(table)
    elif option == "2":
        add(table)
    elif option == "3":
        id_ = ui.get_inputs(["ID"], "\nWhat is the ID of the item you want to remove?")
        remove(table, id_)
    elif option == "4":
        id_ = ui.get_inputs(["ID"], "\nWhat is the ID of the item you want to update?")
        update(table, id_)
    elif option == "0":
        main.main()
    else:
        raise KeyError("There is no such option.")


def handle_menu():
    options = ["show table",
               "add",
               "remove",
               "update"]

    ui.print_menu("\nStore manager", options, "back to the main menu")


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    while True:
        handle_menu()
        try:
            choose()
        except KeyError as err:
            ui.print_error_message(str(err))


def show_table(table):
    """
    Display a table
    Args:
        table (list): list of lists to be displayed.
    Returns:
        None
    """

    # your code
    title_list = ["ID", "Title", "Manufacturer", "Price (USD)", "Stock"]
    ui.print_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.
    Args:
        table (list): table to add new record to
    Returns:
        list: Table with a new record
    """

    # your code
    file_name = "store/games.csv"
    new_data_properties = ["Title", "Manufacturer", "Price (USD)", "Stock"]
    common.add_item(table, new_data_properties, file_name)

    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.
    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed
    Returns:
        list: Table without specified record.
    """

    # your code
    file_name = "store/games.csv"
    common.remove(table, id_, file_name)
    
    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.
    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update
    Returns:
        list: table with updated record
    """

    # your code
    file_name = "store/games.csv"
    new_data_properties = ["Title", "Manufacturer", "Price (USD)", "Stock"]
    common.update(table, id_, new_data_properties, file_name)

    return table
    

# special functions:
# ------------------

def get_counts_by_manufacturers(table):
    """
    Question: How many different kinds of game are available of each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
         dict: A dictionary with this structure: { [manufacturer] : [count] }
    """

    # your code


def get_average_by_manufacturer(table, manufacturer):
    """
    Question: What is the average amount of games in stock of a given manufacturer?

    Args:
        table (list): data table to work on
        manufacturer (str): Name of manufacturer

    Returns:
         number
    """

    # your code
