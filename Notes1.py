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

# String operators & built-in functions
name="TURING"
print(name.lower()) #Converts to lower case
print(ord('+')) # ord is used to find the unicode No. for a certain value, which can be letters, numbers, special characters etc.
print(chr(97)) # chr does the opposite as it finds the value for the unicode inputted.
# %s and %d will take the values within the parenthesis and input them.
print('My name is %s and my weight is %d Kg'%('Raz', 75)) #Here, %s will have to be a string and %d an integer.
print('My name is {0:s} and my weight is {1:d} Kg'.format('Raz', 75))
print('My name is {} and my weight is {} Kg'.format('Raz', 75))