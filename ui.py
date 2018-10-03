""" User Interface (UI) module """


def print_table(table, title_list):
    """
    Prints table with data.

    Example:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code

    number_of_rows = len(table)
    number_of_columns = len(table[0])

    # width of table and columns
    max_with_of_column_list = [len(title_list[element]) for element in range(len(title_list))]  # collect with of columns into a list
    width_of_table = 0  # with of table: integer

    for column in range(number_of_columns):
        for row in range(number_of_rows):
            width_of_column = len(table[row][column])
            if width_of_column > max_with_of_column_list[column]:
                max_with_of_column_list[column] = width_of_column
        width_of_table += max_with_of_column_list[column]

    # format and print title list
    width_for_formatting = width_of_table + number_of_columns * 3 - 1
    print("\n/" + "=" * (width_for_formatting) + "\\")
    title_formatted = "| "
    for column in range(number_of_columns):
        title_formatted += str(title_list[column] + " | ").rjust(max_with_of_column_list[column] + 3)
    print(title_formatted)
    print("\\" + "=" * (width_for_formatting) + "/")

    # format and print table
    for row in range(number_of_rows):
        row_of_table = table[row]
        row_formatted = "| "
        for column in range(number_of_columns):
            row_formatted += str(row_of_table[column] + " | ").rjust(max_with_of_column_list[column] + 3)
        print(row_formatted)
        print("|" + "–" * (width_for_formatting) + "|")


def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code
    print(title)
    number = 1
    for element in list_options:
        print("(%s) %s " % (number, element))
        number += 1
    print("(0) %s " % exit_message)


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """

    # your code
    list_labels = ["Please enter a number: "]
    title = "Please provide your personal information"
    inputs = input(list_labels)

    return inputs


def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code
    message = "There is no such option.\n"
    print(message)
