# development driven by function names
import random
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

def create_a_list_of_random_numbers(number_of_numbers):
    """
    Generates a list of random integers within the range of 0 to 100.

    This function creates a list containing a specified number of random integers.
    Each integer in the list is within the range of 0 to 100 (inclusive). The input
    parameter specifies how many numbers should be generated and included in the
    list. The function ensures all values are non-negative and within the specified
    range.

    :param number_of_numbers: The number of random integers to generate.
    :type number_of_numbers: int
    :return: A list of random integers within the range of 0 to 100.
    :rtype: list[int]

    >>> random.seed(1)
    >>> create_a_list_of_random_numbers(5)
    [17, 72, 97, 8, 32]

    """

    return [random.randint(0, 100) for _ in range(number_of_numbers)]


def bubble_sort(list):
    """
    sort a list of numbers using bubble sort algorithm

    :param list:
    :return:

    >>> random.seed(1)
    >>> list = create_a_list_of_random_numbers(5)
    >>> bubble_sort(list)
    [8, 17, 32, 72, 97]

    """

    for i in range(len(list)):
        for j in range(len(list)-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

    return list


if __name__ == "__main__":
    import doctest
    doctest.testmod()
