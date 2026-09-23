# Fibonacci Number using Recursion

Given an integer N, return the Nth number in the Fibonacci sequence.

```
Input: 7
Output: 13
Explanation: 7th term of Fibonacci sequence is 13 (i.e. 0,1,1,2,3,5,8,13)
```
```
Input: 1
Output: 1
Explanation: 1st term of Fibonacci sequence is 1 (i.e. 0,1)
```

---

### MY SOLUTION

```python
def fibonacci(N):
    if N == 0:
        return 0

    if N == 1:
        return 1

    return fibonacci(N - 1) + fibonacci(N - 2)


print(fibonacci(7))
```
Nth term in Fibonacci can be computed easily. i.e. `fib(n) = fib(n-1) + fib(n-2)`. This is perfect for implementing recursion logic.

`fibonacci()` takes `N` as an argument. At each recursive call, the `fib(n) = fib(n-1) + fib(n-2)` is performed, branching into two smaller calls each time. This goes on until the base condition is satisfied.

**WARNING:** This is not like the straight recursion we saw this long. It's messed up this time. So, buckle up and give your full attention.

- `fibonacci(4)` starts  
Not a base case. It needs `fibonacci(3)` first. Calls it. Freezes. Waits.

- `fibonacci(3)` starts  
Not a base case. It needs `fibonacci(2)` first. Calls it. Freezes. Waits.

- `fibonacci(2)` starts  
Not a base case. It needs `fibonacci(1)` first. Calls it. Freezes. Waits.

- `fibonacci(1)`
Base case. Returns 1 immediately.

- Back to `fibonacci(2)`, it wakes up  
Got 1 for the left side. Still needs the right side `fibonacci(0)`. Calls it. Freezes again.

- `fibonacci(0)`  
Base case. Returns 0 immediately.

- Back to `fibonacci(2)`, it wakes up for the last time  
Has both pieces now: left = 1, right = 0. Adds 1 + 0 = 1. `fibonacci(2)` is done. Returns 1.

- Back to `fibonacci(3)`, it wakes up  
Got 1 for the left side. Still needs the right side `fibonacci(1)`. Calls it. Freezes again.

- `fibonacci(1)`  
Base case. Returns 1 immediately.

- Back to `fibonacci(3)`, it wakes up for the last time  
Has both pieces now: left = 1, right = 1. Adds: 1 + 1 = 2. `fibonacci(3)` is done. Returns 2.

- Back to `fibonacci(4)`, it wakes up  
Got 2 for the left side. Still needs the right side `fibonacci(2)`. Calls it. Freezes again.

- `fibonacci(2)` runs all over again.  
Completely fresh, repeats the same steps and ends up returning 1.

- Back to fibonacci(4), it wakes up for the last time  
Has both pieces: left = 2, right = 1. Adds: 2 + 1 = 3. `fibonacci(4)` is done. Returns 3.

**NOTE:** Time complexity will be **O(2^N)**, not O(N) unlike factorial's single chain, each call spawns *two* more calls, so the same subproblems (like `fibonacci(3)`) get recomputed many times over.