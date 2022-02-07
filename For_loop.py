result = 0
low = int(input("Input starting number: "))
high = int(input("Input ending number: "))
mult = int(input("Input the multiple number: "))


for x in range(151):
    print(x)

for x in range(5, 1001, 5):
    print(x)

for x in range(1, 100):
    if x % 10 == 0:
        print('coding dojo')
    elif x % 5 == 0:
        print('coding')
    else:
        print(x)

for x in range(500001):
    if x % 2 != 0:
        result += x
print (result)

for x in range(2018, 0, -4):
    print(x)

for x in range(low, high, mult):
    print(x)