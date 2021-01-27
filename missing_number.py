#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 14:10:03 2021

@author: behrokh
"""
def missingNumber(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) + 1
        return int(n*(n-1)  / 2 - sum(nums))
    
def main():
  
    nums1 = [3,0,1]
    print(missingNumber(nums1))
    
    nums2 = [0]
    print(missingNumber(nums2))
    

if __name__ == '__main__': main()