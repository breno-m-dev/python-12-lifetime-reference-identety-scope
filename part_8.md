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
## Solution exercise 19
1. Everytime the method is called with default argument, its
the exact same object that will be used. Even after a method call without using the default argument, the default argument object will still exist! Insane
2. Yes
3. Because the code stores default arguments instead of clearing them after a method execution ends. Python is crazy. This could be usefull, but
I recommend using YIELD instead
so it's more clear for others
what is going on.
It could be usefull in some specific situations though.
the following would create a new
default list everytime the method
is called without a argument
```python
def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items
```
4. The default list is created when the function definition is executed,before the first function call.
---