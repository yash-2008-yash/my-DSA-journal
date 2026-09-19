# Print N to 1 using Recursion

Given an integer N, write a program to print numbers from N to 1.

```
Input: N = 4
Output: 4, 3, 2, 1
Explanation: All the numbers from 4 to 1 are printed.
```
```
Input: N = 1
Output: 1 
Explanation: This is the base case.
```

---

### MY SOLUTION

```python
def print_numbers(N):
    if N == 0:
        return

    print(N, end=" ")

    print_numbers(N - 1)


print_numbers(4)
```

The recursive function `print_numbers` takes `N` as an argument. At each recursive call, the current value of `N` is printed and then decreased by 1.

This goes on until the base condition `N == 0` becomes true. In this case:
- `print_numbers(4)` ➜ 4 == 0 is **false** ➜ 4 is printed
- `print_numbers(3)` ➜ 3 == 0 is **false** ➜ 3 is printed
- `print_numbers(2)` ➜ 2 == 0 is **false** ➜ 2 is printed
- `print_numbers(1)` ➜ 1 == 0 is **false** ➜ 1 is printed
- `print_numbers(0)` ➜ 0 == 0 is **true**. Base case has been reached, so recursion stops

**NOTE:** Time complexity will be O(N) because we print the every number from N to 1.