def outer(a,b):
    def plus(c,d):
        return c+d

    result = plus(a, b)
    result2 = plus(b,a)
    print(result + result2)

outer (1,2)