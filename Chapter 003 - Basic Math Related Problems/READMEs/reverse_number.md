# Reverse a number

**OBJECTIVE:** Return the reverse of the given `number`.

Note: If a number has trailing zeros, then its reverse should not include them. For example, reverse of 10400 should be 401, not 00401.

---

**Example 1**  
*Input:* `number` = 12345   
*Output:* 54321  
**Why?** The reverse of 12345 is 54321.

<br>

**Example 2**  
*Input:* `number` = 7789  
*Output:* 9877    
**Why?** The reverse of 7789 is 9877.

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
number = 142300
rev = 0

while number > 0:
    digit = number % 10
    rev = rev * 10 + digit
    number = number // 10

print(rev)
```