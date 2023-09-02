# Given two integers n and k, return all possible combinations of k numbers chosen 
# from the range [1, n]. You may return the answer in any order.

# Input: n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

from ast import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def backtrack(start, combinations):

            if len(combinations) == k:
                result.append(combinations[:])
                return result

            for i in range(start, n + 1):

                    combinations.append(i)
                    backtrack(i + 1, combinations)
                    combinations.pop()

        result = []
        backtrack(0,[])
        print(result)      