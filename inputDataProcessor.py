#Objective:
#The aim of this assignment is to process and format user input data.

#Task 1: Input Length Validator
#Write a script that checks the length of the user's first name and last name. Both should be at least 2 characters long. If not, print 
#an error message.

first_name = input("Please type your first name.: ")
last_name = input("Please type your last name: ")
if len(first_name) <= 1 or len(last_name) <= 1:
    print("Not enough characters, please try again: ")
else:
    print(f"Hello, {first_name} {last_name}!")


#Task 2: Password Complexity Checker
#Create a function that checks the complexity of a user's password. The password must be at least 8 characters long, contain one 
#uppercase letter, one lowercase letter, and one number. If the password does not meet these criteria, print a message explaining the 
#complexity requirements.

password = input("Type your password: ")
result = []
if len(password) < 8:
    result.append("Password must be 8 characters long.")
if not any(x.isupper() for x in password):
    result.append("Password must have 1 uppercase letter.")
if not any(x.islower() for x in password):
    result.append("Password must have one lowercase letter.")
if not any(x.isdigit() for x in password):
    result.append("Password must contain one number.")
if not result:
    result.append("Valid password.")
for i in result:
    print(i)


#Task 3: Email Formatter
#Implement a script that ensures all user email addresses are in a standard format

user_email = last_name + "." + first_name + "@yahoo.com"
print(user_email)