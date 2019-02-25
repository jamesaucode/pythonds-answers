# Implement the binary search using recursion without the slice operator. Recall that you will need to pass the list along with the starting and ending index values for the sublist. Generate a random, ordered list of integers and do a benchmark analysis.

def binary_search_no_slice(search_list, left, right, target):
    # Note: Just pass left and right along with the function
    mid = (left + right) // 2
    if left >= right:
        return False