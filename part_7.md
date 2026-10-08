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

## Solution exercise 16

1. No it wasn't copied. A reference to the object that list refers was sent, not a copy of the object. For a copy it would be: 
```Python
modify(numbers.copy())
```
2. In the instance where modify was called as modify(numbers), yes, they refer the same object.

3. The list numbers is modified, since a object method was used.
If the code did 
```python
value = value + 10
```
then it would rebound the name value, instead of mutating the list.
4. By default yes, but you may pass the value or just use the value.
Either by the use of copy() method.
Or my rebounding the argument.
5. Call by sharing is the use of a copy of the value of the object as argument on a method.
Pass-by-object-reference is passing an object reference as argument, meaning what the method does, will change the same object sent, not a copy.
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


## Solution Exercise 17
1. Because it rebounds the name  value inside the method modify. By doing so the reference is lost.

2. Because it uses the reference of the argument and mutates it, instead of rebounding it.

3. Both names cease at the end of the method. But in example A the object that value refers to, also ceases to exist. 
In example B the oject will still exist since there still are references to it outside of the method.

---