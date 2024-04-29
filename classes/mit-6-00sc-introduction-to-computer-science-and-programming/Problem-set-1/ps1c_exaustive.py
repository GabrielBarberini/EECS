'''
Problem 3
Write a program that uses these bounds and bisection search (for more info check out the
Wikipedia page here) to find the smallest monthly payment to the cent (no more multiples of
$10) such that we can pay off the debt within a year. Try it out with large inputs, and notice how
fast it is. Produce the output in the same format as you did in problem 2.

Exaustive Enumeration Solution
'''

cardBalance = float(input("Enter the outstanding balance on your credit card: \n"))
cardInterest = float(input("Enter the annual credit card interest rate as a decimal: \n"))

def getResult(balance, interest):
    month = 1
    lower_mmp = balance / 12.0 
    higher_mmp = (balance * (1.0 + (interest / 12.0)) ** 12.0) / 12.0
    balance_lower = balance_higher = balance
    balanceTemp = balance
    
    while True:
        if month == 13:
            balance_lower = balance_higher = balanceTemp
            lower_mmp += 0.01
            higher_mmp -= 0.01
            month = 1

        balance_lower = (balance_lower * (1.0 + interest/12.0) - lower_mmp) #move left
        balance_higher = (balance_higher * (1.0 + interest/12.0) - higher_mmp) #move right

        if balance_higher <= 0:
            balance = round(balance_higher, 2)
            mmp = round(higher_mmp, 2)
        
        if balance_lower <= 0:
            balance = round(balance_lower, 2)
            mmp = round(lower_mmp, 2)
            break

        elif lower_mmp == higher_mmp and month == 12:
            break

        else:
            month += 1 #after the breaks since the bill is paid in the next month

    print("\nRESULT")
    print("Monthly payment to pay off debt in 1 year: ", mmp)
    print("Number of months needed: ", month)     
    print("Balance: ", balance)

getResult(cardBalance, cardInterest)

# Problem Set 1c
# Name: Gabriel Barberini
# Collaborators: None
# Time Spent (min): 180
