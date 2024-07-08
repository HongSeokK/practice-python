def print_inf(func):
    def wrapper(*args,**kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

def print_more(func):
    def wrapper(*args,**kwargs):
        print('func: ',func.__name__)
        print('args: ',args)
        print('kwargs: ',kwargs)
        result = func(*args, **kwargs)
        print('result: ',result)
        return result
    return wrapper

@print_inf
@print_more
def add_num(a, b):
    return a + b

def sub_num(a,b):
    return a - b

r = add_num(10,20)
print(r)

f = print_inf(print_more(sub_num))
r = f(10,20)
print(r)




#print('start')
#r = add_num(10,20)
#print('end')
#
#print(r)