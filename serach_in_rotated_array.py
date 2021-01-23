#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 15:36:31 2021

@author: behrokh
"""
'''
Search in Rotated Sorted Array
You are given an integer array nums sorted in ascending order (with distinct values), 
and an integer target.

Suppose that nums is rotated at some pivot unknown to you beforehand 
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

If target is found in the array return its index, otherwise, return -1.
'''

def search(nums, target):
        
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = (low+high) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[low] <= nums[mid] < target or \
                target < nums[low] <= nums[mid] or \
                nums[mid] < target < nums[low]:
                    low = mid + 1
            else:
                    high = mid - 1
        return -1
    
def main():
  
    nums1 = [4,5,6,7,0,1,2]
    print(search(nums1, 0))
    
    nums2 = [4,5,6,7,0,1,2]
    print(search(nums2, 3))
    
    nums3 = [1]
    print(search(nums3, 0))
    

if __name__ == '__main__': main()