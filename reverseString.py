"""
# 344. Reverse String  

# Tags: Two pointers, String
# Difficulty: Easy

Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".

"""


class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # because string is immutable in python, so I need to create a new list
        s = list(s)
        for i in xrange(0, len(s)/2):
            s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]
        return "".join(s)