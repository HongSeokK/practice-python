import builtins

builtins.print()
print(globals())

ranking = {
    'A':100,
    'B':85,
    'C':95
}
print(ranking)
for key in ranking:
    print(key)

print(sorted(ranking,key=ranking.get, reverse=True))