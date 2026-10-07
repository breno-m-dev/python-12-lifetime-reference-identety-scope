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


## Exercise 10 solution

1. On first line of the create_list() method.
2. The name only exists inside the create_list() method, but the object
it references, will still exist while another name reference it, in this
case the name result also references it.
3. No, only the name data disapears not the object it references.
4. Because the method returned a reference to it.
5. If there are any names still referencing it.
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


## Exercise 11 solution
1. Because X was local, and the print is outside of X's scope
2. It doesnt not, neither does the object it references.
3. In this case yes. But it could be different if the method returned a reference to the list.


---