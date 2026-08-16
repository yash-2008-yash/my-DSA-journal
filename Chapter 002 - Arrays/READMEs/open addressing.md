# Open Addressing

In this method, one slot can have only one value. No sharing like *chaining method*. If the slot's taken, then probing will take place to find the next free slot.

In this example:

```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
fruits_dict = {fruit: index for index, fruit in enumerate(fruits)}
```

Imagine that the hash table has 10 slots and:

- `hash("apple") % 10 = 3`
- `hash("banana") % 10 = 7`
- `hash("cherry") % 10 = 3` ← Same as **apple**!

Now "apple" and "cherry" both want slot 3. That's a collision.

<br>

With **Open addressing method**, we can solve this:

Now, slot 3 is occupied by "apple". If "cherry" is hashed to slot 3, then the next slot is checked? If slot 4 is free, "cherry" goes to slot 4. If slot 4 was also not empty, next slot would have been checked. Even though "cherry" real slot is 3, it's now stored in slot 4.

If you do `fruits_dict["cherry"]`:

1. Compute `hash("cherry") % 10 = 3`
2. Go to slot 3, check if "cherry" is there. No, it's apple. Not a match.
3. Since it's occupied by something else, keep probing. Check slot 4
4. Slot 4 has "cherry". Found it!

With too many collisions, and too much probing, clustering can happen, which drags the time complexity O(1) to O(n). This defeats the whole point of using hashmap.

Python internally handles this by performing quadratic probing, double hashing, etc.

You don't have to worry about any of this, you just have to know what's happening under the hood.

---