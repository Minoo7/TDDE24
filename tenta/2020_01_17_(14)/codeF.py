"""Uppgift 5"""

def cartprod(sets): #funkar inte för alla
    """1"""
    if not sets:
        return []
    if isinstance(sets[0], set):
        converted = [list(sset) for sset in sets]
        result = []
        for i in converted[0]:
            result += cartprod([[i]] + converted[1:])
        return set(result)
    first = sets[0]
    rest = sets[1:]
    if isinstance(first, list) and len(sets) > 1:
        return [tuple([first[0]] + [sub_set] + cartprod(rest[1:])) for sub_set in rest[0]]
    return first

#Uppgift 1
def divide_i1(n, seq):
    """Delar upp element i en lista i totalt n givna listor"""
    lst = []
    #amount = len(seq) / n
    amount = 2
    count = 0
    sub_lst = []
    for ele in enumerate(seq):
        sub_lst.append(ele[1])
        indx = ele[0]+1
        if indx - count == amount:
            lst.append(sub_lst)
            sub_lst = []
            count = indx
    return lst

def divide_i(n, seq):
    lst = []
    for i in range(len(n)):
        #for ele in range()
        pass
    pass

if __name__ == '__main__':
    #print(cartprod([{1,2}, {3,4,5}, {11,8}]))
    print(divide_i(3, [1, 2, 3, 4, 5]))

