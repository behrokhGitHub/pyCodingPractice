#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 16:23:27 2021

@author: behrokh
"""
'''
Search in a Sorted Array of Unknown Size

Given an integer array sorted in ascending order, write a function to search target in nums.  
If target exists, then return its index, otherwise return -1. However, 
the array size is unknown to you. You may only access the array using an ArrayReader interface, 
where ArrayReader.get(k) returns the element of the array at index k (0-indexed).

You may assume all integers in the array are less than 10000, and if you access the array out 
of bounds, ArrayReader.get will return 2147483647.

'''
class reader:
    def get(nums, index):
        if nums[index] != None:
            return nums[index]
        else :
            return 2147483647
    
    
def search(nums, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        '''no need to know the exact size of the array'''
        low = 0
        high = 1
        
        while reader.get(nums,high) < target:
            low = high
            high *= 2
            
        while low <= high:
            
            mid = (low+high) // 2
            
            if reader.get(nums,mid) == target:
                return mid
            elif reader.get(nums,mid) > target:
                high = mid - 1
            else:
                low = mid + 1
                
        return -1
    
def main():
  
    nums1 = [-1,0,3,5,9,12]
    print(search(nums1, 9))
    
    nums2 = [-1,0,3,5,9,12]
    print(search(nums2, 2))
    

if __name__ == '__main__': main()