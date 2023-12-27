
def pair_sum_sorted_array(numbers, target):
    """
    Problem:
    Given an array sorted in increasing order and a target number, 
    find the indices of the two values from the array that sum up to the given target number.
    https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

    Complexity:
    * Time: O(n)
    * Space: O(1) 

    """
    n = len(numbers)
    j = n - 1
    i = 0

    while i < j:
        res = numbers[i] + numbers[j]
        if res == target:
            return [i, j]
        if res < target:
            i += 1
        else:
            j -= 1
    return [-1, -1]
