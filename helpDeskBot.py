#Objective:
#The aim of this assignment is to create an interactive help desk bot that processes user queries and responds appropriately for a SaaS 
#application.

#Task 1: Command Parser
#Write a script that takes a user's text input and identifies if it contains one of the predefined commands (e.g., "help", "issue", 
#"contact support"). If a command is found, print a response related to the command.

#Task 2: Issue Categorizer
#If the user's input contains the word "issue", further categorize the issue based on keywords such as "login", "performance", "error", 
#etc. Print out the category of the issue for the support team.


commands = ['help', 'issue', 'contact support']
user_input = input("How can I assist you today? (help / issue / contact support): ").lower()
for command in commands:
    if command in user_input:
        if command == 'help':
            print("I will do my best to help you")
        elif command == 'issue':
            continue_issue = input("Please type the issue you are facing (login / performance / error / etc.): ")
            print(f"The user is having a {continue_issue} issue.")
        elif command == 'contact support':
            print("I will get you in contact with our support team.")


