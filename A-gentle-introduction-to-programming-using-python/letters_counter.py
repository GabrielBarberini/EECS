'''Exercise 8.7 from page 75 of thinkpython2, I'm anger to find different solutions for this, please if you have one please share it with me gabrielbarberinirc@gmail.com'''

def find(string, letter, index):
    count = 0
    while abs(index) <= len(string):
        if string[index] == letter:
            return index 

        count += 1

        if count >= len(string):
        #this solves the issue in case user inputs the last index first
            return 0
    
        index = index - 1
    #when index is out of range
    return 0

def notOneString(string):
    if len(string) == 1:
        return False 
    else:
        return True

def notAboveOneLetter(letter):
    if len(letter) == 1:
        return True

def count(string, letter):
    index = 0
    count = 0 
   
    if notOneString(string)\
    and notAboveOneLetter(letter): 
        while True:
            index = find(string, letter, index-1)
            if index == 0 : break
            count += 1
    elif letter == string:
        count += 1
   
    return count

#tests
print(count("banana", "a"))
print(count("aaaa", "a"))
print(count("aaa", "a"))
print(count("a", "a"))
#expected 3,4,3,1
