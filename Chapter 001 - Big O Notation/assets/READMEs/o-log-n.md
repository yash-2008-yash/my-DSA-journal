# O(log n) - Logarithmic Time

Every times the input size doubles, the number of steps only increases by 1.

**This kind of operation becomes slow slowly with increasing input size.**

The most classic example is _Binary Search_.

```cpp
int binary_search(vector<int>& array, int target) {
  int low =0, high = array.size() - 1;

  while (low <= high) {
    int mid = (low + high) / 2;

    if (array[mid] == target) {
      return mid;
    }
    else if (array[mid] < target) {
      low = mid + 1;
    }
    else {
      high = mid - 1;
    }
  }

  return -1;
}
```

In every loop iteration, the search space is cut in half. So, for 10,000 elements, we don't have to do 10,000 checks, we just need about 13 steps since 2^13 is approx. 10,000.

This halving is _log n_ behavior. That's why binary search is a **O(log n)** operation.