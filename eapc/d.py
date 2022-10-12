line = input()
left = "q w e r t a s d f g z x c v b".split(" ")
right = "y u i o p h j k l n m".split(" ")

is_left = not line[0] in left
for char in line:
    char_is_left = char in left
    if char_is_left and not is_left:
        pass
    elif char_is_left and is_left:
        print("no")
        exit()
    elif not char_is_left and is_left:
        pass
    else:
        print("no")
        exit()
    is_left = char_is_left
print("yes")
