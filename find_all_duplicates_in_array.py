#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 22:36:30 2021

@author: behrokh
"""
'''
Find All Duplicates in an Array
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements 
appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?
'''
def findDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    res = []
    for x in nums:
        index = abs(x) - 1
        if nums[index] < 0:
            res.append(abs(x))
        else:
            nums[index] *= -1
    return res

def main():
    nums1 = [4,3,2,7,8,2,3,1]
    print(findDuplicates(nums1))
    
    nums2 = [10,2,5,10,9,1,1,4,3,7]
    print(findDuplicates(nums2))

if __name__ == '__main__': main()