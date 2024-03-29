"""
Create a function that takes a list of numbers or strings and returns a list with the items from the original list stored into sublists. Items of the same value should be in the same sublist.
Examples

advanced_sort([2, 1, 2, 1]) ➞ [[2, 2], [1, 1]]
advanced_sort([5, 4, 5, 5, 4, 3]) ➞ [[5, 5, 5], [4, 4], [3]]
advanced_sort(["b", "a", "b", "a", "c"]) ➞ [["b", "b"], ["a", "a"], ["c"]]

Notes

The sublists should be returned in the order of each element's first appearance in the given list.
"""


def advanced_sort(lst):
    lists = [[] for i in range(len(set(lst)))]
    for num, i in enumerate(sorted(set(lst), key=lst.index)):
        a = lst.count(i)
        for k in range(a):
            lists[num].append(i)
    return lists




advanced_sort([80,80,4,60,60,3])
advanced_sort(['c','c','b','c','b',1,1])
advanced_sort([1234, 1235, 1234, 1235, 1236, 1235])
advanced_sort(['1234', '1235', '1234', '1235', '1236', '1235'])


"""
Alternative solution

def advanced_sort(lst):
	return [[i] * lst.count(i) for i in sorted(set(lst), key=lst.index)]
"""
