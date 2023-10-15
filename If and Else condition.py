python = 'programming language'
if python == 'non programming language':  # sign : is important to end the if condition
    print('condition matches')            #  result condition should not start from the begin always bit gap
    print('Second line')           # it will keep consider as one condition until you start typing from the begin
else:                                     #  again sign: is important to end the esle condition
    print('condition do not match')       # Again we should not start from the begin
print('condition done')      # this will print as seperate request as has no conditon and started in begin with no gap
print('********similary another example for condition match****************************')

python = 'programming language'
a = 4
if a > 2:
    print('condition matches')
    print('Second line')
else:
    print('condition do not match')


print('*******************************example********************************')

age = 5
if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

