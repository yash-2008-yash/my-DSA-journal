# Arrays

I think we already know this shit. The declaration, the initialization, blah blah blah...  
**So, instead of doing it again, I'm gonna do some real work.**

- If you know where the element is located, just use it's index to access it. _This is an O(1) operation._
- If you don't know where it's located, use an algorithm (linear search, binary search, etc.) to optimize your search. _This is an O(n) operation._
- Remember that O(1) is always faster than O(n). So, can we search for an element in O(1) instead of O(n)? **FUCK YEAH!** You can store the array elements in a hash-based data structure like a hash set or hash map, so finding element will be O(1).

Let's see the 3rd way properly:

---

### Hash-Based Data Structures

A hash table doesn't search for elements like arrays do. It calculates where they should be.

Imagine you want to store "apple" in a hash table. The array underneath has 10 slots for instance (0 to 9).  
Where will "apple" get stored? First, it'll get converted to a number. Say "apple" gets converted to the number 69. Now, you take that number and squeeze it down to fit in the 10 slots, using something like `69 % 10 = 9`. So, "apple" goes to slot 9.

When you want to check if "apple" exists, you don't have to search like we do in arrays. You just have to perform the same calculation. Turn "apple" into 69, then `69 % 10 = 9`, and then check slot 9 directly. No searching. That's why it's O(1).

This whole process of turning the key into a number, then squeezing it to fit the array size, is called **hashing**.

**NOTE:** You don't have to do this "hashing" shit yourself. A built-in hash function called `hash()` will do this conversion.

Okay, enough of this theory bullshit, let's see an example.

```python
# ----- USING AN ARRAY -----

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# O(n)
def search_array(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1

print(search_array(fruits, "cherry"))   # 2
```

```python
# ----- USING AN HASHMAP -----

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

fruits_dict = {fruit: index for index, fruit in enumerate(fruits)}

# O(1)
def search_hashmap(hashmap, target):
    return hashmap[target]

print(search_hashmap(fruits_dict, "cherry"))    # 2
```

Both give the same output, but see the difference in the time complexity!

**NOTE:** In hashmap example code, `fruits` is converted into a hashmap first, which is a O(n) operation. But, that's the trade off. You build hashmap once with an O(n), and then you can search in O(1) always. No pain, no gain, baby!

---

### Collisions

Hash-based data structures are good. But... there's a catch. Collisions can happen.

At this point, you must have known that hash based DS don't have the concept of index. Elements are stored based on math calculation. That's why they are faster than arrays in searching. But, sometimes two different keys can hash to the same slot. That's **collision**. Fun fact is that it's unavoidable *(Pigeonhole principle - "If more pigeons are placed into fewer pigeonholes, at least one pigeonhole must hold more than one pigeon.)*

There are 2 common fixes for this shit:
- [Chaining](./READMEs/chaining.md)
- [Open Addressing](./READMEs/open%20addressing.md) ← PYTHON INTERNALLY USES THIS!

Technically, O(1) is the "average case" for hash tables, not guranteed worst case. A garbage hash function can degrade the time complexity towards O(n).

---