# # print('Hello World!')  
# print('Hello world!')

# favNumber=12


# print('My fav number is:', favNumber)

# # LECTURE 17 WORK

# message=input("what's your name? ")

# print('My name is', message)

# message="I want to ask you a question"

# print(message)

# message+=input("/nWhat's your name? ")

# n=int(input("Enter a number: "))
# print(n+100)

# # LECTURE 18 WORK

# weight=input("How much do you weight?")

# # print(weight)

# weight=(int(weight))

# print(weight)

# print(weight>75)

# # LECTURE 19 INTEGERS WORK

# a=1
# b=5
# print(a+b)

# print(a-b)

# c=0b101101101
# print(c)

# # Octodecimal example:
# d=0o124432
# print(d)

# # Hexadecimal
# e=0x1a23
# print(e)

# my_num='123'
# # # The "print(my_num + b)" will give you an error as you have not formatted the string into an int when declaring.
# # print(my_num + b)

# # The following won't give you the same error as you have converted it into an int on declaration.
# my_num_2=int('123')

# # The following will tell you the type of value that is declared by the variable
# print(type(a))


# # binary translation of my_num_2:
# print(bin(my_num_2))

# # Octo translation of my_num_2:
# print(oct(my_num_2))

# # Hex translation of my_num_2:
# print(hex(my_num_2))

# # Floating Point Numbers & Complex Numbers
# j=1e2
# print(j)

# # LECTURE 22 WORK
# pay_rate=float(input('Whats your pay?'))
# print(pay_rate)

# name=str(input("Whats your name?"))
# if name != str:
#     print('Please enter a valid name next time')
# age=int(input("Whats your age?"))
# income=float(input("Whats your yearly income?"))
# print("Name: ", name)
# print("Age: ", age)
# print("Income: ", income)

# # CHALLENGE: calculating a percentage

# price=float(input('Enter the price of the item you want to buy: '))
# twentyPercent=(price*.2)
# print("Discount: ", twentyPercent)
# salePrice=price-twentyPercent
# print("Sale price: ", salePrice)

# # CHALLENGE: Calculating an Average
# testScore1=float(input("Enter your first test score: "))
# testScore2=float(input("Enter your second test score: "))
# testScore3=float(input("Enter your three test score: "))
# Average=(int(testScore1+testScore2+testScore3)/3)

# print(Average)


# # CHALLENGE: Converting a math formula to a programming statement
# # p = F/((1 + r)**n)
# f=(float(input("Please enter the desired future value: ")))
# r=(float(input("Please enter the annual interest rate: ")))
# n=(int(input("Enter the number of years that the money will sit in the amount: ")))
# p=f/((1+r)**n)
# print(p)

# z=1
# x=2,
# y=1

# # Strings
# a="Hey, how are you doing in \b this day?"
# print(a)

# # String operators & built-in functions
# name="TURING"
# print(name.lower()) #Converts to lower case
# print(ord('+')) # ord is used to find the unicode No. for a certain value, which can be letters, numbers, special characters etc.
# print(chr(97)) # chr does the opposite as it finds the value for the unicode inputted.
# # %s and %d will take the values within the parenthesis and input them.
# print('My name is %s and my weight is %d Kg'%('Raz', 75)) #Here, %s will have to be a string and %d an integer.
# print('My name is {0:s} and my weight is {1:d} Kg'.format('Raz', 75))
# print('My name is {} and my weight is {} Kg'.format('Raz', 75))

# # F-string: An improved string formatting syntax
# from email import message

# name="Alan"
# print("Hello, %s" % name)

# first_name="Alan"
# last_name="Turing"
# age=45
# profession='mathematician'
# print("Hello %s %s. You are %s years old. You are a %s." % (first_name, last_name, age, profession))
# print("Hello, {}. You are {}.".format (name, age))
# print("Hello, {1}. You are {0}.".format (age, name)) # this will get you results based on the index.
# print(f"Hello {name}. You are {age} years old. You are a {profession}.")

# message=(f"Hi {name}."
#                f"You are a {profession}."
#                )
# print(message)


# # LECTURE 30
# first='Alan'
# last='Turing'
# age=50

# print('The value of pi is approximately: %.2f' %(3.1415))
# print('The value of pi is approximately: %.3f' %(3.1415))

# print("my name is {x} and I am {y} years old.".format(x='Andreas',y=43))
# message=f'Hello Mr {last}, I try to learn Python'
# print(message)

# import math
# age=50
# print(f"Alans age times pi is {age*math.pi:.2f}")


# # LECTURE 31 String indexing
# a='apple'
# print(a[3]) # prints out l
# print(a[len(a)-1]) # prints the last letter within the string
# print(a[-len(a)])


# # LECTURE 32 String Slicing
# d='avocado'
# print(len(d))
# print(d[1:4]) # prints out voc
# print(d[:5]) # prints out avoca
# print(d[2:len(d)]) # prints out ocado
# print(d[:]) # prints out the full string
# print(d[0:7:2])
# print(d[::2]) # prints out the increments of two
# print(d[::-2]) # prints out the increments of two backwards


# # LECTURE 33 The difference between strings and numbers
# age='12'

# converted_age=int(age)
# if converted_age==12:
#     print('Do you like maths?')

# # LECTURE 35 Type Casting

# print(int('10'))

# print(float('5'))

# print(str(5.5))

# # LECTURE 36 Dates and Times
# import datetime
# print(datetime.datetime.now())
# print(str(datetime.datetime.now().date()))
# from datetime import date, time, datetime
# today=date.today()
# print(today)
# now=datetime.now()
# print(now)


# # PROJECT: Create a Receipt Printing Program

# # create a product and price for three items

# # from email import message


# p1_name, p1_price="Orange", 5.90 
# p2_name, p2_price="Shampoo", 3.70 
# p3_name, p3_price="Olive Oil", 9.50 

# # create a company name and information
# company_name="golden corner"
# company_address="2 Mandilara St."
# company_city="Rodos, Gr"

# # declare ending message
# message="Thanks for shopping with us today!"

# # create a top border
# print("*" * 50)

# # print company information first, using format
# print("\t\t{}".format(company_name.title()))
# print("\t\t{}".format(company_address))
# print("\t\t{}".format(company_city))

# # print a line between sections
# print("=" * 50)

# # print out headers for section of items
# print("\tProduct Name\tProduct Price")

# # create a print statement for each product
# print("\t{}\t\t${}".format(p1_name.title(), p1_price))
# print("\t{}\t\t${}".format(p2_name.title(), p2_price))
# print("\t{}\t\t${}".format(p3_name.title(), p3_price))

# # print a line between sections
# print("=" * 50)

# # print out header for section of total
# print("\t\t\tTotal")

# # calculate total price and print out 
# total = p1_price + p2_price + p3_price
# print("\t\t\t${}".format(total))

# # print a line between sections
# print("=" * 50)

# # output thank you message
# print("\n\t{}\n".format(message))

# # create a bottom border 
# print("*" * 50)


# # LECTURE 38:  WHAT IS A LIST?
# from math import prod

# appleProducts=['iPhone', 'iPad','airMac','iCloud']
# # print(appleProducts)
# print(appleProducts[0])
# products=appleProducts
# products=appleProducts[1:3]
# print(products)
# appleProducts.append('iPod')
# print(appleProducts)
# del appleProducts[1]
# print(appleProducts)


# # LECTURE 39: WORKING WITH LISTS
# from traceback import print_tb

# appleProducts1=['iPhone', 'iPad', 'iPod']
# appleProducts2=['iCloud', 'iOS', 'airMac']
# appleProducts1.extend(appleProducts2) # This merges appleProducts1 with appleProdcuts2
# print('office' in appleProducts1)
# print('iOS' in appleProducts1)
# appleProducts1.insert(2, 'office')
# print(appleProducts1)
# appleProducts1.remove('airMac')
# print(appleProducts1)
# appleProducts1.sort()
# print(appleProducts1)

# # LECTURE 40: MAKING NUMERICAL LISTS
# num=list(range(1, 10)) # this will give you 1 to 9. For 1 to 10, do rang(1, 11) instead 
# print(num)


# # LECTURE 41: PRINTING LISTS
# Cars=['Toyota', 'BMW', 'Fiat', 'Seat']
# print(*Cars, sep='\n') #sep is used to seperately print each of the list items in a new line.
# for Item in Cars:print(Item.rjust(8), sep='/n') # This will align the content with the right margin.
# print('First:{0}\nSecond: {1}'.format(*Cars)) 


# # LECTURE 42: PRACTICE
# Cars=['BMW','Audi',  'Genesis', 'Infiniti']
# print(Cars)
# Cars.sort()
# print(Cars)


# # LECTURE 43: TUPLES
# from traceback import print_tb

# t=('apple', 'banana', 'orange', 'melon', 'blueberry','cherry')
# print(t)
# print(type(t))
# # sb=['grape', 'peache', 'watermelon', 'pear']
# # print(type(sb))
# print(t[0])
# print(t[3:6])
# print(t[1:4])
# print(t[0:6:2]) # 0 = first item, 6 = last or number 6 item, 2 = item to be outputted from the list
# print(t[::-1]) # The tuple gets outputted backwards

# a='tomato'
# b=16
# print(a, 9.963, b)



# # LECTURE 44: Tuple Assignment, Packing and Unpacking
# t=('apple', 'banana', 'orange', 'melon')
# print(t[0])
# (s1, s2, s3, s4) = t
# print(s1)
# print(s2)
# print(s3)
# print(s4)

# x1, x2, x3 = 4, 5, 6
# print(x1, x2, x3)

# # Swapping
# a='apple'
# b='banana'
# print(a,b)
# a, b = b, a
# print(a, b)



# # LECTURE 45: WORKING WITH DICTIONARIES
# people={'Andreas':75, 'john':85, 'Jim':25}
# print(people)
# # Adding a value to the dictionary
# people['Alan']=90
# print(people)
# # Changing a value in the dictionary
# people['Jim']=33
# print(people)
# # Deleting an entry
# del people['john']
# print(people)
# # Dictionaries do not use index numbers. The following will give you a key error:
# # print(people[0])
# d={
#     0:'earth',
#     1:'hermes',
#     2:'venus'
# }
# print(d[0])
# print(d[2])



# # LECTURE 46: SETS

# print(set(['apple', 'banana']))
# print(set("avocado"))
# print(list("avocado"))
# print(set())
# x={'Turing', True, (1,2)}
# print(x)

# # The below cannot be hashed:
# # s='Hello'
# # s.append("a")
# # print(s)
# # print(hash([1,2,3]))
# # print(hash({1:2}))
# # x={1,[1,2,3]}
# print(x)


# # LECTURE 47: EXERCISE 7: DICTIONARIES
# friend={
#     'Name':'Anders', 
#     "Age": '40', 
#     'Job': 'Teacher', 
#     'Place':'Greece'
#     }

# print("My friend's name is "+friend['Name']+" and he is "+friend['Age']+". His job is "+friend['Job']+" and he lives in "+friend['Place'], "."  )



# # LECTURE 49: IF STATEMENT

# userInput=input('Please enter 1 or 2:')
# if userInput=='1':
#     print('You entered the number 1')
# elif userInput=='2':
#     print('You entered the number 2')
# else:
#     print('You did not enter a valid number')
   
   
 
# # CODING EXERCISE 6: ODD OR EVEN

# input=int(input('Enter a number: '))
# modulo=input%2
# print(modulo)

# if modulo==0 :
#     print('Your input is an even number')
# elif modulo==1 :
#     print('Your input is an odd number ')
# else:
#     print('Please print a whole number')



# LECTURE 50 EXAMPLES of Using the if Statement in an Application
# MyValue=10
# if MyValue==5:
#     print('My value does equal 5!')
# elif MyValue!=5:
#     print('My value does not equal to 5')
#     print('Done!')   
    
# Value=int(input("Type a number between 1 and 5: "))
# if (Value>0) and (Value<=5):
#     print("You typed: ", Value)
# else:
#     print("The value you typed is incorrect!")

# print("1. Pasta")
# print("2. Pizza")
# print("3. Salad")
# print("4. Panacota")
# choice=int(input('Select your favourite menu: '))
# if (choice==1):
#     print("You chose Pasta")
# elif (choice==2):
#     print("You chose Pizza")
# elif (choice==3):
#     print('You chose Salad')
# elif (choice==4):
#     print("You chose Panacota")
# else:
#     print("You made an invalid choice!")
#     print("Hint: Choose from the menu next time!")

# one=int(input("Type a number between 1 and 5: "))
# two=int(input("Type a number between 1 and 5: "))
# if (one>=1) and (one<=5):
#     if (two>1) and (two<=5):
#         print("One*two", one*two)
#     else:
#         print("Incorrect second value!")
# else:
#     print("Incorrect first value!")



# # CODING EXERCISE 7: PIZZA STREET 99
 
#  # Don't change the code below 👇

# print("Welcome to Pizza Street 99!")
# size=input("What size pizza do you want? S, M, or L ").upper()
# add_prosciutto=input("Do you want prosciutto crudo? Y or N ").upper()
# extra_cheese=input("Do you want extra cheese? Y or N ").upper()
# # Don't change the code above 👆

# #Write your code below this line 👇
# bill=0

# if size=="S":
#     bill+=10
# elif size=="M":
#     bill+=15
# elif size=="L":
#     bill+=20

# if add_prosciutto=="Y" and size=='S':
#     bill+=2
# elif add_prosciutto=="Y" and size=='M' or add_prosciutto=="Y" and size=='L':
#     bill+=4

# if extra_cheese=="Y":
#     bill+=1
    
# print(f"Your final bill is: ${bill}.") 





# # LECTURE 51: BREAK AND CONTINUE

# num=5
# while num>0:
#     print('CURRENT NUMBER: ', num)
#     num=num-1
#     if num==1:
#         continue





# # LECTURE 52: FOR LOOPS

# seasons={'Winter', 'Spring', 'Summer', 'Fall'}

# for year_seasons in seasons:
#     print(year_seasons)
    
# # Enumerate prints out the index beside each of the items in the loop
# for year_seasons in enumerate (seasons):
#     print(year_seasons)
    




# # LECTURE 53: EXAMPLES OF USING THE FOR STATEMENT
# Value=input("Type less than 8 characters: ")

# letterNum=1
# for letter in Value:
#     print("Letter", letterNum, " is ", letter)
#     letterNum+=1
#     if letterNum>8:
#         print("The string is too long!")
#         break

# letterNum=1
# for letter in 'Andreas':
#     if letter=="d":
#         pass
#         print("Encountered d, not processed")
# print('Letter', letterNum, "is", letter)
# letterNum=+1

# Value=input("Type less than 6 characters")
# letterNum=1
# for letter in Value:
#     print("Letter", letterNum, " is ", letter)
#     letterNum+=1
# else:
#     print("The string is blank")





# # LECTURE 54: WHILE LOOPS

# num=0
# while (num<4):
#     print(num)
#     num+=1
# print("Good bye! ")

# prompt="Enter a message"
# prompt+="\nEnter quit if you want to terminate the program: "
# myText=""
# while myText!="quit":
#     myText=input(prompt)





# # EXERCISE 8: FOR LOOPS

# spanishSpeakers=['Spain', 'Mexico', 'Cuba']

# for countries in spanishSpeakers:
#     print(countries)





# # EXERCISE 9: IF STATEMENT

# score=int(input('How many points did the player score? '))

# if score>=1:
#     print(f'Player scored {score} points')
# else:
#     print("The player did not score any points")
    
# # OR

# # elif score==0:
# #     print('Player did not score any points')





# # LECTURE 57: PROJECT: GUESSING GAME
# import random

# computers_number= random.randint(1,50)
# prompt='What is your guessing? '
# while True:
    
#     players_guess=input(prompt)
#     if computers_number==int(players_guess):
#         print("Correct! ")
#         break
#     elif computers_number>int(players_guess):
#         print("Too low!")  
#     else:
#         print("Too high!")





# # LECTURE 59: USING IF STATEMENTS WITH LISTS
# shopping=['rice', 'bread', 'milk', 'cheese', 'toothpaste']
# scanner=input('Hello! Which product do you want?' )
# if scanner in shopping:
#     print('We have this type of product in the supermarket!')
# else:
#     print('Sorry. There is no such type of product')





# # LECTURE 60: USING FOR LOOPS WITH LISTS
# available_doctors=['Anesthesiologist', 'Cardiologist', 'Dentist', 'Dermatologist', 'Orthopedist']
# for available_doctors in available_doctors:
#     print('In this hospital there is: ', available_doctors, 'available')





# # LECTURE 61: USING A WHILE LOOP WITH LIST AND DICTIONARIES
# print('You have to enter the password to access the app: ')
# myCode=int(input('What is the code?'))
# password={'app': 1111}
# while myCode!=password['app']:
#     print('You entered the wrong password. Try again.')
#     myCode=int(input('What is the code? '))
# print('Correct!')