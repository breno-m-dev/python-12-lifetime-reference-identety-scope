a = [1, 2, 3]
b = [1, 2, 3]

print(a is b)
print(a == b)

print(id(a))
print(id(b))

a = b

print(id(a))
print(id(b))
