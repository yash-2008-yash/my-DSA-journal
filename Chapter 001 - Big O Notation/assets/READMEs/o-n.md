# O(n) - Linear Time

The number of steps grows directly proportional to the input size.  
**Basically, double the input, double the work.**

```cpp
int array_sum(vector<int>& array) {
  int sum = 0;

  for (int i = 0; i < array.size(); i++) {
    sum += array[i];
  }

  return sum;
}
```

This function will loop through all the elements exactly once. If there are 10 elements in the array, then it's 10 steps. If 10,000 elements, then 10,000 steps. No shortcuts, no halving, every element gets visited.

Stuff like linear search, finding max/min element in an unsorted array, traversing a linked list, printing all elements, etc. are all **O(n)** operations.