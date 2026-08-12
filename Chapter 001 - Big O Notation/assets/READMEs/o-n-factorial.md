# O(n!) - Factorial Time

This is even worse. This happens when we are generating all permutations of something.

```cpp
void permute(vector<int>& arr, int l, int r) {
  if (l == r) {
    for (int x : arr) {
      std::cout << x << " ";
    }

    std::cout << endl;
    return;
  }

  for (int i = l; i <= r; i++) {
    swap(arr[l], arr[i]);
    permute(arr, l + 1, r);
    swap(arr[l], arr[i]);
  }
}
```

For `n` elements, there are total `n!` orderings, and this generates every single one. If `n=10`, that's 36,28,800 permutations. If `n=15`, that's over a trillion permutations!

Both **O(2ⁿ)** and **O(n!)** are "Your algorithm sucks!" area. So, it's best if we avoid these.