# O(n) - Linear Time

**_Linear time complexity means that the running time of an algorithm grows linearly with the size of the input._**

The number of steps grows directly proportional to the input size.  
**Basically, double the input, double the work.**

```python
def sum_array(array):
    total = 0

    for num in array:
        total += num

    return total
```

This function will loop through all the elements exactly once. If there are 10 elements in the array, then it's 10 steps. If 10,000 elements, then 10,000 steps. No shortcuts, no halving, every element gets visited.

Stuff like linear search, finding max/min element in an unsorted array, traversing a linked list, printing all elements, etc. are all **O(n)** operations.
