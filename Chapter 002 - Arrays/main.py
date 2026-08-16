fruits = ["apple", "banana", "cherry", "date", "elderberry"]

fruits_dict = {fruit: index for index, fruit in enumerate(fruits)}


# O(n)
def search_array(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1


# O(1)
def search_hashmap(hashmap, target):
    return hashmap[target]


print(search_array(fruits, "cherry"))
print(search_hashmap(fruits_dict, "cherry"))
