# conditional statements: those sttements that are exeuted based upon the conditions. 

# if statements
# if else statements
# if elif else statements
# 4.nested conditionals:-

# 1.if statements:

# syntax:
# if condition:
#     statements
#     statements
#     statements

# a=60
# print(a, "is greater than 50")

# a=60
# if a>50:
#     print(a, "is greater than 50")
    # print(str(a)+ " is greater than 50")

# a=45
# if a>50:
#     print(a, "is greater than 50")

# a=int(input("enter a value:"))
# if a>50:
#     print(str(a)+" is greater than 50")
# print(str(a)+" is less than 50")

# 2. if-else statement:

# syntax:-
# if condition:
#     statements
# else:
#     satements

# a=int(input("enter a value:"))
# if a>50:
#     print(str(a)+" is greater than 50")
# else:
#     print(str(a)+" is less than 50")

# 3. if-elif-else conditionals: 
# note: before declaring elif condition if condition should be declared mandatory.

# syntax: 
# if condition: 
#     statements
# elif condition:
#     statements
# elif condition:
#     statements
# else:
#     statements

# marks=int(input("enter yur percentage:"))
# if marks>=70:
#     print("you got distinction!")
# elif marks >= 60 and marks<70:
#     print("you got first class")
# elif marks>=50 and marks<60:
#     print("you got second class")
# elif marks>=40 and marks<50:
#     print("you got third class")
# else:
#     print("you are just passed")

# 4.nested conditionals:-

# if condition:
#     if condition:
#         statements
#     else:
#         statements
# else:
#     statements

# a=int(input("enter a value:"))
# if a>0:
#     if a%5==0:
#         print(a,"is a multiple of 5")
#     else:
#         print(a,"is not a multiple of 5")
# else:
#     print("you entered negetive value")

# task: 
# step1 -  ask of pin number
# step2 - check pin number if correct
#     step2.1 - ask for account type
#     step2.2 - check if account type matches
#         step 2.2.1 - ask for amount to be withdrawn
#         step 2.2.2 - aprint statement that amount is debited from the account
#     step 2.3 - print statement mentioning account type not matching
# step3 - pprint statement mentioning pin is incorrect

# pin=int(input("enter your pin:"))
# if pin==1234:
#     account_type=input("enter the type of account:")    
#     if account_type=="savings":
#         amount=float(input("enter the amount to be withdrawn:"))
#         print(amount," is debited from your account")
#     else:
#         print("account type doesn't match")
# else:
#     print("incorrect pin")