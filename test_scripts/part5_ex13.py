x = [1]
print(f"id before{id(x)}")
x += [3]
print(x)

print(f"id after += {id(x)}")

x = x + [2]