it = 4
while it < 1:
    print(it)  #It will not print because it is not less than 4 so it will not go to loop
# now will make it true as it >1 then it will get into loop and start giving answer 4444.. and until it is false
# now we add extra step like it = it-1
it = 4
while it > 1:
    print(it)
    it = it-1  #now it stop until it become false like 4 , 3, 2, and 1 is not greater than 1 so it stop
print('****************************************************')
it = 50020
while it > 50000:
    print(it)
    it = (it-1)
print('****************************************************')
to = 4
while to > 1:
    if to != 3:
        print(to)
    to = to-1
print('****************************************************')
# now we apply break loop to the above scenario
to = 4
while to > 1:
    if to == 3:
        break
    print(to)
    to = to-1
# answer will be 4 because it started with 4 and 4-1 = 3 which is equal to 3 hence it broken loop

print('*********will replicate above with big numbers************')
to = 10
while to > 1:
    if to == 5:
        break
    print(to)
    to = to - 1
print('loop ended')
print('********continue loop***********')
it = 10
while it > 1:
    if it == 9:
        it = it - 1   # we have one more codition if 9 == 9
        continue  # here since 9 = 9 condition say continue 'so it is going back to first after it = it - 1 which is 8
    if it == 3:  # since 3 ==3 it break the loop and didn't print 3, 2, 1
        break
    print(it)
    it = it - 1
print('loop end')
print('********Another example continue loop***********')
so = 20
while so > 1:
    if so == 4:
        so = so - 1
        continue
    if so == 3:
        break
    print(so)
    so = so - 1
print('result')





