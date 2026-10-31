
# DSA 539: Find the Duplicate Number
# Floyd's Cycle Detection Algorithm

def find_duplicate(nums):
    if len(nums) < 2:
        raise ValueError("Array must contain at least two elements")

    # Phase 1: Find the meeting point
    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break

    # Phase 2: Find the entrance of the cycle
    slow = nums[0]

    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow


print(find_duplicate([1, 3, 4, 2, 2]))
print(find_duplicate([3, 1, 3, 4, 2]))
print(find_duplicate([1, 1])) 
