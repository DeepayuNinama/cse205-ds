# def subsets(nums):
#     #Creating a Class to create a loop for recursion

#     #we have two variables which will point to the i^th and our subset
#     def backtrack(start , curr_subset):  
        
#         result.append(curr_subset[:])

#         for i in range(start, len(nums)):

#             curr_subset.append(nums[i])
#             backtrack(i + 1, curr_subset)
#             curr_subset.pop()

#     result = []
#     backtrack(0 , [])
#     return result        

# nums = [1 ,2 ,3]
# result = subsets(nums)
# print(result)


def subsets(nums):
    def backtrack(start, curr_subsets):

        result.append(curr_subsets[:])

        for i in range(start, len(nums)):
            curr_subsets.append(nums[i])
            backtrack(i + 1,curr_subsets)
            curr_subsets.pop()

    result= []
    backtrack(0,[])
    print(result)        