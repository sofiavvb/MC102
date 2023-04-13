'''
sequencia = [1] * 5
i = 1
while i < 10:
    breakpoint()
    sequencia[i] = sequencia[i - 1] * i
    i += 1
print(sequencia)
'''

for i in range(5, 11):
    for j in range(10 - i):
        print(" ", end="")
    for j in range(2 * i):
        print("*", end="")
    for j in range(10 - i):
        print(" ", end="")
    print()