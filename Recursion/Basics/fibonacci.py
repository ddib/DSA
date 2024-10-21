def find_fibonacci(n):
    """
    Problem:
    Given a number n, find the n-th Fibonacci Number.
    In mathematics, the Fibonacci numbers, commonly denoted Fn, form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
F(0) = 0, F(1) = 1 and F(n) = F(n − 1) + F(n − 2) for n > 1.
    https://leetcode.com/problems/fibonacci-number/
    
    Complexity:
    * Time: O(n)
    * Space: O(n)
    """
    def add_seq(i, b1, b2):
        if i == n:
            return b1
        return add_seq(i + 1, b2, b1 + b2)
    return add_seq(0, 0, 1)
