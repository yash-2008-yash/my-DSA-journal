# Print name N times using recursion

Given an integer N, write a program to print your name N times.

```
Input: N = 3
Output: Batman Batman Batman 
Explanation: Name is printed 3 times.
```
```
Input: N = 1
Output: Batman
Explanation: Name is printed once.
```

---

### MY SOLUTION

```python
def print_name(N, count):
    if count == N:
        return

    print("Batman", end=" ")

    print_name(N, count + 1)


print_name(3, 0)
```

The recursive function `print_name` takes `N` and a count variable as arguments. Here, the `count` variable is passed as an argument because defining it inside the function is of no use. At every call, it'll be reset. To make its state survive, we gotta pass it as an argument.

The base condition is `count == N`. The count is initially 0. At each call, the count increases. When the count becomes equal to N, recursion ends printing the name exactly N times.

**NOTE:** Time complexity will be O(N) because we print the name exactly N times.