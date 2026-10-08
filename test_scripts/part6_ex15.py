x = [1, 2, 3]

original_id = id(x)

x.append(4)

print(original_id == id(x))
print("*************")

x = [1, 2, 3]

original_id = id(x)

x = x + [4]

print(original_id == id(x))