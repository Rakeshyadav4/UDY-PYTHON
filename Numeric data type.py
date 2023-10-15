print('******************************************************************')
print("hello world")
print('***************# successfully printed variable********************')
int = 3
print(int)
print('****************successfully printed String***********************')
str = 'Hello'
print(str)
print('*************successfully printed combination of int, str and float*********************')
a, b, c = 5.7, 6, 'greaT'
print(a,b,c)
# or
d = 10
e = 3.5
f = 'string'
print(d,e,f)
print('******************concatenate str + int**************************')
#  print('value is' +b) = this will throw error because it has mix of int and str so now we
#  will see how to do like open 2 flower bracket and tell
# python that expecting 2 values so put above 2 arguments one is string and another intergers
#  which will go to 2 flower brackets and you can more arguments then add more flower brakets.
print('{} {}'.format('value is', b))
print('************************concatenate str + str*********************')
h, i, j = 'me', 'you', 'to'
print('value is' +h)
print('**********************to find what data type python***************')
print(type(b))
print(type(a))
print('*********create a variable with integer value.*********************')
a=100
print("The type of variable having value", a, " is ", type(a))
print('*********create a variable with float value.***********************')
b=10.2345
print("The type of variable having value", b, " is ", type(b))
print('*********create a variable with complex value.*********************')
c=100+3j
print("The type of variable having value", c, " is ", type(c))
print('*********to find particular argument.*********************')
name = ('rakesh', 2, 4, 'rahul')
print(name)
print(name[1])


