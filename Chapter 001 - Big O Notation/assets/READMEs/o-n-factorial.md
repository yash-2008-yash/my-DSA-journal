# O(n!) - Factorial Time

**_Factorial time complexity means that the running time of an algorithm grows factorially with the size of the input._**

This is even worse. This is often seen in algorithms that generate all permutations of a set of data.

```python
def permute(arr, l, r):
    if l == r:
        print(" ".join(map(str, arr)))
        return

    for i in range(l, r + 1):
        arr[l], arr[i] = arr[i], arr[l]
        permute(arr, l + 1, r)
        arr[l], arr[i] = arr[i], arr[l]
```

For `n` elements, there are total `n!` orderings, and this generates every single one. If `n=10`, that's 36,28,800 permutations. If `n=15`, that's over a trillion permutations!

Both **O(2ⁿ)** and **O(n!)** are "Your algorithm sucks!" area. So, it's best if we avoid these.
