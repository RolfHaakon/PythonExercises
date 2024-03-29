"""
Odd numbers like to hangout with odd numbers. Even numbers like to hangout with even numbers.

A spot is an insertion between two numbers in a list. Given a list of n integers in length, there are n-1 spots available.

For instance:

[3, 4, 9, 10, 1]  # List of 5 digits can also be thought of as...

[3, __ , 4, __ , 9, __, 10, __, 1]  # ...a list of 4 spots.

After a number is newly inserted into a spot, it's left neighbor is the number directly to the left of it and it's right neighbor is the number directly to the right of it.

For instance:

[3, 6, 4, 9, 10, 1]  # Left neighbor of 6 is 3, right neighbor of 6 is 4.

Odd numbers like having the following (left neighbor, right neighbor combinations): (odd, even), (even, odd), (odd, odd) .They dislike having both neighbors being even, or (even, even).

Similarly, even numbers like the following neighbor combinations: (even, odd), (odd, even), (even, even). They dislike having both neighbors being odd, or (odd, odd).

Given a list, calculate the number of liked spots.
Examples

available_spots([0, 4, 6, 8], 9) ➞ 0
# 9 likes NONE of the following spots: [0, __, 4], [4, __ , 6], [6, __, 8] b/c all of his neighbors are even.

available_spots([0, 4, 6, 8], 12) ➞ 3
# 12 likes ALL of the spots.

available_spots([4, 4, 4, 4, 5], 7) ➞ 1
# 7 dislikes every spot except the last one at: [4, __, 5].

available_spots([4, 4], 8) ➞ 1
"""


def available_spots(lst, num):
    ls = 0
    if num % 2 == 0:
        for i in range(len(lst) - 1):
            if lst[i] % 2 != 1 and lst[i + 1] % 2 != 1:
                ls += 1
        return ls
    else:
        for i in range(len(lst) - 1):
            if lst[i] % 2 != 0 and lst[i + 1] % 2 != 0:
                ls += 1
        return ls


print(available_spots([4, 3, 2, 6], 8))
print(available_spots([0, 4, 6, 8], 9))
print(available_spots([0, 4, 6, 8], 12))
print(available_spots([4, 4, 4, 4, 5], 7))
