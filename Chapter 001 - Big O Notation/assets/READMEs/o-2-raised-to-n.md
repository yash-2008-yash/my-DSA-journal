# O(2ⁿ) - Exponential Time

In this operation, when one element is added to the input, the work doubles.

This usually happens with recursion where 2 calls happen each time. For example, **Fibonacci**.

```cpp
int fibonacci(int n) {
  if (n <= 1) { 
    return n; 
  }

  return fibonacci(n - 1) + fibonacci(n - 2);
}
```

In every function call, 2 recursive call arises.

That means `fibonacci(10)` is approx. 1000 calls, `fibonacci(30)` is approx. 10,00,000 and `fibonacci(40)` is approx. 1B calls!