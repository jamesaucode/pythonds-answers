# 1. Set up a random experiment to test the difference between a sequential search and a binary search on a list of integers.

# Step1: Create a huge list of random integers in a list.
from random import randint
import time


def create_random_list(number_of_items):
    random_list = []
    for i in range(number_of_items):
        # Generate a random number from 0 - 100
        random_number = randint(1, number_of_items)
        random_list.append(random_number)
    return random_list

# Step2: Implement the binary search function, you can do it recursively or in loops
def binary_search_rec(search_list, target):
    midpoint = len(search_list) // 2  # Floor division of the length of the list
    if search_list == []:
        return False
    elif target == search_list[midpoint]:
        print('binary recur: Found!')
        return True
    elif target > search_list[midpoint]:
        return binary_search_rec(search_list[midpoint + 1:], target)
    elif target < search_list[midpoint]:
        return binary_search_rec(search_list[:midpoint], target)

# Using while loop
def binary_search(search_list, target):
    first = 0
    last = len(search_list)-1
    found = False
    while first <= last and not found:
        midpoint = (first + last)//2
        if search_list[midpoint] == target:
            print('binary search : Found!')
            found = True
        else:
            if target < search_list[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1

    return found

# A normal linear_search to test against binary search
def linear_search(search_list, target):
    for item in search_list:
        if item == target:
            print('Linear search : Found!')
            return True

    return False


def get_run_time(function, param_for_function, random_list):
    start_time = time.time()
    function(random_list, randint(1, param_for_function))
    return time.time() - start_time


def main():
    number_of_items = 1000000 # randomly picked number, put whatever you want here
    random_list = create_random_list(number_of_items)
    random_list.sort()
    binary_search_run_time = get_run_time(binary_search_rec, number_of_items, random_list)
    normal_binary_search_run_time = get_run_time(binary_search, number_of_items, random_list)
    linear_search_run_time = get_run_time(linear_search, number_of_items, random_list)
    print("The recursive binary search function ran {:.8f} seconds.".format(
        binary_search_run_time))
    print("The normal binary search function ran {:.8f} seconds.".format(normal_binary_search_run_time))
    print("The linear search function ran {:.8f} seconds".format(
        linear_search_run_time))


main()
