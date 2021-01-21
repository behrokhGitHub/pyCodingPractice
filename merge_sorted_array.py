#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

"""
Created on Thu Jan 21 08:37:56 2021

@author: behrokh
"""
"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

The number of elements initialized in nums1 and nums2 are m and n respectively. 
You may assume that nums1 has a size equal to m + n such that it has enough space 
to hold additional elements from nums2.

"""
import random

def merge(nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        
        while m > 0 and n > 0:
            
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1] 
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        
        if n > 0:
            nums1[:n] = nums2[:n]
       
        return nums1
            
            
def main():
    nums1 = []
    for i in range(0,5):
        n1 = random.randint(1,300)
        nums1.append(n1)
    nums1.sort()
    for i in range(5):
        nums1.append(0)
    print(nums1)
    
    nums2 = []
    for i in range(0,5):
        n2 = random.randint(1,300)
        nums2.append(n2)
    print(nums2)
    
    nums2.sort()
    #merge(nums1,5,nums2,7)
    res = merge(nums1,5,nums2,5)
    print(res)


if __name__ == "__main__": main()