"""
# 242. Valid Anagram 

# Tags: Hash Table, Sort
# Difficulty: Easy

Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)


class Solution2(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        dict = collections.defaultdict(int)
        for key_index in xrange(len(s)):
            dict[s[key_index]] += 1
            dict[t[key_index]] -= 1
        return all(value == 0 for value in dict.values())