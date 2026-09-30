# Part I — Foundations

## Exercise 1 — Names and Objects

Answer the following questions:

1. What is a variable in Python?
2. Is a variable a container that physically stores an object?
3. What happens when you execute the following statement?

```python
x = 10
```


4. What is the difference between a **name**, an **object**, and a **reference**?
5. What does the `=` operator do in Python?

## Exercise 1 Solution:

1. It's name that references an object, for example x = 5 is a reference to an
integer number.

2. No, a name refers to were the stored data is

3. x starts referencing an integer of the value of 10

4. Name is the name of a variable. Like in x = 5, "x" is the name.
Object is an instance of a class, reference is when a variable points to a
space in memory where there is data, wheter its a basic type like int, str,
float, etc or data strucutures like lists, dictionaries, tuples, sets, etc. Or
a class type created by the user for example.
5. it makes a variable on the left side to reference the values on the right
side


---

## Exercise 2 — Assignment and References

Consider the following code:

```python
a = [1, 2, 3]
b = a
```

Answer the following questions:

1. How many list objects were created?
2. How many names refer to the list?
3. What happens when you execute:

```python
b.append(4)
```

4. Why does `a` also contain `4`?

## Exercise 2 Solution:

1. only one list was created.
2. Two, a and b.
3. It will appen d a value to the list that both a and b reference.
4. Because both names refer the same object.

---

## Exercise 3 — Identity vs. Equality

Explain the difference between:

```python
a == b
```

and:

```python
a is b
```

Answer the following questions:

1. What does `==` compare?
2. What does `is` compare?
3. When should `is` normally be used?
4. Can two different objects be equal?
5. Can two names refer to the same object?



## Exercise 3 Solution:

1. it compares if the left and right values are the same. It does use
what a name references not the name itself.
2. is command checks if 2 names refer the same object. And also to check
if a name refers no object. For example if x is None.
3. whenever one wants to check if 2 names are exacly refering the same
thing
4. Yes, because they can have the same value.
5. Yes. 

---