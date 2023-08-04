from time import sleep
print("Welcome to calculator.py!")
sleep(1)
print("what operation would you like to perform? ")
sleep(1)

operation = '[addition, subtraction, multiplication, division,]: '
   
user = input(operation)

if user == "addition": 
 x = int(input("what's the value of the first term: "))
 sleep(0.50)
 y = int(input("what's the value of the second term: "))
 sleep(1)
 result = x + y

elif user == "subtraction": 
 x = int(input("what's the value of the first term: "))
 sleep(0.50)
 y = int(input("what's the value of the second term: "))
 sleep(1)
 result = x - y

elif user == "multiplication": 
 x = int(input("what's the value of the first term: "))
 sleep(0.50)
 y = int(input("what's the value of the second term: "))
 sleep(1)
 result = x * y

elif user == "division": 
 x = int(input("what's the value of the first term: "))
 sleep(0.50)
 y = int(input("what's the value of the second term: "))
 sleep(1)
 result = x / y

print(f"the result of {user} is {result}")
 
 
