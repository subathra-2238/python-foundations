
def kth_element(arr1, arr2, k):
    # Always binary search on the smaller array
    if len(arr1) > len(arr2):
        return kth_element(arr2, arr1, k)

    n = len(arr1)
    m = len(arr2)

    low = max(0, k - m)
    high = min(k, n)

    while low <= high:
        cut1 = (low + high) // 2
        cut2 = k - cut1

        left1 = float("-inf") if cut1 == 0 else arr1[cut1 - 1]
        left2 = float("-inf") if cut2 == 0 else arr2[cut2 - 1]

        right1 = float("inf") if cut1 == n else arr1[cut1]
        right2 = float("inf") if cut2 == m else arr2[cut2]

        if left1 <= right2 and left2 <= right1:
            return max(left1, left2)

        elif left1 > right2:
            high = cut1 - 1

        else:
            low = cut1 + 1

    return -1


arr1 = [2, 3, 6, 7, 9]
arr2 = [1, 4, 8, 10]
k = 5

print("Kth smallest element:", kth_element(arr1, arr2, k))
