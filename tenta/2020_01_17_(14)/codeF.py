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

if __name__ == '__main__':
    print(cartprod([{1,2}, {3,4,5}, {11,8}]))
