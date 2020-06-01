##Advance Printing

i = 4
f = 3.4

print('our float value is %s. Our integer value is %s'% (f,i))

##Conditional statement in python
if i == 1 and f > 4:
    print("i is equal to 1 and f is greater than 4")
elif i > 4 or f > 4:
    print("i and f are both greater than 4")
else:
    print("neither i nor f is greater than 4")

##Loops
l = [1,2,3,4]

for element in l:
    print(element)

print('\n New Loop \n')

count = 6
while count < 10:
    print(count)
    count += 1

#Creating functions in python
print('\n creating functions \n')
def add2(x):
    y = x + 2
    return y

i = add2(5)
print(i)

print('\n lambda function \n')
square = lambda x: x*x

square(3)
