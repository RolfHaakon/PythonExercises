"""
Make a function that encrypts a given input with these steps:

Input: "apple"

Step 1: Reverse the input: "elppa"

Step 2: Replace all vowels using the following chart:

a => 0
e => 1
o => 2
u => 3

# "1lpp0"

Step 3: Add "aca" to the end of the word: "1lpp0aca"

Output: "1lpp0aca"
"""

def encrypt(n):
    l = []
    n = "".join(reversed(n))
    for x in n:
        if x == "a":
            l.append("0")
        elif x == "e":
            l.append("1")
        elif x == "o":
            l.append("2")
        elif x == "u":
            l.append("3")
        else:
            l.append(x)
    l.append("aca")
    encrypted = ''.join(l)
    return encrypted





encrypt("apple")