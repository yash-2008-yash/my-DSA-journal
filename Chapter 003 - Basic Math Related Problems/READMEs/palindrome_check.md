# Check if a number is palindrome or not

**OBJECTIVE:** Given an integer `number`, return **true** if it's a palindrome, else return **false**.

A palindrome is a number that reads the same backward as forward. For example, 121, 1331, and 4554 are palindromes because they remain the same when their digits are reversed.

---

**Example 1**  
*Input:* `number` = 4554  
*Output:* Palindrome number  
**Why?** The reverse of 4554 is 4554 and therefore it is a palindrome number.

<br>

**Example 2**  
*Input:* `number` = 7789  
*Output:* Not Palindrome number  
**Why?** The reverse of 7789 is 9877 and therefore it is not a palindrome number.

---

Algorithm:

Now we know how we can extract digits and create a number, too. Using it, we can check whether the original number and reversed number are same or not to decide whether to call it as a palindrome or not.

- Initialize an integer `rev_number` to 0. This variable will store the reverse of the number.
- Make a duplicate of the `number` and store it in an integer for later comparison.
- Run a while loop with the condition `number > 0` to reverse the number and at each iteration:
  - Get the last digit of the `number` by using the modulus operator % with 10 and store it in a temporary variable.
  - Update the `rev_number` by multiplying it by 10 and adding the last digit.
  - Update the `number` by integer division with 10 effectively removing the last digit.
- After the loop, check if the `number` duplicate is equal to the `rev_number`.
- If they are equal, return **true** indicating the number is a palindrome.
- If they are not equal, return **false** indicating that the number is not a palindrome.

```python
number = 1001
number_copy = number
rev = 0

while number > 0:
    digit = number % 10
    rev = rev * 10 + digit
    number = number // 10

if number_copy == rev:
    print("yes")
else:
    print("no")
```