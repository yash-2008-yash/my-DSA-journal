# Check if a string is palindrome or not using recursion

Given an string, check whether it is a palindrome or not without using loops, slicing, or built-in reverse functions.
```
Input: "madam"
Output: True
Explanation: Reverse of "madam" is "madam"
```
```
Input: "hello"
Output: False
Explanation: Reverse of "hello" is "olleh"
```

---

### MY SOLUTION

```python
def palindrome_check(the_string, start, end):
    if start >= end:
        return True

    if the_string[start] != the_string[end]:
        return False

    return palindrome_check(the_string, start + 1, end - 1)


demo = "madam"
print(palindrome_check(demo, 0, len(demo) - 1))
```

My approach is similar to the previous "reverse an array" problem. I'm using the same two-pointer technique. But in this, I'm not actually building something, I'm just comparing.

`palindrome_check()` takes `the_string`, `start`, and `end` as arguments. At each recursive call, `the_string[start]` is compared with `the_string[end]`. If they don't match, `False` is returned immediately. Otherwise, the function calls itself with `start + 1` and `end - 1`, shrinking the window inward. This goes on until the base condition is satisfied.

- `palindrome_check("madam", 0, 4)` ➜ `m == m`, call `palindrome_check("madam", 1, 3)`
- `palindrome_check("madam", 1, 3)` ➜ `a == a`, call `palindrome_check("madam", 2, 2)`
- `palindrome_check("madam", 2, 2)` ➜ Base case reached. Returns `True`

**NOTE:** Time complexity will be O(N) because the function is called N/2 times (one comparison per call), which simplifies to O(N).