'''
Given two roman numbers, print their sum in roman notation.

* Numbers from 1 to 100
* Tokens I V X L C

Recommendation: 
Get two roman numbers, convert them to integers, perform the sum and then convert the sum back to roman.
In the end of the file there is a table with roman examples from 1 to 100
'''

roman_to_int_tokens = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100
        }

int_to_roman_tokens = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C"
        }

def roman_to_int(rom, tokens):
    '''Assumes tokens.keys are chars and tokens.values are ints'''
    temp = 0

    for i in range(len(rom)):
        if i-1 >= 0 and tokens.get(rom[i]) > tokens.get(rom[i-1]):
        #if its not the first roman number and the next one is greater than the current, sum current minus the previous one
            temp += tokens.get(rom[i]) - 2*tokens.get(rom[i-1])
        else:
            temp += tokens.get(rom[i])
    return temp

def sumUp(x, y):
    return x + y

def int_to_roman(num, tokens):
    ''' Assumes tokens.keys are int and tokens.values are char'''
    keys = list(tokens.keys())
    keys.sort()
    values = []
    
    for k in keys:
        values.append(tokens.get(k))

    i = 1 
    roman = "" 

    while num > 0:
        if num // keys[-i] > 0 and num // keys[-i] <= 3:
            roman += values[-i] * (num // keys[-i])
            num -= keys[-i] * (num // keys[-i])

        elif num // keys[-i] > 3:
            roman += values[-i] + values[1-i]
            num -= keys[-i]+keys[1-i]
        i += 1

    return roman

print(int_to_roman(sumUp(roman_to_int("VIII", roman_to_int_tokens), roman_to_int("XIV", roman_to_int_tokens)), tokens=int_to_roman_tokens))
        
'''
1	I	1
2	II	1+1
3	III	1+1+1
4	IV	5-1
5	V	5
6	VI	5+1
7	VII	5+1+1
8	VIII	5+1+1+1
9	IX	10-1
10	X	10
11	XI	10+1
12	XII	10+1+1
13	XIII	10+1+1+1
14	XIV	10-1+5
15	XV	10+5
16	XVI	10+5+1
17	XVII	10+5+1+1
18	XVIII	10+5+1+1+1
19	XIX	10-1+10
20	XX	10+10
21	XXI	10+10+1
22	XXII	10+10+1+1
23	XXIII	10+10+1+1+1
24	XXIV	10+10-1+5
25	XXV	10+10+5
26	XXVI	10+10+5+1
27	XXVII	10+10+5+1+1
28	XXVIII	10+10+5+1+1+1
29	XXIX	10+10-1+10
30	XXX	10+10+10
31	XXXI	10+10+10+1
32	XXXII	10+10+10+1+1
33	XXXIII	10+10+10+1+1+1
34	XXXIV	10+10+10-1+5
35	XXXV	10+10+10+5
36	XXXVI	10+10+10+5+1
37	XXXVII	10+10+10+5+1+1
38	XXXVIII	10+10+10+5+1+1+1
39	XXXIX	10+10+10-1+10
40	XL	    50-10
41	XLI	    50-10+1
42	XLII	50-10+1+1
43	XLIII	50-10+1+1+1
44	XLIV	50-10-1+5
45	XLV	    50-10+5
46	XLVI	50-10+5+1
47	XLVII	50-10+5+5+1
48	XLVIII	50-10+5+1+1+1
49	XLIX	50-10-1+10
50	L	    50
51	LI	    50+1
52	LII	    50+1+1
53	LIII	50+1+1+1
54	LIV	    50-1+5
55	LV	    50+5
56	LVI	    50+5+1
57	LVII	50+5+1+1
58	LVIII	50+5+1+1+1
59	LIX	    50-1+10
60	LX	    50+10
61	LXI	    50+10+1
62	LXII	50+10+1+1
63	LXIII	50+10+1+1+1
64	LXIV	50+10-1+5
65	LXV	    50+10+5
66	LXVI	50+10+5+1
67	LXVII	50+10+5+1+1
68	LXVIII	50+10+5+1+1+1
69	LXIX	50+10-1+10
70	LXX	    50+10+10
71	LXXI	50+10+10+1
72	LXXII	50+10+10+1+1
73	LXXIII	50+10+10+1+1+1
74	LXXIV	50+10+10-1+5
75	LXXV	50+10+10+5
76	LXXVI	50+10+10+5+1
77	LXXVII	50+10+10+5+1+1
78	LXXVIII	50+10+10+5+1+1+1
79	LXXIX	50+10+10-1+5
80	LXXX	50+10+10+10
81	LXXXI	50+10+10+10+1
82	LXXXII	50+10+10+10+1+1
83	LXXXIII	50+10+10+10+1+1+1
84	LXXXIV	50+10+10+10-1+5
85	LXXXV	50+10+10+10+5
86	LXXXVI	50+10+10+10+5+1
87	LXXXVII	50+10+10+10+5+1+1
88	LXXXVIII	50+10+10+10+5+1+1+1
89	LXXXIX	50+10+10+10-1+10
90	XC 100-10
91	XCI	100-10+1
92	XCII	100-10+1+1
93	XCIII	100-10+1+1+1
94	XCIV	100-10-1+5
95	XCV	100-10+5
96	XCVI	100-10+5+1
97	XCVII	100-10+5+1+1
98	XCVIII	100-10+5+1+1+1
99	XCIX	100-10-1+10
100	C	100
'''
