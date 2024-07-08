def counter(num=10):
    for _ in range(num):
        yield 'run'

def greeting():
    yield 'Good morning'
    for i in range(10):
        print(i)
    yield 'Good afternoon'
    for i in range(10):
        print(i)
    yield 'Good night'

#for g in greeting():
#    print(g)

g = greeting()
c = counter()
print(next(g))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print(next(g))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print(next(g))