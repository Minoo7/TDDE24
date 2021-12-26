#%%
"""
          Datortentamen i kursen TDDD64 Programmering i Python

                     tisdag 18 december kl 8-13

"""
"""-----------------------------------------------------------------------------
 Uppgift 1
-----------------------------------------------------------------------------"""

#*** Deluppgift 1A (2,5p) ***

def echo(string: str):
    lngth = len(string)
    return string + " " + string[round(lngth/2):] + " " + string[lngth - int(lngth/4):]

#*** Deluppgift 1B (2,5p) ***

def initials(name: str):
    new = ""
    for ini in name.split(" "):
        new += ini[0]
    return new

"""-----------------------------------------------------------------------------
 Uppgift 2
-----------------------------------------------------------------------------"""
#Klarade extremt fult xxx

def add(val1, val2):
    if "infinity" in (val1, val2):
        return "infinity"
    return val1 + val2

def add_list_i(seq: list): #fixd
    summ = 0
    for val in seq:
        summ = add(summ, val)
    return summ

def add_list_r(seq: list): #fixd
    if not seq:
        return 0
    return add(seq[0], add_list_r(seq[1:]))

"""-----------------------------------------------------------------------------
 Uppgift 3
-----------------------------------------------------------------------------"""

#*** Deluppgift 3A (3p) ***

def add_for_each(seq: list, fn: "function") -> int:
    if not seq:
        return 0
    if isinstance(seq, list):
        return fn(seq[0]) + add_for_each(seq[1:], fn)
    return fn(seq[0])

#*** Deluppgift 3B (2p) ***

def average_max(seq: list) -> int:
    return add_for_each(seq, lambda val: max(val))/len(seq)

"""-----------------------------------------------------------------------------
 Uppgift 4
-----------------------------------------------------------------------------"""

def makering(seq: list) -> "ring":
    """make_ring : list of elements -> ring"""
    return 
    pass

if __name__ == '__main__':
    assert echo("Korvbröd") == 'Korvbröd bröd öd'
    assert echo("Hejsan") == 'Hejsan san n'
    assert echo("Julgran") == 'Julgran ran n'

    assert initials("Kalle Anka") == "KA"
    assert initials("Per Anders Fogelström") == "PAF"

    assert add_list_i([1, 2, 3, 4]) == 10
    assert add_list_i([1, 2, 'infinity', 4]) == "infinity"

    assert add_for_each([1, 2, 3, 4], lambda x: x**2) == 30
    assert add_for_each([[1, 2, 3], [1], [1, 2, 3, 4]], lambda x: len(x)) == 8

    assert average_max([[12,13,15,11],[8,9,10],[5,7,6],[8,9,11,10],[3,5,5,2]]) == 9.6

    #
#%%
##abstrakt datatyp, högordning funktion etc..