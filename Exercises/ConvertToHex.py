"""
Create a function that takes a strings characters as ASCII and returns each characters hexadecimal value as a string.
Examples

convert_to_hex("hello world") ➞ "68 65 6c 6c 6f 20 77 6f 72 6c 64"

convert_to_hex("Big Boi") ➞ "42 69 67 20 42 6f 69"

convert_to_hex("Marty Poppinson") ➞ "4d 61 72 74 79 20 50 6f 70 70 69 6e 73 6f 6e"

Notes
    Each byte must be seperated by a space.
    All alpha hex characters must be lowercase.
"""

def convert_to_hex(txt):
    st = ''
    for i in txt:
        x = hex((ord(i)))
        st += (''.join(x[-2:]))
    st = " ".join(st[i:i + 2] for i in range(0, len(st), 2))
    print(st)

convert_to_hex('hello world')
convert_to_hex('Big Boi')
convert_to_hex('Marty Poppinson')




"""
Alternative Solution

def convert_to_hex(txt):
	return ' '.join(hex(ord(i))[2:] for i in txt)
"""