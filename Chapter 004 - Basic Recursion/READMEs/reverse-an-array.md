# Reverse an array using recursion

Given an array, reverse the elements without using any loops or built-in reverse functions.

```
Input: [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]
Explanation: Reverse of [1, 2, 3, 4, 5] is [5, 4, 3, 2, 1]
```
```
Input: [1, 2]
Output: [2, 1]
Explanation: Reverse of [1, 2] is [2, 1]
```

---

### MY SOLUTION

```python
def reverse_array(arr, start, end):
    if start >= end:
        return arr

    # Swap those elements
    arr[start], arr[end] = arr[end], arr[start]

    return reverse_array(arr, start + 1, end - 1)


demo = [10, 20, 30, 40, 50, 60, 70]
print(reverse_array(demo, 0, len(demo) - 1))
```

My approach is to swap the outermost elements first, then shrinking the problem inward. `start` moves right, and `end` moves left. When they meet or cross, it means the array is sorted. BOOYAH!

`reverse_array()` takes `arr`, `start`, and `end` as arguments. At each recursive call, `arr[start]` and `arr[end]` are swapped, then the function calls itself with `start + 1` and `end - 1`. This goes on until the base condition `start >= end` is satisfied.

- `reverse_array(arr, 0, 6)` ➜ swap index 0 & 6, call `reverse_array(arr, 1, 5)`
- `reverse_array(arr, 1, 5)` ➜ swap index 1 & 5, call `reverse_array(arr, 2, 4)`
- `reverse_array(arr, 2, 4)` ➜ swap index 2 & 4, call `reverse_array(arr, 3, 3)`
- `reverse_array(arr, 3, 3)` ➜ Base case reached. Return the sorted `arr`

Basically, this is how it looks (using `[10, 20, 30, 40, 50, 60, 70]`):

[10, 20, 30, 40, 50, 60, 70]  
[70, 20, 30, 40, 50, 60, 10]  ← swapped 0 & 6  
[70, 60, 30, 40, 50, 20, 10]  ← swapped 1 & 5  
[70, 60, 50, 40, 30, 20, 10]  ← swapped 2 & 4  
[70, 60, 50, 40, 30, 20, 10]  ← start(3) >= end(3), STOP

**NOTE:** Time complexity will be O(N) because the function is called N/2 times (each call handles one swap), which simplifies to O(N).