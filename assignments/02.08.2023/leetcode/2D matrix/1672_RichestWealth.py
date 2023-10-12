class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        higest_sum = 0

        for account in accounts:
            current_sum = sum(account)
            
            if higest_sum < current_sum:
                higest_sum = current_sum

        return higest_sum        
        