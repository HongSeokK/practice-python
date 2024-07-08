def say_someting():
    s = 'hi'
    print(s)
    return s

print(type(say_someting))
result=say_someting()
print(result)

def what_is_this(color):
    if color == 'red':
        return 'tomato'
    if color == 'green':
        return 'green pepper'
    else:
        return 'i don\'t know'

result=what_is_this('green')
print(result)