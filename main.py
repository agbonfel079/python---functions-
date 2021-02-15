# def greet():
#     return "Hello Victor"
  
# print(greet())

#===================

'''
Functions with parameters
'''
#def greet (name):
#'''
#Greets a person passed in as  argument
#name: a name  of a person  to greet
#'''
 
#   return f"Hello {name}, Good morning"
# print(greet("Felix", "Kingsley"))
# print(greet("Felix", "Kingsley"))
# print(greet("Kingsley"))
# print(greet("Adriana"))

# help(greet)

'''
Arbitrary parameters
'''

def fruits(*names):
  '''
  Accepts unknown number of fruit names and prints each  of them  
  *name: list of fruits
  '''
  # names are  tuples
  #print(type(names))
  
  # for fruit in names:
  #  print(fruit)

#fruits("Orange", "Banana", "Apple", "Grapes")

#fruits("Orange")

'''
Keyword parameters
'''

def greet(name, msg):
  '''
  This function greets a person with a given message 
  name: person  to greet
  msg: message to greet person with
  '''

  # return f"Hello {name}, {msg}"

 

# print(greet("Felix", "Good morning!"))
# print(greet("Good morning", "Adriana!"))

# print(greet(name="Felix", msg="Good morning!"))
# print(greet(msg="Good morning!",name= "Adriana", tel="123"))
  
'''
Arbitrary  Keyword parameters
'''
# def person(**student):
#   # print(type(student))
#   # print(student)
#   for key in student:
#     print(student[key])

# # person(fname="Felix", lname="Johnson")
# person(fname="Felix", lname="Johnson", subject="Python")

'''
Default parameter values
'''

# def greet(name='David'):
#    return f"Hello, {name}"
# print(greet())
# print(greet("Dayana"))
  
# '''
# Pass statement
# '''

# def greet():
#   pass

'''
Recursion
'''

def factorial_recursive(n):
  '''
  Multiply a given  number  by every number less  than  it down  to 1  in a factorial way 
  e.g  if n is 5 then  calculate 5*4*3*2*1 = 120
  n: is the highest starting number
  '''
  if n == 1:
    return True
  else:
   return n * factorial_recursive(n -1)

print(factorial_recursive(5))