# O(n²) - Quadratic Time

**_Quadratic time complexity means that the running time of an algorithm is proportional to the square of the input size._**

This kind of operation have nested loops for the same input.

```python
def add_matrices(matrix_A, matrix_B):
    n = len(matrix_A)
    m = len(matrix_A[0])
    result = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            result[i][j] = matrix_A[i][j] + matrix_B[i][j]

    return result
```

The outer loop runs `n` times, and for each of those, inner loop also `n` times. So, total operations is `n × n = n²` times.

That means if n=10, then it's 100 operations, and if n=1000, then it's 10,00,000 operations. It becomes slow with growing input size. That's why nested loops are a big red flag for optimizing code.

**Bubble Sort** is also a **O(n²)** operation, which acts as another example.
