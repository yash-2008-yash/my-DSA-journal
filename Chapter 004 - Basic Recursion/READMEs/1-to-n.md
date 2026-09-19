# Print 1 to N using Recursion

Given an integer N, write a program to print numbers from 1 to N.

```
Input: N = 4
Output: 1, 2, 3, 4
Explanation: All the numbers from 1 to 4 are printed.
```
```
Input: N = 1
Output: 1 
Explanation: This is the base case.
```

---

### MY SOLUTION

```python
def print_numbers(N, count):
    if count > N:
        return

    print(count, end=" ")

    print_numbers(N, count + 1)


print_numbers(4, 1)
```

The recursive function `print_numbers` takes `N` and `count` as arguments. At each recursive call, current `count` is printed and the value is increased by 1.

This goes on until the base condition `count > N` becomes true. In this case:
- `print_numbers(4, 1)` ➜ 1 > 4 is **false** ➜ 1 is printed 
- `print_numbers(4, 2)` ➜ 2 > 4 is **false** ➜ 2 is printed
- `print_numbers(4, 3)` ➜ 3 > 4 is **false** ➜ 3 is printed
- `print_numbers(4, 4)` ➜ 4 > 4 is **false** ➜ 4 is printed
- `print_numbers(4, 5)` ➜ 5 > 4 is **true**. Base case has been reached, so recursion stops

**NOTE:** Time complexity will be O(N) because we print the every number from 1 to N.