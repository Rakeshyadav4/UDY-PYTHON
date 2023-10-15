# keyword class should be used to create class in Python language ex: calculator is a class below
#class calculator:
   # num = 100
  #  def getdata(self):        # this self is compulsory
 #       print('i am now executing as a method in class')
#obj = calculator()  # syntax to create objects in python
#print(obj.num)    # = 100
#print(obj.getdata())  # = i am now executing as a method in class  and in next line = none( because no constructor)
#************what is constructor in class*************')

class calculator:
    num = 100
    def __init__(self):
        print('I am called automatically when object is created')

    def getdata(self):        # this self is compulsory
        print('i am now executing as a method in class')
obj = calculator()
obj.getdata()
print(obj.num)



