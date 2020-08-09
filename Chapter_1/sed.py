"""Exercise 14.1. Write a function called sed that takes as arguments a pattern string, a replacement string, and two filenames; it should read the first file and write the contents into the second file (creating it if necessary). If the pattern string appears anywhere in the file, it should be replaced with the replacement string.
If an error occurs while opening, reading, writing or closing files, your program should catch the exception, print an error message, and exit. Solution: http: // thinkpython2. com/ code/ sed. py."""

def sed(pattern, replacement, searchfile='../mombo.txt', replacefile='mombo_replaced'):
    l = [] 
    try:
        fin = open(searchfile)
    except:
        print("Something went wrong while opening the search file")
        exit()
    for line in fin:
        try:
            l.append(line.strip())
        except:
            print("Something went wrong while reading the search file")
            exit()
    try:
        fin.close()
    except:
        print("Something went wrong while closing the search file")
        exit()
    try:
        fout = open(replacefile, 'w') 
    except:
        print("Something went wrong while opening the replace file")
        exit()
    for item in l:
        try:
            print(item.replace(pattern, replacement))
            replaced = item.replace(pattern, replacement)
            fout.write(replaced+"\n")
        except:
            print("Something went wrong while writing in replace file")
    try:
        fout.close()
    except:
        print("Something went wrong while closing the replace file")
        exit()

sed("The", "jooj")
