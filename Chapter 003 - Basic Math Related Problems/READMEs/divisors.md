# Print all divisors of a given number

**OBJECTIVE:** Given an integer `number`, return all divisors of it.

---

**Example 1**  
*Input:* `number` = 36  
*Output:* [1, 2, 3, 4, 6, 9, 12, 18, 36]  
**Why?** The divisors of 36 are 1, 2, 3, 4, 6, 9, 12, 18, 36.

<br>

**Example 2**  
*Input:* `number` = 12  
*Output:* [1, 2, 3, 4, 6, 12]  
**Why?** The divisors of 12 are 1, 2, 3, 4, 6, 12.

---

Algorithm:

Find all the divisors of `number` by iterating through every number from 1 to `number` and check whether it is a divisor or not. We can store all the divisors and return the list of divisors after iteration.

```python
number = 36
factors = []

for i in range(1, number + 1):
    if number % i == 0:
        factors.append(i)

print(factors)
```