""" Common module
implement commonly used functions here
"""

import random
import ui
import data_manager


def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """

    # your code
    special_characters_list = ['+', '!', '%', '/', '=', '-', '*', ',', '&', '@', 'ß', 'Ł', 'Đ', '~']
    numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    lower_case_letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                               'n', 'o', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    upper_case_letters_list = [x.upper() for x in lower_case_letters_list]
    # generated = ''
    # eH34Jd#&

    generated = str(lower_case_letters_list[random.randint(0, (len(lower_case_letters_list)-1))] +
                    upper_case_letters_list[random.randint(0, (len(upper_case_letters_list)-1))] +
                    numbers_list[random.randint(0, (len(numbers_list)-1))] +
                    numbers_list[random.randint(0, (len(numbers_list)-1))] +
                    upper_case_letters_list[random.randint(0, (len(upper_case_letters_list)-1))] +
                    lower_case_letters_list[random.randint(0, (len(lower_case_letters_list)-1))] +
                    special_characters_list[random.randint(0, (len(special_characters_list)-1))] +
                    special_characters_list[random.randint(0, (len(special_characters_list)-1))])

    check_generate_random(table, generated)
    return generated


def check_generate_random(table, generated):
    for i in range(len(table)):
        if generated == table[i][0]:
            generate_random(table)
        else:
            return generated


def start_module():
    pass


def add_item(table, new_items, file_name):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    # your code

    new_ID = [generate_random(table)]
    new_line_to_add = new_ID + new_items
    table += [new_line_to_add]
    data_manager.write_table_to_file(file_name, table)

    return table


def remove(table, id_, file_name):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    # your code

    for i in range(len(table)):
        if table[i][0] == id_[0]:
            del table[i]
            break
    data_manager.write_table_to_file(file_name, table)

    return table


def update(table, new_items, file_name, id_):

    new_line_elements = new_items
    new_line_elements.insert(0, id_[0])
    print(new_line_elements)
    for i in range(len(table)):
        if id_[0] == table[i][0]:
            table[i] = new_line_elements

    data_manager.write_table_to_file(file_name, table)
