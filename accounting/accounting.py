""" Accounting module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * month (number): Month of the transaction
    * day (number): Day of the transaction
    * year (number): Year of the transaction
    * type (string): in = income, out = outflow
    * amount (int): amount of transaction in USD
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common
# main module (it is vorbidden)
import main


def choose():
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    file_name = "accounting/items.csv"
    table = data_manager.get_table_from_file(file_name)
    if option == "1":
        title_list = ["ID", "Month", "Day", "Year", "Type", "Amount"]
        ui.print_table(table, title_list)
    elif option == "2":
        new_items = ui.get_inputs(["Month", "Day", "Year", "Type", "Amount"], "\nPlease provide the following items:")
        common.add_item(table, new_items, file_name)
    elif option == "3":
        id_ = ui.get_inputs(["ID"], "\nWhat is the ID of the item you want to remove?")
        common.remove(table, id_, file_name)
    elif option == "4":
        id_ = ui.get_inputs(["ID"], "\nWhat is the ID of the item you want to update?")
        new_items = ui.get_inputs(new_data_properties, title)
        common.update(table, new_items, file_name, id_)
    elif option == "0":
        main.main()
    else:
        raise KeyError("There is no such option.")


def handle_menu():
    options = ["show table",
               "add",
               "remove",
               "update"]

    ui.print_menu("\nAccounting manager", options, "back to the main menu")


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    # your code
    while True:
        handle_menu()
        try:
            choose()
        except KeyError as err:
            ui.print_error_message(str(err))


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

    # return table


# special functions:
# ------------------

def which_year_max(table):
    """
    Question: Which year has the highest profit? (profit = in - out)

    Args:
        table (list): data table to work on

    Returns:
        number
    """

    # your code


def avg_amount(table, year):
    """
    Question: What is the average (per item) profit in a given year? [(profit)/(items count)]

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        number
    """

    # your code
