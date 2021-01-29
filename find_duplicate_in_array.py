#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 22:29:27 2021

@author: behrokh
"""
'''
Given an array of integers nums containing n + 1 integers where each integer 
is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.
'''
'''in O(1) space'''
def findDuplicate(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # s = set()
        # for i in nums:
        #     if i in s:
        #         return i
        #     else:
        #         s.add(i)
        slow = nums[0]
        fast = nums[nums[0]]
        
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        print()
        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
    
    
def main():
    nums1 = [1,3,4,2,2]
    print(findDuplicate(nums1))
    
    nums2 = [1,1,2]
    print(findDuplicate(nums2))

if __name__ == '__main__': main()