def majority_element(nums):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num

        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate


numbers = [2, 2, 1, 2, 3, 2, 2]
print("Majority element:", majority_element(numbers))
