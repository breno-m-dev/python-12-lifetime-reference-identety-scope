# Part II — Predict the Output

## Exercise 4 — Same Object

Without running the code, predict the output:

```python
a = [1, 2, 3]
b = a

print(a is b)
print(a == b)

b.append(4)

print(a)
print(b)
```

Then explain why each result occurs.

---

## Exercise 5 — Two Equal Objects

Predict the output:

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a is b)
print(a == b)
```

Answer the following questions:

1. Are `a` and `b` references to the same object?
2. Are the objects equal?
3. How can you prove your answer using `id()`?

---

## Exercise 6 — Copy vs. Assignment

Predict the output:

```python
a = [1, 2, 3]

b = a
c = a.copy()

b.append(4)
c.append(5)

print(a)
print(b)
print(c)

print(a is b)
print(a is c)
```

Explain the results in terms of object identity and references.

---