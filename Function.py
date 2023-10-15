print('*****In python, function is a group of related statement to perform a specific task********')


def greetme():   #def is the identifier to create any function and then give function name
    print('Good Morning')
greetme()  #=Good Morning

print('******************function with parameter****************************************')
def greetme(name):
    print('Good Morning' + name)
greetme('Rakesh Yadav')  # = Good MorningRakesh Yadav

print('******************Add intergers**************************************************')

def greetme(name):
    print('Good Morning' + name)
def addinterfers(a,b):
    print(a+b)           # instead of printing we can also return this which will show in next example
greetme('Rakesh Yadav')
addinterfers(2,3)   # = Good MorningRakesh Yadav   and for line17 answer is 5 printed in  nextline

print('************instead of printing we can also return this which will show in next example *****************')

def greetme(name):
    return 'Good Morning' + name
def addinterfers(a,b):
    return a+b           # instead of printing we can also return this which will show in next example
print(greetme('Rakesh Yadav'))
print(addinterfers(2,3))  ## instead of printing above we will print here

print('************my example *****************')
def gladme(num):
    print('morning' + num)
def interger(y,z):
    return y*z
print(gladme('rocky'))
print(interger(8,9))

print('************my example *****************')


