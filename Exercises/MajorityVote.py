"""Create a function that returns the majority vote in a list.
A majority vote is an element that occurs > N/2 times in a list (where N is the length of the list)."""



def majority_vote(n):
    m_vote = None
    for i in n:
        if (n.count(i)) > (len(n)/2):
            m_vote = i
    return m_vote



print(majority_vote(["A","B","C","C"]))
print(majority_vote(["A","B","C","C","C"]))
