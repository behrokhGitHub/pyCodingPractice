#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 14:37:31 2021

@author: behrokh
"""
"""
Group Anagrams
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.
"""

def groupAnagrams(strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        dict = {}
        for strn in strs:
            sList = sorted(strn)
            s = ''.join(sList)
            
            if s not in dict.keys():
                newList =[strn]
                dict[s] = newList
            else:
                dict[s].append(strn)
        res = dict.values()
        return res
    
def main():
    strs1 = ["eat","tea","tan","ate","nat","bat"]
    strs2 = [""]
    strs3 = ["a"]
    
    print("1st result is: ", groupAnagrams(strs1))
    print("2nd result is: ", groupAnagrams(strs2))
    print("3rd result is: ", groupAnagrams(strs3))
    
if __name__ == "__main__": main()