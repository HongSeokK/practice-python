a = 1
b = 2

if a == b:
    print('equal')

print(a > 0 and b > 0)
print(a < 0 or b < 0)
print(a > 0 or b < 0)

if a > 0 and b > 0:
    print('positive')

if a > 0 :
    if b > 0:
        print('positive')
a = -1
b = 2
if a > 0 or b > 0:
    print('positive')


if a > 0 :
    print('a or b positive')
elif b > 0 :
    print('a or b positive')