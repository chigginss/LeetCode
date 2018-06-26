
""" Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice."""

        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i, j]

""" Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward."""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        num = str(x)
        
        for i in range(0, len(num)/2):
            if num[i] != num[len(num)-i-1]:
                return False
        
        return True
        

        
        