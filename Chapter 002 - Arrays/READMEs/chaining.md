# Chaining

In this method, each slot holds a small list of everything that hashed there.

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

With **Chaining method**, we can solve this:

Instead of each slot holding only one value, each slot holds a small list. When "apple" get hashed to slot 3, the list becomes `[("apple", 0)]`. When "cherry" also gets hashed to slot 3, the list becomes `[("apple", 0), ("cherry", 1)]`.

If you do `fruits_dict["cherry"]`:

1. Compute `hash("cherry") % 10 = 3`
2. Go to slot 3
3. Slot 3 has a list, not a single value. So, now you loop through that small list checking which pair's key matches "cherry"
4. Slot 3 has a list, not a single value — so now you loop through _that small list_ checking which pair's key matches "cherry"
5. Found it: `("cherry", 2)` → return `2`

This "each slot holds a list, and you loop through just that list" approach is called **chaining** — the collided items get chained together at one slot.

If you notice clearly, step 3 is a O(n). If that small list becomes large, the size is resized accordingly and rehashed so that one list don't have too many values.

You aren't getting a true O(1) time complexity. But, with fewer collisions and shorter chains, it's still close to O(1).

---