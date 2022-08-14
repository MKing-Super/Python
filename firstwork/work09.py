for i in 'qwertyuiop':
    print(i)

print("--------------------------")

fruits = ['banana', 'apple',  'mango']
for i in fruits:
    print(i)

print("---------------------------------")

for i in range(len(fruits)):
    print(fruits[i])

print("-----------------------------")

for num in range(20,30):
    print("-")
    for i in range(2,num):
        print(i)
        print(num)

        break
    else:
        print("end")
