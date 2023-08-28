class Solution:
    def reverseString(self, s: List[str]) -> None:
        def backtrack(left, right):
            if left < right:
                s[left] , s[right] = s[right] , s[left]
                backtrack(left + 1 , right - 1)
        backtrack( 0 , len(s) - 1)    