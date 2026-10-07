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

## Exercise 4 solution
True
True
[1, 2, 3, 4]
[1, 2, 3, 4]

This happens because both names reference the same object. 
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

## Exercise 5 solution
1. No.
2. Yes, because they have the same value.
3. Yes, only if both names reference the same object they will have the 
same id

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

## Exercise 6 solution
[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 3, 5]
True
False

a and b reference the same object since b = a was executed.
c is a copy of a, meaning it references a diferent object with the same
values that "a" had when c = a.copy() was executed. After that line of 
code they are not linked anymore.


---