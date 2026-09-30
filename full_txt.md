# Python Object Model Exercises

A collection of theoretical and practical exercises designed to develop a deeper understanding of Python's object model.

The exercises cover:

* Scope
* Object lifetime
* References
* Object identity
* Equality
* Mutability
* Assignment and rebinding
* Function arguments
* Default arguments
* Shallow copies
* Closures
* Object graphs

---

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

---

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

# Part III — Scope

## Exercise 7 — Local vs. Global

Predict the output:

```python
x = 10

def change():
    x = 20
    print(x)

change()
print(x)
```

Explain why the two values are different.

---

## Exercise 8 — Reading vs. Rebinding

Consider the following code:

```python
x = 10

def test():
    print(x)

test()
```

Now compare it with:

```python
x = 10

def test():
    x = 20
    print(x)

test()
print(x)
```

Answer the following questions:

1. Why can the first function access `x`?
2. Why does the second function create a different `x`?
3. What is the difference between **accessing** a name and **rebinding** a name?
4. Does assigning a value to a name inside a function automatically modify a global name with the same identifier?

---

## Exercise 9 — The `global` Statement

Predict the output:

```python
counter = 0

def increment():
    global counter
    counter += 1

increment()
increment()

print(counter)
```

Then answer:

1. What does the `global` statement do?
2. What would happen if `global counter` were removed?
3. Why does `counter += 1` require special treatment here?

---

# Part IV — Object Lifetime

## Exercise 10 — Returning an Object

Consider:

```python
def create_list():
    data = [1, 2, 3]
    return data

result = create_list()
```

Answer the following questions:

1. When is the list object created?
2. When does the local name `data` exist?
3. Does the list disappear when `create_list()` returns?
4. Why does `result` still refer to the list?
5. What determines whether the list object is still alive?

---

## Exercise 11 — Name Lifetime vs. Object Lifetime

Predict what happens:

```python
def create():
    x = [1, 2, 3]

create()

print(x)
```

Answer the following questions:

1. Why can't `x` be accessed after the function returns?
2. Does the name `x` still exist after the function returns?
3. Does the list object necessarily have the same lifetime as the name `x`?
4. What would need to happen for the list object to remain accessible after the function returns?

---

# Part V — Mutation and Scope

## Exercise 12 — The Sneaky List

Predict the output:

```python
items = []

def add_item():
    items.append("Python")

add_item()
add_item()

print(items)
```

Now compare it with:

```python
items = []

def add_item():
    items = []
    items.append("Python")

add_item()
add_item()

print(items)
```

Explain why one function modifies the outer list while the other does not.

---

## Exercise 13 — Mutation vs. Rebinding

For each operation below, determine whether it **mutates an existing object** or **rebinds a name**:

```python
x = []

x.append(1)

x = [1, 2]

x += [3]

x = x + [4]
```

For each statement, answer:

1. Is the existing object modified?
2. Is the name `x` rebound?
3. Can the identity of `x` change?
4. Why?

---

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

# Part VII — Function Arguments

## Exercise 16 — How Does Python Pass Arguments?

Consider:

```python
def modify(value):
    value.append(10)

numbers = [1, 2, 3]

modify(numbers)

print(numbers)
```

Answer the following questions:

1. Was the list copied when passed to the function?
2. Does `value` refer to the same object as `numbers`?
3. What happens to the list when `value.append(10)` is executed?
4. Is it accurate to simply say that Python uses "pass-by-reference"?
5. What is meant by **call-by-sharing** or **pass-by-object-reference**?

---

## Exercise 17 — Rebinding a Parameter

Compare the following two examples.

### Example A

```python
def modify(value):
    value = [10, 20, 30]

numbers = [1, 2, 3]

modify(numbers)

print(numbers)
```

### Example B

```python
def modify(value):
    value.append(10)

numbers = [1, 2, 3]

modify(numbers)

print(numbers)
```

Answer the following questions:

1. Why does Example A leave `numbers` unchanged?
2. Why does Example B modify `numbers`?
3. What happens to the local name `value` in each example?
4. What is the difference between rebinding `value` and mutating the object referenced by `value`?

---

# Part VIII — Default Arguments

## Exercise 18 — The Mutable Default Argument

Predict the output:

```python
def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item("A"))
print(add_item("B"))
print(add_item("C"))
```

Explain:

1. When is the default list created?
2. How many list objects are created by the function definition?
3. Why does the list persist between function calls?
4. Is the default list recreated every time the function is called?
5. What is the recommended way to write this function?

---

## Exercise 19 — Default Argument Identity

Investigate the following code:

```python
def test(items=[]):
    print(id(items))

test()
test()
test()
```

Answer:

1. What do you observe?
2. Are the three calls using the same default object?
3. Why?
4. When was that default object created?

---

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
2. Is `a.copy()` a deep copy?
3. Which objects are shared between `a` and `b`?
4. What would happen if you replaced `a.copy()` with `copy.deepcopy(a)`?

---

## Exercise 21 — Draw the Object Graph

Consider:

```python
a = [[1, 2], [3, 4]]
b = a
c = a.copy()
```

Draw an object graph showing:

* Names
* References
* List objects
* Nested list objects
* Shared objects

For example:

```text
a ─────┐
       ↓
     [ list ]
       │
       ├──→ [1, 2]
       └──→ [3, 4]

b ─────┘
```

Then add `c` to the diagram.

---

# Part X — Advanced Object Semantics

## Exercise 22 — What Happened?

Predict the output without executing the code:

```python
x = [1, 2]

def modify(value):
    value.append(3)
    value = [4, 5]
    value.append(6)

modify(x)

print(x)
```

Then explain every step in terms of:

* References
* Mutation
* Rebinding
* Object identity
* Scope

---

## Exercise 23 — Lifetime and Closures

Consider:

```python
def outer():
    data = [1, 2, 3]

    def inner():
        print(data)

    return inner

function = outer()

function()
```

Answer the following questions:

1. `outer()` has already returned. Why can `inner()` still access `data`?
2. What is a closure?
3. What happened to the lifetime of `data`?
4. What keeps the `data` object alive?
5. What scope does `data` belong to?
6. How does the closure affect the lifetime of the referenced object?

---

# Part XI — Final Challenge

## Exercise 24 — Explain the Object Model

Analyze the following program:

```python
def create_counter():
    count = [0]

    def increment():
        count[0] += 1
        return count[0]

    return increment


counter_a = create_counter()
counter_b = create_counter()

print(counter_a())
print(counter_a())
print(counter_b())
print(counter_a())
```

Without running the program, determine:

1. The output.
2. How many `count` objects exist.
3. Which calls share the same `count` object.
4. Why `counter_a` and `counter_b` maintain independent state.
5. What keeps each `count` object alive.
6. Which scopes are involved.
7. How references are involved.
8. How object lifetime is affected by the closures.
9. How object identity relates to the two counters.
10. How mutation differs from rebinding in this example.

---

# Bonus — Conceptual Questions

Answer the following questions in your own words.

## Question 1

What is the difference between:

* A name
* A reference
* An object
* An identity

---

## Question 2

Can two names refer to the same object?

Give an example.

---

## Question 3

Can two different objects have the same value?

Give an example.

---

## Question 4

What determines whether an object is still alive?

---

## Question 5

Can an object outlive the function in which it was created?

Explain with an example.

---

## Question 6

What is the difference between:

```python
x = y
```

and:

```python
x = y.copy()
```

---

## Question 7

Why can mutating an object through one name affect another name?

---

## Question 8

Why does rebinding a name usually not affect another name that previously referred to the same object?

---

## Question 9

What is the difference between object identity and equality?

---

## Question 10

Why can mutable default arguments cause unexpected behavior?

---

# Suggested Study Order

The concepts in this exercise set are strongly connected. A useful order for reviewing them is:

```text
Names
  ↓
References
  ↓
Objects
  ↓
Identity
  ↓
Equality
  ↓
Mutability
  ↓
Assignment
  ↓
Rebinding
  ↓
Scope
  ↓
Object Lifetime
  ↓
Function Arguments
  ↓
Default Arguments
  ↓
Closures
  ↓
Object Graphs
```

The goal is not only to memorize Python's behavior, but to develop the ability to **reason about what objects exist, which names refer to them, how long they remain alive, and how operations affect their identity and state.**
