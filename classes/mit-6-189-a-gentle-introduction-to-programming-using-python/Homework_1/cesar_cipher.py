'''implement a cesar cipher (ex: OPT 2)'''

phrase = input("Say so...\n")
shift = int(input("Key?\n"))
encoded_phrase = ''

# a-z = 97-122
# A-Z = 65-90

for letter in phrase:
    if ord(letter) >= 97\
    and (ord(letter) - 97) <= 25:
        cipher = ord(letter)+shift

        while cipher%122 > 0\
        and cipher%122 != cipher:
            cipher = ((96+cipher)%122)
        encoded_phrase += chr(cipher)

    elif ord(letter) >= 65\
    and (ord(letter) - 65) <= 25:
        cipher = ord(letter)+shift

        while cipher%90 > 0\
        and cipher%90 != cipher:
            cipher = ((64+cipher)%90)
        encoded_phrase += chr(cipher)

    else:
        encoded_phrase += letter
print (encoded_phrase)
