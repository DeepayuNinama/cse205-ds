from ast import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        # nums = [1, 2, 2, 2, 3, 3]
        def backtrack(start, curr_subset):

            result.append(curr_subset[:])

            for i in range(start, len(nums)):

                if( i > start and nums[i] == nums[i - 1]):
                    continue

                curr_subset.append(nums[i])
                backtrack(i + 1, curr_subset)
                curr_subset.pop()

        result = []
        backtrack(0 , []) 
        print(result)          
