#1.The volume of a sphere with radius r is(4/3)* pie * r**2
#What is the volume of the sphere with radius 5
##Make sure the program that enters the radius from the keyboard and provide the answer in 2 decimal places.
radius=int(input("Enter the radius of the sphere:"))
pie=3.14
volume=(4/3)*pie*radius**2
print(f"The volume of the sphere with {radius} is :{volume:.2f}")

#2.Create a program to calculate the area of a triangle (1/2 *base * height).
# #Base and height should be entered using a keyboard
base=int(input("Enter the base of the triangle:"))
height= int(input("Enter the height of the triangle:"))
area=1/2*base*height
print(f"The area of the triangle is {area} ")

#3. Witi has asked you to automate a simple grading system.
#As a python student, write a program that is used to display;
#the student will be receiving grades basing on the mark scored in a subject.
# the grades are,
#90%-100% Grade is A
#80%-89% Grade is B
#70%-79% Grade is C
#60%-69% Grade is D
#50%-59% Grade is E#< 50% Fail
Student_mark=int(input("Enter the student mark"))
if Student_mark >=90 and Student_mark<=100:
    print("Grade is A")

elif Student_mark >=80 and Student_mark <=89:
    print("Grade is B")
elif Student_mark >=70 and Student_mark <=79:
    print("Grade is C")
elif Student_mark >=60 and Student_mark <=69:
    print("Grade is D")
else:
    print("Fail")

#4. WITI academy is proposing a SACCO to help students save their money.
#Design a platform that will do the following ,
#Deposit money
#Withdraw money
#check balance.
# Ensure if the student selects 1, money is deposited and the minimum deposit should be 1000
# If the student selects 2, money should be withdrawn and a minimum of withdraw is 500
# If the student selects 3, the account balance should be displayed .
# account_balance=0
# print("Welcome to WITI academy SACCO")
# print("1. Deposit money")
# print("2. Withdraw money")
# print("3. Check balance")
student_option = int(input("Enter the selection numbers (1,2,3):"))
if student_option ==1:
    deposit_name=int(input("Enter amount to be deposited:"))
    if deposit_amount < 1000:

        print("Minimum deposit is 1000")
    else:
        account_balance += deposit_amount
        print(f'Dear student you have deposited {deposit-amount:,} and your new account balance is {account_balance:,}')

    
elif student_option ==2:
    Withdraw_amount = int(input("Enter amount to be withdrawn:"))
    if account_balance ==0:
        print("Your account is 0")

    elif Withdraw_amount <500:
        print("Minimum withdraw amount should be more than 400")

    elif Withdraw_amount > account_balance:
        print(f'Withdraw failed insufficient account balance')
    
    else:
        account_balance -= Withdraw_amount
        print(f'Dear student, you have withdrawn {Withdraw_amount:,} and your new account balance is {account_balance:,}')
    
elif student_option ==3:
    print(f'Your account balance is {account_balance:,}')
else:
    print("You have entered a wrong choice!! please select 1,2 or3")
 
    



