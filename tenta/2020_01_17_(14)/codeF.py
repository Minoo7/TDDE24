"""Uppgift 5"""

def cartprod1(sets: list):
    """Tar en lista av n >= 2 godtyckliga mängder och returnerar
    kartesiska produkten av alla dessa mängder, vilket alltså är en mängd av tupler"""
    if not sets:
        return {}

    
    #print('first: ', sets[0])
    
    #first = set([sets[0].pop()])
    #print('first: ', first)
    rest = cartprod(sets[1:])
    
    without_first = rest

    first = set([sets[0].copy().pop()])
    print('first: ', first)
    test = set()
    for ele in rest:
        add = first.union(set([ele]))
        test = test.union(add)
        print("ele", ele)
    print('test: ', test)
    #with_first = {[first.union(ss) for ss in rest]}
    #print('with_first: ', with_first)
    print('without_first: ', without_first)

    #return {1,2}
    return test.union(without_first)
    #return with_first.union(without_first)

    #first = sets[0].union(cartprod(sets[1:]))
    #new_list = []
    #for set in sets:
    #    for ele in set:
    #        set(ele).union()
    #print('first: ', first)

    
    #return calc
    #return first

def cartprod5(old_sets):
    """1"""
    new_list = [list(sset) for sset in old_sets]
    def calc(sets, brack):
        """"calc"""
        if not sets or sets == [[]]:
            return []
        print('sets: ', sets)
        first = sets[0]
        rest = sets[1:]
        if isinstance(first, list) and len(first) > 1:
            #if len(first) > 1:
            #    [calc([first[0]] + rest, False)] + calc([first[1:]] + rest, False)
            print('first: ', first)
            print('rest: ', rest)
            #print([first[1:]] + rest)
            if isinstance(rest, list) and len(rest) > 0 and isinstance(rest[0], list):
                rr = calc(rest, True)
                print(f"rr: {rr}")
                fon = [first[0]] +rr
                print(f"rr: {rr}")
                path = [[first[0]]] + [rest[0][1:]] + rest[1:]
                #print('path: ', path)
                if brack:
                    ret = [first[0]] + rr + calc(path, False)
                    print(f"return: {ret}")
                    return ret
                else:
                    ret = [[first[0]] + rr] + calc(path, False)
                    print(f"return: {ret}")
                    return ret
            print(f"path!!: {[[first[0]]] + [rest[1:]]}")
            ret = [first[0]] + calc(rest, True) + calc([[first[0]]] + [rest[1:]], False)
            print(f"return: {ret}")
            return ret
        ret = first
        print(f"return: {ret}")
        return ret # + calc(rest, False) #+ ['hej']
    return calc(new_list, False)

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
