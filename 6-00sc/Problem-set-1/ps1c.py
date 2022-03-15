'''
Problem 3
Write a program that uses these bounds and bisection search (for more info check out the
Wikipedia page here) to find the smallest monthly payment to the cent (no more multiples of
$10) such that we can pay off the debt within a year. Try it out with large inputs, and notice how
fast it is. Produce the output in the same format as you did in problem 2.

Exaustive Enumeration Solution

Not the elegant solution I was expecting, but... 
'''

cardBalance = float(input("Enter the outstanding balance on your credit card: \n"))
cardInterest = float(input("Enter the annual credit card interest rate as a decimal: \n"))

#Monthly payment lower bound = Balance / 12.0
lower_bound = cardBalance / 12.0

#Monthly payment upper bound = (Balance * (1 + (Annual interest rate / 12.0)) ** 12.0) / 12.0
upper_bound = (cardBalance * (1 + (cardInterest / 12.0)) ** 12.0) / 12.0

def showResult(result):
    print("\nRESULT")
    print("Monthly payment to pay off debt in 1 year: ", result[0])
    print("Number of months needed: ", result[1])     
    print("Balance: ", result[2])

def getResult(balance, interest, minima, maxima):
    month = 1
    balanceReset = balance
    mid = (maxima - minima) / 2
    freq = 0

    while True:
        if month == 13:
            freq += 1
            if abs(freq) > 1000: 
                return [round(mid, 2), month-1, round(balance, 2)]
            balance = balanceReset
            month = 1
            minima = mid
            mid += ( maxima - mid ) / 2.0 #go right

        balance = (balance * (1 + interest/12.0) - mid)
        
        if balance <= 0:
            freq -= 1
            if abs(freq) > 1000: 
                return [round(mid, 2), month, round(balance, 2)]
            balance = balanceReset
            month = 1
            maxima = mid
            mid -= ( mid - minima ) / 2.0 #go left
        else:
            month += 1 #after the break since the bill is paid in the next month
    
showResult( getResult(cardBalance, cardInterest, lower_bound, upper_bound) )

# Problem Set 1c
# Name: Gabriel Barberini
# Collaborators: None
# Time Spent (min): 180
