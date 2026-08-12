# O(n log n) - Linearithmic Time

In this, if `n` loops are there, each loop does a `log n` operation.

**Most efficient sorting algorithms belong to this category.**

The Classic example: **Merge Sort**

```cpp
void merge(vector<int>& array, int left, int mid, int right) {
  vector<int> temp;
  int i = left, j = mid + 1;

  while (i <= mid && j <= right) {
    if (array[i] <= array[j]) { temp.push_back(array[i++]); }
    else { temp.push_back(array[j++]); }
  }

  while (i <= mid) { temp.push_back(array[i++]); }
  while (j <= right) { temp.push_back(array[j++]); }
  for (int k = left; k <= right; k++) { array[k] = temp[k - left]; }
}

void merge_sort(vector<int>& array, int left, int right) {
  if (left >= right) { return; }

  int mid = (left + right) / 2;

  merge_sort(array, left, mid);
  merge_sort(array, mid + 1, right);
  merge(array, left, mid, right);
}
```

Why it's O(n log n):

Here, the array keeps getting split in half, which is the `log n` part. At each level of splitting, merge step touches every element, which is the `n` part. So, `log n` levels x `n` work per level = **O(n log n)**.

Quick Sort, Heap Sort, etc. are also **O(n log n)** stuff.