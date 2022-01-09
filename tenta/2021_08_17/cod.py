#%%

"""Uppgift 1"""
def tuplify(seq: list):
    if not seq:
        return []
    if len(seq) == 1:
        return [(seq[0],)]
    return [(seq[0], seq[-1])] + tuplify(seq[1:-1])

"""Uppgift 2"""
def split_lists(seq: list, sizes: str) -> list:
    calc_sizes = [int(x) for x in list(sizes)]
    summ = sum(calc_sizes)
    if summ != len(seq) or summ < 1:
       return (None, None)
    new_list = []
    i, j = 0, 0
    while True:
        sub_list = []
        for _ in range(calc_sizes[i]):
            sub_list.append(seq[j])
            j += 1
        new_list.append(sub_list)
        if len(calc_sizes) == 1+i:
            break
        i += 1
    return new_list

def split_lists_rec2(seq: list, sizes: str) -> list:
    if not seq or not sizes:
        return []
    if isinstance(sizes, str):
        converted = [int(x) for x in list(sizes)]
        if sum(converted) != len(seq): #kan man göra såhär?
            return (None, None)
        return [split_lists_rec2(seq, converted)]
    print("sizes: ", sizes)
    curr = sizes[0]
    if curr == 0:
        return ["h"]
    if curr == 1:
        return [seq[0]] + split_lists_rec2(seq[1:], [curr-1] + sizes[1:]) #+ [split_lists_rec(seq[1:], sizes[1:])]
    return [seq[0]] + split_lists_rec2(seq[1:], [curr-1] + sizes[1:]) + split_lists_rec2(seq[1:], sizes[1:])

def split_lists_rec1(seq: list, sizes: str) -> list:
    if not seq or not sizes:
        return []
    if isinstance(sizes, str):
        int_list = list(map(int, sizes))
        if sum(int_list) != len(seq):
            return (None, None)
        return split_lists_rec2(seq, int_list)
    def inner(inner_seq: list, amount: int):
        if not inner_seq or amount == 0:
            return []
        if amount == 1:
            return [inner_seq[0]]
        return [inner_seq[0]] + inner(inner_seq[1:], amount-1)
    length = sizes[0]
    return [inner(seq, length)] + split_lists_rec1(seq[length:], sizes[1:])

def split_lists_rec(seq: list, sizes: str) -> list:
    if not sizes:
        if len(seq) > 0:
            return (None, None)
        return []
    amount = int(sizes[0])
    rest = split_lists_rec(seq[amount:], sizes[1:])
    val_none = (None, None)
    if amount > len(seq):
        return val_none
    if rest == val_none:
        return val_none
    return [seq[:amount]] + rest

def alternating_jumps(seq1, seq2, maxjumps: int):
    "test 0"
    jumps = "de hopp som gjorts"
    index_1, index_2 = 0, 0
    while True:
        if 

if __name__ == '__main__':
    NEST = True
    if NEST:
        assert tuplify([1]) == [(1,)]
        assert tuplify(['hello', 'hello', 'world']) == [('hello', 'world'), ('hello',)]
        assert tuplify([1, 2, 3, 4]) == [(1, 4), (2, 3)]
        assert tuplify([1, 2, 3, 4, 5]) == [(1, 5), (2, 4), (3,)]
        assert tuplify([1, 2, 3, 4, 5, 6]) == [(1, 6), (2, 5), (3, 4)]
    
        assert split_lists([1, 2, 0, 4, 7, 6], "132") == [[1], [2, 0, 4], [7, 6]]
        assert split_lists([1, 2, 3, "x"], "12") == (None, None)
        assert split_lists([1, 2], "12") == (None, None)
        assert split_lists([1, 2, 3], "102") == [[1], [], [2, 3]]

        assert split_lists_rec([1, 2, 0, 4, 7, 6], "132") == [[1], [2, 0, 4], [7, 6]]
        assert split_lists_rec([1, 2, 3, "x"], "12") == (None, None)
        assert split_lists_rec([1, 2], "12") == (None, None)
        assert split_lists_rec([1, 2, 3], "102") == [[1], [], [2, 3]]
    pass

#%%
