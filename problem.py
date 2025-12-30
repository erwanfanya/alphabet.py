# Ask the user for two numbers
num1 = int(input(" Enter a number: "))
num2 = int(input("Enter a second number:"))

# Perform operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

# Print results
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)

# asking user for input
a = int( input("Enter a number:"))
b = int (input("Enter a second number:"))

#perform modulus & floor division 
z = a // b
c = a % b
# print result
print(c)
print(z)
# Ask user for an integer
num = int(input(" Enter a integer")) 

# Initialize factorial
factorial = 1

# Calculate factorial using a for loop
for i in range(1, num + 1):
    factorial *= i

# Print the result
print("Factorial of", num, "is", factorial)

# Ask the user for a string
text = input("Enter a string: ")

# Vowel counter
vowel_count = 0

# Loop through each character in the string
for s in text:
    # Check if the character is a vowel (case-insensitive)
    if s in "aeiou":
        vowel_count += 1

# Print the result
print("Number of vowels:", vowel_count)

#
import random
secret_num = random.randint(1,100)

guess = 0

while guess != secret_num:
    guess = int(input("enter a number: "))
    if guess > secret_num:
        print("too hight")
    elif guess < secret_num:
        print("too low")
    else :
        print("correct you guessed the secret_num")

# I'm putting an input to ask the user for thier age
age = int(input("enter your age please: "))
  
if age >=18:
    print("True")
else: 
    print("false")
