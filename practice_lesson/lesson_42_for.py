some_list=[1,2,3,4,5]

#i = 0
#while i < len(some_list):
#    print(some_list[i])
#    i+=1

#for i in some_list:
#    print(i)
"""
for s in 'abcdee':
    print(s)

for word in ['My','name','is','Mk']:
    if(word == 'name'):
        #break
        continue
    print(word)
"""

for fruit in ['apple','orange','banana']:
    if fruit == 'orange':
        print('stop eating')
        break
    print(fruit)
else:
    print('Ate all!')