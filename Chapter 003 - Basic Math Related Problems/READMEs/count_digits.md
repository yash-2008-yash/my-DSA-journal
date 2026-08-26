# Count all digits of a number

**OBJECTIVE:** Given an integer `number`, return the number of digits in `number`.

---

**Example 1**  
*Input:* `number` = 12345  
*Output:* 5  
**Why?** The `number` 12345 has 5 digits

<br>

**Example 2**  
*Input:* `number` = 7789  
*Output:* 4  
**Why?** The `number` 7789 has 4 digits

---

Algorithm:

- Initialise a counter to store the number of digits.
- While `number` is greater than 0, execute the following:
  - Increment the counter by 1
  - Update `number` by removing its last digit by performing a modulo 10 (%10) operation on it.
- After exiting the while loop, we return the counter as the number of digits.

```python
number = 123456
digits = 0

while number > 0:
    digits += 1
    number = number // 10

print(f"digits: {digits}")
```