def test(items=[]):
    print(id(items))

test()
test()
print("oioioi")
i = 0
while(i < 10000000):
    i += 1
test()
test([1,2])
test() ## <- THIS IS CRAZY O_o <-