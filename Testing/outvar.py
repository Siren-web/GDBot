def test(flags):

    global flag

    flags = not flags
    print(flags)
    flag = flags

flag = True
test(flag)
print(flag)
