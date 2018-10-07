""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
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
    file_name = "sales/sales.csv"
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
    elif option == "5":
        get_lowest_price_item_id(table)
    elif option == "6":
        # dates = ["Month from:", "Day from:", "Year from:"]
        month_from = int((ui.get_inputs(["Month from"], ""))[0])
        day_from = int((ui.get_inputs(["Day from:"], ""))[0])
        year_from = int((ui.get_inputs(["Year from:"], ""))[0])
        month_to = int((ui.get_inputs(["Month to"], ""))[0])
        day_to = int((ui.get_inputs(["Day to:"], ""))[0])
        year_to = int((ui.get_inputs(["Year to:"], ""))[0])
        get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to)
    elif option == "0":
        main.main()
    else:
        raise KeyError("There is no such option.")


def handle_menu():
    options = ["show table",
               "add",
               "remove",
               "update",
               "lowest price",
               "sold between"]

    ui.print_menu("\nSales manager", options, "back to the main menu")


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
    title_list = ["ID", "Title", "Price (USD)", "Month", "Day", "Year"]
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
    file_name = "sales/sales.csv"
    new_data_properties = ["Title", "Price (USD)", "Month", "Day", "Year"]
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
    file_name = "sales/sales.csv"
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
    file_name = "sales/sales.csv"
    new_data_properties = ["Title", "Price (USD)", "Month", "Day", "Year"]
    common.update(table, id_, new_data_properties, file_name)

    return table


# special functions:
# ------------------

def get_lowest_price_item_id(table):
    """
    Question: What is the id of the item that was sold for the lowest price?
    if there are more than one item at the lowest price, return the last item by alphabetical order of the title

    Args:
        table (list): data table to work on

    Returns:
         string: id
    """
    
    # your code
    lowest_price = table[0][2]
    prices = []
    titles = []
    id = []
    result = ""

    # calculate lowest price
    for i in range(len(table)):
        prices += [table[i][2]]
        if table[i][2] < lowest_price:
            lowest_price = str(table[i][2])

    # collect titles (and IDs) of the lowest price items 
    for i in range(len(prices)):
        if prices[i] == lowest_price:
            titles += [table[i][1].upper()]
            id += [table[i][0]]

    # search last item by alphabetical order of the title (amongst the lowest price items)
    last_titles = titles[0]
    result = id[0]
    for i in range(len(titles)):
        if titles[i] > last_titles:
            last_titles = titles[i]
            result = id[i]

    label = "ID of the item that was sold for the lowest price is"
    ui.print_result(result, label)

    return result


def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    """
    Question: Which items are sold between two given dates? (from_date < sale_date < to_date)

    Args:
        table (list): data table to work on
        month_from (int)
        day_from (int)
        year_from (int)
        month_to (int)
        day_to (int)
        year_to (int)

    Returns:
        list: list of lists (the filtered table)
    """

    # your code
    result = []
    # Year input error: from year > to year:
    if year_from > year_to:
        print("Invalid year input!")
    else:
        for i in range(len(table)):
            # same year:
            if year_from == int(table[i][5]) and year_to == int(table[i][5]):
                # same month:
                if month_from == int(table[i][3]) and day_from < int(table[i][4]) and month_to == int(table[i][3]) and day_to > int(table[i][4]):
                    result += [table[i]]
                # different months:
                if month_from < month_to:
                    if month_from == int(table[i][3]) and day_from < int(table[i][4]):
                        result += [table[i]]
                    if month_from < int(table[i][3]) and int(table[i][3]) < month_to:
                        result += [table[i]]
                    if int(table[i][3]) == month_to and int(table[i][4]) < day_to:
                        result += [table[i]]

            # different year:
            if year_from < year_to:
                # from year's different months:
                if int(table[i][5]) == year_from:
                    if month_from == int(table[i][3]) and day_from < int(table[i][4]):
                        result += [table[i]]
                    if month_from < int(table[i][3]):
                        result += [table[i]]
                # years between from year and to year:
                if year_from < int(table[i][5]) and int(table[i][5]) < year_to:
                    result += [table[i]]
                # to year's different months:
                if int(table[i][5]) == year_to:
                    if month_to == int(table[i][3]) and int(table[i][4]) < day_to:
                        result += [table[i]]
                    if int(table[i][3]) < month_to:
                        result += [table[i]]
        if result != []:
            show_table(result)
        else:
            print("There was no sale from %s-%s-%s to %s-%s-%s." %(month_from, day_from, year_from, month_to, day_to, year_to))
        
    label = "\nSold items between %s-%s-%s and %s-%s-%s are: \n" %(month_from, day_from, year_from, month_to, day_to, year_to)
    ui.print_result(result, label)
    
    return result
