#a sample dictionary variable

a = {1:"first name",2:"last name", "age":33}

#print value having key=1
print(a[1])   #= first name
#print value having key=2
print(a[2])   #=last name
#print value having key="age"
print(a["age"]) #= 33
print('**********another example where key and value should be in " if it is string')
rakesh = {1: 'name', 'reya': 'daughter', 4: 5}
print(rakesh[4])  # = 5
print(rakesh["reya"])    # = daughter
print(rakesh[1])  # = name
print('*************create dictionary and pass values in that Dictionary**********')
raki = {}
raki['version'] = 2023
print(raki)    # {'version': 2023}
print('*************passing values in that Dictionary**********')
raki['state'] = 'VIC'
raki[99] = 'number'
raki[5] = 2023
print(raki)  # {'version': 2023, 'state': 'VIC', 99: 'number', 5: 2023}
print('*************printing particular value**********')
print(raki['state'])  # = VIC

print('*************example***********************e**********')
student = {"name": "Bob", "age": 25, "major": "Computer Science"}
print('age',student['age'])  # =age 25
print("Name:", student["name"]) # Name: Bob


