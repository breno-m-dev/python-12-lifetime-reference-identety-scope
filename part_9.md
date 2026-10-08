# Part IX — Nested References

## Exercise 20 — Shallow Copy

Predict the output:

```python
a = [[1, 2], [3, 4]]
b = a.copy()

b[0].append(99)

print(a)
print(b)
```

Answer the following questions:

1. Why did modifying `b` affect `a`?
3. Which objects are shared between `a` and `b`?
3. What would happen if you replaced `a.copy()` with `copy.deepcopy(a)`?

## Solution exercise 20
1. Because it was a shallow copy not a deep one! So the outer list is copied, but the nested lists are still shared between a and b.
2. All the nested data structures inside the list
3. what would change b would not affect a
---
