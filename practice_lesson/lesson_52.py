def say_something(word,*args):
    print('word = ', word)
    for i, arg in enumerate(args):
        print(i, arg)

say_something('Hi!','Mike','Nance')


#t = ('Mike','Nancy')
#say_something('Hi!',*t)