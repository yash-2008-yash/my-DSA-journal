# Sum of First N Numbers

Given a number ‘N’, find out the sum of the first N natural numbers.

```
Input: N=5
Output: 15
Explanation: 1+2+3+4+5=15
```
```
Input: N=6
Output: 21
Explanation: 1+2+3+4+5+6=15
```

---

### MY SOLUTION

`BRUTE FORCE APPROACH`
```python
def sum_of_n(N):
    total = 0

    for i in range(1, N + 1):
        total += i

    return total


print(sum_of_n(5))
```

Most of the begineers would follow this approach. Iterate from 1 to N and keep adding each number to a total count.  
This solution is beginner-friendly, but it becomes less efficient with larger N as it requires looping through all numbers.

<br>

`FORMULA APPROACH`

Folks who have a good knowledge in mathematics know that we can find the sum of first N numbers using a formuala. i.e. N(N+1)/2.

```python
def sum_of_n(N):
    return (N * (N + 1)) // 2


print(sum_of_n(5))
```
This is a super-efficient solution because no looping is involved, just pure calculation.

**NOTE:** Time complexity is O(1).

<br>

`RECURSIVE APPROACH`

```python
def sum_of_n(N, total):
    if N == 0:
        return total

    return sum_of_n(N - 1, total + N)


print(sum_of_n(5,0))
```

This recursive function is a lil' different than others because it ain't printing anything, it's returning it.

`sum_of_n` takes `N` and `total` as an argument. At each recursive call, `N` is added to the `total` and then decreased by 1.

This goes on until the base condition `N == 0` becomes true. In this case:

- `sum_of_n(5, 0)` ➜ return `sum_of_n(4, 5)`
- `sum_of_n(4, 5)` ➜ return `sum_of_n(3, 9)`
- `sum_of_n(3, 9)` ➜ return `sum_of_n(2, 12)`
- `sum_of_n(2, 12)` ➜ return `sum_of_n(1, 14)`
- `sum_of_n(1, 14)` ➜ return `sum_of_n(0, 15)`
- `sum_of_n(0, 15)` ➜ Base case reached. Returns 15

This is how the final result gets back to the original call. And that value is returned to the user.

**NOTE:** Time complexity will be O(N) because the function is called N times, with each call performing O(1) work.

---

At this point, you should get a question in your mind.

*"The normal `for` loop (brute force approach) is O(N) and even this recursive approach is O(N), then what's the point of using recursion?"*

Yes, compared to recursion, `for` loop is the better tool. Same O(N) time. But this exercise is just for understanding the working mechanism of recursion.

Recursion actually earns its place when the problem is naturally nested, like trees and graphs, folders inside folders, JSON, backtracking, or divide-and-conquer stuff like merge sort. Writing those with loops gets messy fast, while recursion is a few clean lines.