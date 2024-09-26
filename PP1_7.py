'''
    Lesson: Booleans
    Author: Mr Kalisz
    Date Created: Sept 25, 2024
    Date Last Modified: Sept 25, 2024
'''

def q1():
  bool = True
  print (bool)

def q2():
  integer = input("Input an integer: ")
  integer1= int(integer)
  bool= True
  bool2 = False
  bool= integer1 > 5
  print(bool)
  bool2 = integer1 < 5
  print (bool2)

def q3():
  letter = input("Input letter a:")
  bool= True
  bool2 = False
  bool = (letter == "a")
  print(bool)
  bool2 = (letter > "a")
  print (bool2)
def q4():
  word= input("Input a word earlier in the dictionary than google: ")
  bool = True
  bool2 = False
  bool= (word < "google")
  print (bool)
  bool2 = (word > "google")
  print (bool2)

def q5():
  integer= input("Input an integer: ")
  integer1 = (int(integer))
  integer2= input ("Input another integer: ")
  integer3 = (int(integer2))
  print ("Your numbers multiplied together is greater than 40: ")
  bool = True
  bool2 = False
  bool = (integer1*integer3)>40
  print (bool)
  bool2 = (integer1*integer3)>40
  print (bool2)
#Do edit the code below
#Comment the lines below when running your tests

# q1()
# q2()
# q3()
# q4()
# q5()
