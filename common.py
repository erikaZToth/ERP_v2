""" Common module
implement commonly used functions here
"""

import random


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

    while True:
        generated = str(lower_case_letters_list[random.randint(0, (len(lower_case_letters_list)-1))] +
                        upper_case_letters_list[random.randint(0, (len(upper_case_letters_list)-1))] +
                        numbers_list[random.randint(0, (len(numbers_list)-1))] +
                        numbers_list[random.randint(0, (len(numbers_list)-1))] +
                        upper_case_letters_list[random.randint(0, (len(upper_case_letters_list)-1))] +
                        lower_case_letters_list[random.randint(0, (len(lower_case_letters_list)-1))] +
                        special_characters_list[random.randint(0, (len(special_characters_list)-1))] +
                        special_characters_list[random.randint(0, (len(special_characters_list)-1))])
        for i in table:
            if table[i][0] == generated:
                True
            else:
                False

    return generated


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
