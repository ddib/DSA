def kth_largest_in_an_array(numbers, k):
    """
    Problem:
    Given an array of integers, find the k-th largest number in it.
    https://leetcode.com/problems/kth-largest-element-in-an-array

    Complexity:
    * Time: O(nlog(n))
    * Space: O(1)
    """
    numbers.sort()
    return numbers[-k]
