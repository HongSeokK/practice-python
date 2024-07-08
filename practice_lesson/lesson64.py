"""
TEST TEST ##################################
"""

animal = 'cat'

def func():
    #global animal
    animal = 'dog'
    print('local',locals())
    print(func.__name__)
    print(func.__doc__)

func()
print(__name__)
print(globals())