def subsets(nums):
    def backtrack(start, current_subset):
        # Append the current subset to the result
        result.append(current_subset[:])
        
        # Generate subsets by including each element from start to the end
        for i in range(start, len(nums)):
            current_subset.append(nums[i])
            backtrack(i + 1, current_subset)  # Recurse with the next index
            current_subset.pop()  # Backtrack (remove the last element)

    result = []
    backtrack(0, [])  # Start with an empty subset at index 0
    return result

# Example usage:
nums = [1, 2, 3]
result = subsets(nums)
print(result)
   