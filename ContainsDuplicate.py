"""
# 217. Contains Duplicate

# Tags: Array, Hash Table
# Difficulty: Easy

Given an array of integers, find if the array contains any duplicates. 
Your function should return true if any value appears at least twice in the array, 
and it should return false if every element is distinct.

"""


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dict = {}
        for i in xrange(len(nums)):
            if nums[i] in dict:
                return True
            dict[nums[i]] = 0
        return False