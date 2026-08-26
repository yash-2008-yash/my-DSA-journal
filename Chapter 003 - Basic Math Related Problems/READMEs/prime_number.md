# Check if a number is prime or not

**OBJECTIVE:** Given an integer `number`, check whether it is prime or not.

---

**Example 1**  
*Input:* `number` = 2  
*Output:* true  
**Why?** 2 is a prime number because it has exactly two divisors: 1 and 2.

<br>

**Example 2**  
*Input:* `number` = 10  
*Output:* false  
**Why?** 10 isn't a prime number because it has more than two divisors: 1, 2, 5, and 10.

---

Algorithm:

We can iterate through 1 to `number`, counting how many of these numbers divide `number` without a remainder. If exactly two numbers do, `number` is prime otherwise it is not prime.

- Initialize a variable to count the number of factors and set it to 0.
- Start a loop from 1 to `number`, iterating through each number i. Inside the loop:
  - Check if `number` is divisible by i without any remainder.
  - If it is, increment the counter variable by 1.
- After the loop if the number of divisors is equal to 2, return **true** indicating the number is prime.
- If the number of divisors is not equal to 2 (but greater), return **false** indicating that the number is not prime.

```python
number = 7

factors = []

if number < 0:
    print("NO")

if number == 2:
    print("YES")

for i in range(1, number + 1):
    if number % i == 0:
        factors.append(i)

if len(factors) == 2:
    print("YES")
else:
    print("NO")
```