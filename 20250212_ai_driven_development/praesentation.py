import random

def generate_list_of_random_numbers(numbers):
    """
    Generates a list containing random integers within the range 0-200. The
    length of the generated list is determined by the input parameter.
    
    >>> random.seed(1)
    >>> generate_list_of_random_numbers(5)
    [17, 72, 97, 8, 32]
    
    :param numbers: The number of random integers to generate in the list.
    :type numbers: int
    :return: A list of random integers within the range 0-200.
    :rtype: list[int]
    """
    
    return [random.randint(0, 200) for _ in range(numbers)]


def bubble_sort(lst: list[int]) -> list[int]:
    """
    Sorts a list of numbers in ascending order using the bubble sort algorithm.

    The function iteratively compares adjacent elements in the list and swaps them
    if they are in the wrong order. This process is repeated until the entire list
    is sorted. This algorithm is simple but has a time complexity of O(n^2) in the
    worst case, making it inefficient for large datasets.
    >>> random.seed(1)
    >>> bubble_sort(generate_list_of_random_numbers(5))
    [16, 34, 65, 145, 195]

    :param lst: A list of numeric values to be sorted.
    :type lst: list of int
    :return: The sorted list of integers.
    """
    for i in range(len(lst)):
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst


def wordle_function(trial, target):
    """
    this function solves wordle. The trail should be compared letter by letter against the 
    target word. It should output which letters occur and which letters are at the correct position.
    
    return the answer as a pattern. Small letters occur and 
    capital letters occur at the correct position.
    >>> wordle_function("hello", "world")
    '  lLo'

    :param trial:
    :param target: 
    :return: 
    """
    result = []
    for t_char, target_char in zip(trial, target):
        if t_char == target_char:
            result.append(t_char.upper())
        elif t_char in target:
            result.append(t_char.lower())
        else:
            result.append(' ')
    return ''.join(result)


dictionary={'January':100,'February':200,'March':300,'April':400,'May':500,'June':600,'July':700,'August':800,'September':900,'October':1000,'November':1100,'December':1200}

for key, value in dictionary.items():
    print(key, value)

def total_values(dict):
    """
    """
    return sum(dict.values())

