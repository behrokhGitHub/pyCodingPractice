#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 13:51:23 2021

@author: behrokh
"""
'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

'''
def searchMatrix(matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        i = 0 
        j = len(matrix[0]) - 1
        
        while i < len(matrix) and j >= 0:
            
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False
                
def main():
  
    nums1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    print(searchMatrix(nums1, 3))
    
    nums2 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    print(searchMatrix(nums2, 13))
    

if __name__ == '__main__': main()