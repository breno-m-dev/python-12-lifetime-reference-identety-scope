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

## Exercise 7 solution
output:
20
10

Explanation: The x = 20 is a local variable inside the function, it is
not the same x that is outside of it.
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

## Exercise 8 solution
1. Because no x was declared inside the function. So the only
x avaiable was the global one.
2. Because when it was done x = 20, a new x was created to reference the value 20.
3. Accessing is just using a variable value for something like
print(x). Rebidding is making the name reference another value/object.
4. No it doest not, it only changes the local name reference.
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

## Exercise 9 solution
1. It enables a function to change the global variable instead of creating a new local one.
2. There would be an error, since there would be no local variable 'counter' and the code would try to access it before
creating it. With the global declaration it specifies the code
is using the global variable, not with a local one, so it fixes the error.
3. Because it's creating a new value based on a past value, if
there are no past values there will be an error. In other words, it must be initialized first.
---