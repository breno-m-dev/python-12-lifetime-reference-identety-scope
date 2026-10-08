# Part VI — Identity Investigation

## Exercise 14 — `id()` Detective

Write a program that:

1. Creates a list called `a`.
2. Assigns `b = a`.
3. Creates `c = a.copy()`.
4. Prints the `id()` of all three objects.
5. Determines which names refer to the same object.

Your program should produce a conclusion similar to:

```text
a and b refer to the same object.
c refers to a different object.
```
## Solution Exercise 14
```python
a = []
b = a
c = a.copy()

print(f"id(a):{id(a)} ")
print(f"id(b):{id(b)} ")
print(f"id(c):{id(c)} ")
```
---

## Exercise 15 — Identity Changes

Investigate what happens to the identity of an object after the following operation:

```python
x = [1, 2, 3]

original_id = id(x)

x.append(4)

print(original_id == id(x))
```

Then compare it with:

```python
x = [1, 2, 3]

original_id = id(x)

x = x + [4]

print(original_id == id(x))
```

Explain the difference between the two operations.

---
## Solution Exercise 15

x.append(4) mutates de list.

x = x + [4] rebounds the list