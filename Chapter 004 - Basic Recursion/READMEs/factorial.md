# Factorial of N numbers

Given a positive integer N, find its factorial — the product of all positive integers from 1 up to n.

```
Input: N=5
Output: 120
Explanation: 1x2x3x4x5 = 120
```
```
Input: N=3
Output: 6
Explanation: 1x2x3 = 6
```

---

### MY SOLUTION

```python
def find_factorial(N):
    if N == 0 or N == 1:
        return 1

    return N * find_factorial(N - 1)

print(find_factorial(5))
```

In the world of mathematics, factorial has a beautiful recursive structure. i.e. `n! = n * (n-1)!`. This is perfect for implementing recursion logic.

`find_factorial()` takes `N` as an argument. At each recursive call, the `n! = n * (n-1)!` is performed. This goes on until the base condition is satisified.

- `find_factorial(5)` ➜ return `5 * find_factorial(4)`
- `find_factorial(4)` ➜ return `4 * find_factorial(3)`
- `find_factorial(3)` ➜ return `3 * find_factorial(2)`
- `find_factorial(2)` ➜ return `2 * find_factorial(1)`
- `find_factorial(1)` ➜ Base case reached. Returns 1

Basically, this is how it looks:

5!  
5 * 4!  
5 * 4 * 3!  
5 * 4 * 3 * 2!  
5 * 4 * 3 * 2 * 1!  
5 * 4 * 3 * 2 * 1 = 120

**NOTE:** Time complexity will be O(N) because the function is called N times, with each call performing O(1) work.