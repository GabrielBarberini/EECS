'''
Paying Debt Off In a Year

Problem 2

Now write a program that calculates the minimum fixed monthly payment needed in order pay
off a credit card balance within 12 months. We will not be dealing with a minimum monthly
payment rate.

Take as raw_input() the following floating point numbers:
1. the outstanding balance on the credit card
2. annual interest rate as a decimal 

Print out the fixed minimum monthly payment, number of months (at most 12 and possibly less
than 12) it takes to pay off the debt, and the balance (likely to be a negative number).
Assume that the interest is compounded monthly according to the balance at the start of the
month (before the payment for that month is made). The monthly payment must be a multiple of
$10 and is the same for all months. Notice that it is possible for the balance to become negative
using this payment scheme. 

In short:
Monthly interest rate = Annual interest rate / 12.0
Updated balance each month = Previous balance * (1 + Monthly interest rate) – Minimum
monthly payment '''

cardBalance = float(input("Enter the outstanding balance on your credit card: \n"))
cardInterest = float(input("Enter the annual credit card interest rate as a decimal: \n"))

def getResult(balance, interest):
    month = 1
    mmp = 10
    balanceBackup = balance 
    
    while True:
        if month == 13:
            balance = balanceBackup 
            mmp += 10
            month = 1

        balance = round((balance * (1 + interest/12) - mmp), 2)
        
        if balance <= 0:
            break
        else:
            month += 1 #after the break since the bill is paid in the next month

    print("\nRESULT")
    print("Monthly payment to pay off debt in 1 year: ", mmp)
    print("Number of months needed: ", month)     
    print("Balance: ", balance)

getResult(cardBalance, cardInterest)

# Problem Set 1b
# Name: Gabriel Barberini
# Collaborators: None
# Time Spent (min): 45:00
