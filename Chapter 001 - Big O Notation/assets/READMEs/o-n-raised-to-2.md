# O(n²) - Quadratic Time

This kind of operation have nested loops for the same input.

```cpp
vector<vector<int>> add_matrices(vector<vector<int>>& matrix_A, vector<vector<int>>& matrix_B) {
  int n = matrix_A.size();
  int m = matrix_A[0].size();
  vector<vector<int>> result(n, vector<int>(m));

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      result[i][j] = matrix_A[i][j] + matrix_B[i][j];
    }
  }

  return result;
}
```

The outer loop runs `n` times, and for each of those, inner loop also `n` times. So, total operations is `n × n = n²` times.

That means if n=10, then it's 100 operations, and if n=1000, then it's 10,00,000 operations. It becomes slow with growing input size. That's why nested loops are a big red flag for optimizing code.

**Bubble Sort** is also a **O(n²)** operation, which acts as another example.