class Solution(object):
    def twoSum(self, nums, target):
        #create hashmap
        prevMap = {}#value,index
        #traverse through given list
        for i,n in enumerate(nums):
            diff=target-n
            #finds if there is a number in the hashmap that sums to the target
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[n] = i
        return
