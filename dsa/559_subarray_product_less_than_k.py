
def num_subarray_product_less_than_k(nums, k):
    if k <= 1:
        return 0

    left = 0
    product = 1
    count = 0

    for right in range(len(nums)):
        product *= nums[right]

        while product >= k:
            product //= nums[left]
            left += 1

        count += right - left + 1

    return count


print(num_subarray_product_less_than_k([10, 5, 2, 6], 100))
print(num_subarray_product_less_than_k([1, 2, 3], 0))
print(num_subarray_product_less_than_k([1, 1, 1], 2))
print(num_subarray_product_less_than_k([2, 3, 4], 10))
```

### 3. Output

```text
8
0
6
4
```

### 4. Understand the logic

We use **Sliding Window + Product Tracking**.

Our rule:

- Expand the window by multiplying the next element.
- If the product becomes greater than or equal to `k`, shrink the window.
- Count all valid subarrays ending at the current position.

**Important condition:**

```python
while product >= k:
    product //= nums[left]
    left += 1
```

We shrink the window until its product becomes strictly less than `k`.

**Why this line?**

```python
count += right - left + 1
```

Suppose the current valid window is:

`[5, 2, 6]`

The valid subarrays ending at `6` are:

- `[6]`
- `[2, 6]`
- `[5, 2, 6]`

That's 3 subarrays!

### 5. Complexity

- **Time:** O(n)
- **Space:** O(1)

*Important: This sliding-window solution requires positive integers.*

### 6. Run and commit

```powershell
python dsa/559_subarray_product_less_than_k.py

git add dsa/559_subarray_product_less_than_k.py
git commit -m "Add subarray product less than k"
git push
```

<badge color="success">DSA 559 completed</badge>

Next: **DSA 560 – Find All Anagrams in a String (Optimized Sliding Window)** 🚀
