# -*- coding: utf-8 -*-
# Author: Weichen Liao
import numpy as np

# https://www.techiedelight.com/0-1-knapsack-problem/

# generally speaking when we are looking at such problem without dp technique, we would be interested in looking for the first item to consider, and we tend to sort it.
# why the order of checking doesn't matter? because here we are looking whether a item should be added in the sack or not, which is irrelevent with the order.

def knapsack0_1(v_list, w_list, W):
    def recursive(i, W):
        if W < 0:
            return -np.inf
        if W == 0 or i < 0:
            return 0
        else:
            return max(v_list[i] + recursive(i-1, W-w_list[i]), recursive(i-1, W))
    return recursive(len(v_list)-1, W)

if __name__ == '__main__':
    # v_list = [20, 5, 10, 40, 15, 25]
    # w_list = [1, 2, 3, 8, 7, 4]
    v_list = [5, 10, 15, 20, 25, 40]
    w_list = [2, 3, 7, 1, 4, 8]
    W = 10
    print(knapsack0_1(v_list, w_list, W))

