# O(n log n) - Linearithmic Time

In this, if `n` loops are there, each loop does a `log n` operation.

**Most efficient sorting algorithms belong to this category.**

The Classic example: **Merge Sort**

```python
def merge(array, left, mid, right):
    temp = []
    i, j = left, mid + 1

    while i <= mid and j <= right:
        if array[i] <= array[j]:
            temp.append(array[i])
            i += 1
        else:
            temp.append(array[j])
            j += 1

    while i <= mid:
        temp.append(array[i])
        i += 1

    while j <= right:
        temp.append(array[j])
        j += 1

    for k in range(left, right + 1):
        array[k] = temp[k - left]


def merge_sort(array, left, right):
    if left >= right:
        return

    mid = (left + right) // 2

    merge_sort(array, left, mid)
    merge_sort(array, mid + 1, right)
    merge(array, left, mid, right)
```

Why it's O(n log n):

Here, the array keeps getting split in half, which is the `log n` part. At each level of splitting, merge step touches every element, which is the `n` part. So, `log n` levels x `n` work per level = **O(n log n)**.

Quick Sort, Heap Sort, etc. are also **O(n log n)** stuff.