
# DSA 542: Majority Element II
# Extended Boyer-Moore Voting Algorithm

def majority_element(nums):
    candidate1 = None
    candidate2 = None

    count1 = 0
    count2 = 0

    # Find two possible candidates
    for num in nums:

        if num == candidate1:
            count1 += 1

        elif num == candidate2:
            count2 += 1

        elif count1 == 0:
            candidate1 = num
            count1 = 1

        elif count2 == 0:
            candidate2 = num
            count2 = 1

        else:
            count1 -= 1
            count2 -= 1

    # Verify the candidates
    result = []

    for candidate in (candidate1, candidate2):
        if candidate is not None:
            if nums.count(candidate) > len(nums) // 3:
                if candidate not in result:
                    result.append(candidate)

    return result


print(majority_element([1, 2, 1, 1, 3, 2, 2]))
print(majority_element([1, 1, 1, 2, 3, 4]))
print(majority_element([1, 2, 3, 4]))
