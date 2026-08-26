# Find GCD of two numbers

**OBJECTIVE:** Given two integers `number_1` and `number_2`, find their greatest common divisor.

---

**Example 1**  
*Input:* `number_1` = 9, `number_2` = 12  
*Output:* 3  
**Why?** The factors of 9 and 12 are [1, 3, 9] and [1, 2, 3, 4, 6, 12] respectively. The common factors are [1, 3] and the greatest common factor is 3.

<br>

**Example 2**  
*Input:* `number_1` = 20, `number_2` = 15    
*Output:* 5    
**Why?** The factors of 20 and 15 are [1, 2, 4, 5, 10, 20] and [1, 3, 5, 15] respectively. The common factors are [1, 5] and the greatest common factor is 5.

---

Algorithm:

We know that we can extract digits of a number by repeatedly taking modulo 10 and dividing by 10. Instead of just extracting digits, we can append them in reverse order to build a number, which is effectively the reversed `number`.

- Initialize a variable to store the reversed number as 0.
- Loop while the `number` is greater than 0.
- Extract the last digit by performing modulo 10.
- Multiply the reversed number by 10 and add the extracted digit.
- Remove the last digit from the `number` using integer division by 10.
- Continue this process until the `number` becomes 0.
- Return the reversed number.

```python
number_1 = 20
number_2 = 15

factors_1 = []
factors_2 = []

for i in range(1, number_1 + 1):
    if number_1 % i == 0:
        factors_1.append(i)

for i in range(1, number_2 + 1):
    if number_2 % i == 0:
        factors_2.append(i)

common_factors = list(set(factors_1).intersection(factors_2))
print(max(common_factors))
```