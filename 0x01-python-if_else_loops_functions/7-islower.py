def islower(c):

    return ord('a') <= ord(c) <= ord('z') if len(c) == 1 else False

print(islower('a'))
print(islower('B'))
print(islower('5'))
