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
  bool1 = bool(integer1>5)
  print (bool1)
  

def q3():
  letter = input("Input the letter a: ")
  bool1 = bool(letter== 'a' )
  print(bool1)
  

def q4():
  word= input("Input a word earlier in the dictionary than google: ")
  bool1= bool(word < "google")
  print (bool1)
  

def q5():
  integer= input("Input an integer: ")
  integer1 = (int(integer))
  integer2= input ("Input another integer: ")
  integer3 = (int(integer2))
  integer4 = int(integer1*integer3)
  bool1 = bool(integer4>40)
  print (f"Your numbers multiplied together are greater than 40: {bool1}")
  
  
#Do edit the code below
#Comment the lines below when running your tests

#q1()
#q2()
#q3()
#q4()
#q5()
