# Check if a number is Armstrong number or not

**OBJECTIVE:** Given an integer `number`, return **true** if it's an Armstrong number, otherwise return **false**.

Note: An Amrstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

---

**Example 1**  
*Input:* `number` = 153  
*Output:* true  
**Why?** 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

<br>

**Example 2**  
*Input:* `number` = 345  
*Output:* false  
**Why?** 3^3 + 4^3 + 5^3 = 9 + 64 + 125 = 198

---

Algorithm:

- Calculate the number of digits in the input number and store it in k.
- Initialize a variable `sum` to 0. This variable will store the sum of each digit raised to the power of number of digits in number.
- Make a copy of the original `number` to store it in a temporary variable.
- Run a while loop with the condition `number > 0` and at each iteration:
  - Get the last digit of `number` by using the modulus operator % with 10 and store it in a temporary variable.
  - Add the digit raised to the power of k of the sum.
  - Update `number` by integer division with 10 effectively removing the last digit.
- After the loop, check if the original input number is equal to the sum of the digits raised to the power of the number of digits in the number.
- If they are equal, return **true** indicating the number is an Armstrong number.
- If they are not equal, return **false** indicating that the number is not an Armstrong number.

```python
number = 371
number_copy = number
digits_list = []
sum = 0

while number > 0:
    digit = number % 10
    digits_list.append(digit)
    number = number // 10

for num in digits_list:
    sum += num ** len(digits_list)

if sum == number_copy:
    print("yes")
else:
    print("no")
```