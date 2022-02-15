"""
Paying the Minimum
Problem 1

Write a program to calculate the credit card balance after one year if a person only pays the
minimum monthly payment required by the credit card company each month.
Use raw_input() to ask for the following three floating point numbers:
1. the outstanding balance on the credit card
2. annual interest rate
3. minimum monthly payment rate
For each month, print the minimum monthly payment, remaining balance, principle paid in the
format shown in the test cases below. All numbers should be rounded to the nearest penny.
Finally, print the result, which should include the total amount paid that year and the remaining
balance. 

Minimum monthly payment = Minimum monthly payment rate x Balance
(Minimum monthly payment gets split into interest paid and principal paid)

Interest Paid = Annual interest rate / 12 months x Balance

Principal paid = Minimum monthly payment – Interest paid

Remaining balance = Balance – Principal paid
"""

cardBalance = float(input("Enter the outstanding balance on your credit card: \n"))
cardInterest = float(input("Enter the annual credit card interest rate as a decimal: \n"))
cardMinPay = float(input("Enter the minimum monthly payment rate as a decimal: \n"))

#optional
months = int(input("Enter the number of months to be calculated: \n"))

def getResult(balance, interest, minimum_payment, months):
    total_paid = 0

    for m in range(months):
        mmp = round(minimum_payment * balance, 2)
        ip = round((interest/12) * balance, 2)
        pp = round(mmp - ip, 2)
        balance = round(balance - pp, 2)
        total_paid += round(pp + ip, 2)
        print("\nMONTH", (m+1))
        print("Minimum monthly payment: ", round(mmp,2))
        print("Remaining balance: ", round(balance, 2))
        print("Principal paid: ", round(pp, 2)) 

    print("\nRESULT")
    print("Total amount paid: ", round(total_paid, 2))
    print("Remaining balance: ", round(balance, 2))

getResult(cardBalance, cardInterest, cardMinPay, months)

# Problem Set 1a
# Name: Gabriel Barberini
# Collaborators: None
# Time Spent (min): 60:00
