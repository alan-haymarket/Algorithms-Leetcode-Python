"""
# 70. Climbing Stairs

# Tags: Dynamic Programming
# Difficulty: Easy

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""


# first version, the space complexity can be improved!
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 1
        dict = [1, 1]
        for i in xrange(2, n + 1):
            dict.append(dict[i - 1] + dict[i - 2])
        return dict[-1]


 # second version, improved to constant space complexity
 class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 1
        dict = [1, 1]
        for i in xrange(2, n + 1):
            append_val = dict[0] + dict[1]
            dict[0] = dict[1]
            dict[1] = append_val
        return dict[-1]