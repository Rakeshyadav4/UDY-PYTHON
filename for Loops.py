name = 'rakesh'
a = 10000
b = 900
yadav = "chaitra"
1 > 100

if yadav == 'chaitra':  # == is very impotant in if condition only for cha not int since for int use > or < sign
    print('condition matches')
    print('done')
else:
    print('condition not matching')
    print('done')
print('**********************************************************************')
#for loop

obj = [2, 3, 5, 7, 9]
for i in obj:
    print(i)  # to pint the each number
print('**********************************************************************')
obj = [2, 3, 5, 7, 9]
for i in obj:
    print(i*2)  # to multiple each number with 2
print('**********************************************************************')
# print first 5 natural number ie 1 2 3 4 5
for j in range(1, 6):  # range (i,j) = i to j-1
    print(j)
print('**********************************************************************')
# sum of first 5 natural number ie 1+2+3+4+5 = 15
sumation = 0
for j in range(1, 6):
    sumation = sumation + j
    print(sumation)  # it will show the process for the sum of each step
print(sumation)      # it will show final outcome of the sum.
print('**********************************************************************')
addition = 1
for l in range (5, 20):
    addition = addition + l
print(addition)
print('**********************************************************************')
for k in range (1,10,2):
    print (k)
print('**********************************************************************')
for k in range(1, 10, 5):
    print(k)
print('************Skipping first index*****************************************************')
# if you don't give starting index like (10) then it will consider as (0, 10)
for k in range(10):
    print(k)
print('**********************************************************************')
for number in range(50020, 50000, -1):
    print(number)
print('**********************************************************************')
for i in range(50001, 50021):
    print(f'PO{i:05d}')
print('**********************************************************************')
addition = 0
for rakesh in range(1, 90):
    addition = (addition + rakesh)
print(addition+rakesh)
print('**********************************************************************')
count = 0
while count < 5:
    print("Count:", count)
    count += 1











