days = ['Mon','Tue','Wed']
fruit = ['apple','banana','orange']
drinks = ['coffee','tea','beer']

#for i in range(len(days)):
#    print(days[i],fruit[i],drinks[i])

for day,fruit,drink in zip(days,fruit,drinks):
    print(day,fruit,drink)
