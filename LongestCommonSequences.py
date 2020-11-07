# -*- coding: utf-8 -*-
# Author: Weichen Liao

'''
leetcode No.1143

Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

If there is no common subsequence, return 0.

Example 1:

Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

------------------------------------------------------------------------------------------------------------------------------------------------
analysis:

the idea is to compare 2 strings from their tails, by keep deleting the last character

divide the problems into subproblems
LCS(str1, str2) = LCS(str1[:-1], str2[:-2])+1 if str1 and str2 ends with same char, otherwise max(LCS(str1[:-1], str2), LCS(str1, str2[:-1]))

and build a memoization structure to avoid recomputation. the lengths of strings can uniquely identify two strings
'''

def longestCommonSubsequence(text1: str, text2: str):
    lookup = {}
    def recursive(str1, str2):
        if (len(str1), len(str2)) in lookup.keys():
            return lookup[(len(str1), len(str2))]
        if len(str1) == 0 or len(str2) == 0:
            return 0
        if str1[-1] == str2[-1]:
            res = recursive(str1[:-1], str2[:-1]) + 1
            lookup[(len(str1), len(str2))] = res
            return res
        else:
            res = max(recursive(str1[:-1], str2), recursive(str1, str2[:-1]))
            lookup[(len(str1), len(str2))] = res
            return res
    return recursive(text1, text2)




if __name__ == '__main__':
    res = longestCommonSubsequence('abcde', 'ace')
    print(res)
