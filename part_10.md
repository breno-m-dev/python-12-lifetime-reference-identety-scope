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