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