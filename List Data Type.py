print('********************list of having only integers****************************************')
a= [1,2,3,4,5,6]
print(a)
print('********************list of having only strings*****************************************')
b=["hello","john","reese"]
print(b)
print('********************list of having both integers and strings****************************')
c= ["hey","you",1,2,3,"go"]
print(c)
print('********************index are 0 based. this will print a single character****************')
print(c[1]) #this will print "you" in list c

print('*****************************************************************************************')
rock = [1, 2, 'chill', 9, 'in', 5]  # Liat is data type that allows multiple value and can be different data types
print(rock[2])  # = chill
print(rock[0])  # = 1
print('********************************shortcut to print last value -1***************************')
print(rock[-1])  # = 5
print('********************************print value from 2 to*************************************')
print(rock[1:5])  # = [2, 'chill', 9, 'in']
print('**********************insert value to existing command and print the value ****************')
rock.insert(3,'out')  #rock = [1, 2, 'chill', 9, 'in', 5]
print(rock)  # =  [1, 2, 'chill', 'out', 9, 'in', 5]
print('********************************shortcut to add value at last***************************')
rock.append('new end value')
print(rock)  # = [1, 2, 'chill', 'out', 9, 'in', 5, 'new end value']
print('********************************Update existing value to a new value ***************************')
rock[3] = 'Reya'
print(rock)  # = [1, 2, 'chill', 'Reya', 9, 'in', 5, 'new end value']
print('********************************to Delete existing value ******* ***************************')
del rock[4]
print(rock)  #=[1, 2, 'chill', 'Reya', 'in', 5, 'new end value']
print('******************************************************************')
fruits = ["apple", "banana", "cherry"]
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

