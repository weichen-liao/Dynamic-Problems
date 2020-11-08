# -*- coding: utf-8 -*-
# Author: Weichen Liao
import numpy as np

'''
https://www.techiedelight.com/longest-common-subsequence-finding-lcs/


'''

def findAllLCS(text1: str, text2: str):
    lookup = {}
    # build a matrix to track back the path. axis-x stands for each character of text2, axis-y stands for each character of text1
    path = [[0 for i in range(len(text2))] for j in range(len(text1))]
    def recursive(str1, str2):
        if (len(str1), len(str2)) in lookup.keys():
            return lookup[(len(str1), len(str2))]
        if len(str1) == 0 or len(str2) == 0:
            path[len(str1)][len(str2)] = 0
            return 0
        if str1[-1] == str2[-1]:
            res = recursive(str1[:-1], str2[:-1]) + 1
            lookup[(len(str1), len(str2))] = res
            path[len(str1)-1][len(str2)-1] = res
            return res
        else:
            res = max(recursive(str1[:-1], str2), recursive(str1, str2[:-1]))
            lookup[(len(str1), len(str2))] = res
            path[len(str1)-1][len(str2)-1] = res
            return res
    def recursiveTraceBack(path, x, y):
        if x < 0 or y < 0:
            return [""]
        if text1[x] == text2[y]:
            ans = recursiveTraceBack(path, x-1, y-1)
            for i in range(len(ans)):
                ans[i] += text1[x]
            return ans
        else:
            # move left
            if path[x][y-1] > path[x-1][y]:
                return recursiveTraceBack(path, x, y-1)
            # move top
            elif path[x][y-1] < path[x-1][y]:
                return recursiveTraceBack(path, x-1, y)
            # try both
            else:
                ans1 = recursiveTraceBack(path, x, y - 1)
                ans2 = recursiveTraceBack(path, x - 1, y)
                return ans1 + ans2


    # the number of LCS
    num_LCS = recursive(text1, text2)

    path = np.array(path)
    print(path, path.shape)

    # trace back the path. Start from the right bottom and end at the left top corner.  Move either left or top of diagonally
    # if the x and y are the same, add them to the answer, and move diagonally.
    # elif one of them is greater, then move towards that direction.
    # elif left and top is same value, try both direction to involve all possible LCS
    x, y = len(text1)-1, len(text2)-1
    LCS = recursiveTraceBack(path, x, y)

    return LCS


if __name__ == '__main__':
    res = findAllLCS('ABCBDAB', 'BDCABA')
    print(res)
