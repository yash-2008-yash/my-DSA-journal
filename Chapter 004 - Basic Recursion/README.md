# Introduction to Recursion

**Recursion** is a programming technique to solve a problem by breaking it into smaller sub-problems. This "breaking" goes on until the problem gets so small that the answer is obvious (the base case).

Recursion has 5 parts. Let me break them down easily:

1. **Base case:** This is what stops the recursion. If base case isn't defined, recursion will go on forever, creating infinite calls and program crash (stack overflow). ALWAYS write the base case first.
2. **Recursive case:** The recursive function calls itself with a smaller input. At every call, it has to move closer to the base case, or it will never stop.
3. **Body of the recursive function (The Job):** This is performed whenever the recursive function is called. The main job of the function is defined here.
4. **Return:** It passes the result back up the chain. When multiple recursive calls are there, each call must return its value to its parent call. This goes on until the OG call gets the value. This is only needed when a value needs to be returned, not necessary when you are just printing something.
5. **Call stack:** Each recursive call waits on top of the one before it. A LIFO data structure to store the recursive calls (LIFO - last in, first out).

### Advantages of Recursion

- **Simplifies code:** Complex problems can be solved in fewer lines of code compared to iterative solutions.
- **Natural representation:** Problems that are recursive in nature (like tree traversals, factorial, Fibonacci, etc.) are easier to express.
- **Reduces code complexity:** Avoids writing nested loops, making the logic more readable and elegant.
- **Useful in divide-and-conquer algorithms:** Essential for algorithms like QuickSort, MergeSort, Binary Search, and Dynamic Programming.

### Disadvantages of Recursion

- **High memory usage:** Each recursive call adds a new layer to the function call stack, which may lead to memory overhead.
- **Risk of stack overflow:** Without proper base cases, infinite recursion can occur and crash the program.
- **Slower execution:** Function calls and returns add extra overhead compared to simple loops.
- **Harder to debug:** Tracing recursive calls can be confusing, especially in deep recursion.

---

*You won't understand recursion properly until you try some programming examples.*

Here are some exercises that made **recursion** click for me:
- [Print name N times using recursion](./READMEs/name-n-times.md)
- [Print 1 to N using Recursion](./READMEs/1-to-n.md)
- [Print N to 1 using Recursion](./READMEs/n-to-1.md)
- [Sum of First N Numbers](./READMEs/sum-of-n-numbers.md)