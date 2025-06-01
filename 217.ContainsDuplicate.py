#Solution 1: Brute Force Approach
def containsDuplicate_brute_force(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:  # Found a duplicate
                return True
    return False  # No duplicates found
  #Solution 2: Optimized Using Hash Set
def containsDuplicate_hash_set(nums):
    seen = set()
    for num in nums:
        if num in seen:  # Duplicate found
            return True
        seen.add(num)
    return False  # All elements are unique

