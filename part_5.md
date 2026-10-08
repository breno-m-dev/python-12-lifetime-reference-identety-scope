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

## Solution exercise 12
First output:
["Python","Python"]
Second output:
[]

First solution uses a global list and its method to change the list.
It's interesting here there was no need to use global statement, since
we're using the list method .append inside the method add_item().
The second one creates a local list, because of that it doesn't change
The global one.
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


Exercise 13 — Mutation vs. Rebinding
1. x = []
Rebounds x

2. x.append(1)
mutates x

3. x = [1, 2]
rebounds x

4. x += [3]
mutates. Its not quite obvious, but += on a list is the same as doing
x.extend() and NOT x = x + [3]

5. x = x + [4]
rebounds x