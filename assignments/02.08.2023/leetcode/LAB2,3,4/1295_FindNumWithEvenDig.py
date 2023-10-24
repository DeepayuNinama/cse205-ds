from ast import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:

        count = 0
        for i in nums:

            ele = str(i)
            if len(ele) % 2 ==0:
                count  += 1

        return count   