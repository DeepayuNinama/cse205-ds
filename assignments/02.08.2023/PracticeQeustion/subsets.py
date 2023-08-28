def subsets(nums):
    #Creating a Class to create a loop for recursion

    #we have two variables which will point to the i^th and our subset
    def backtrack(start , curr_subset):  
        
        result.append(curr_subset[:])

        for i in range(start, len(nums)):

            curr_subset.append(nums[i])
            backtrack(i + 1, curr_subset)
            curr_subset.pop()

    result = []
    backtrack(0 , [])
    return result        

nums = [1 ,2 ,3]
result = subsets(nums)
print(result)