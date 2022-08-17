#%%
import unittest

def is_empty_tree(tree):
    return isinstance(tree, list) and not tree

def is_leaf(tree):
    return isinstance(tree, int)
	
def left_subtree(tree):
    return tree[0]

def right_subtree(tree):
    return tree[2]

def key(tree): # Från Labb4
    """ Returnerar trädets nyckel """
    return tree[1]

def is_node(tree):
    return isinstance(tree, list)

def empty_tree_fn():
    return 0

def leaf_fn(key):
    return key**2

def inner_node_fn(key, left_value, right_value):
    return key + left_value

#---i---

def traverse(tree, left_fn, middle_fn, right_fn):
    """ Går systematiskt igenom ett giltigt binärt sökträd """
    if not tree:
        return right_fn() #empty_tree_fn()
    if is_leaf(tree):
        return middle_fn(tree) #leaf_fn(tree)
    if is_node(tree):
        left = traverse(left_subtree(tree), left_fn, middle_fn, right_fn)
        right = traverse(right_subtree(tree), left_fn, middle_fn, right_fn)
        return left_fn(key(tree), left, right)

#---ii---

def contains_key(search_key, tree):
    """ Söker igenom ett träd efter en key """
    def left_fn(key, left, right):
        if search_key == key or left or right:
            return True
        return False
    def middle_fn(tree):
        if tree == search_key:
            return True
        return False
    def right_fn():
        return False

    return traverse(tree, left_fn, middle_fn, right_fn)

#---iii---
def tree_size(tree):
    """ Beräknar trädets storlek(totala antalet löv och inre noder) """
    def left_fn(key, left, right):
        return 1 + left + right
    def middle_fn(tree):
        return 1
    def right_fn():
        return 0
    
    return traverse(tree, left_fn, middle_fn, right_fn)

#---iv---
def tree_depth(tree):
    """ Beräknar trädets djup(antal noder i den längsta vägen från roten till ett löv) """
    def left_fn(key, left, right):
        return 1 + max(left, right)
    def middle_fn(tree):
        return 1
    def right_fn():
        return 0
        
    return traverse(tree, left_fn, middle_fn, right_fn)

if __name__ == '__main__':
    #---i---
    assert traverse([6, 7, 8], inner_node_fn, leaf_fn, empty_tree_fn) == 43
    assert traverse([[2, 5, 1], 7, 8], inner_node_fn, leaf_fn, empty_tree_fn) == 16
    assert traverse([[], 7, 8], inner_node_fn, leaf_fn, empty_tree_fn) == 7
    assert traverse(5, inner_node_fn, leaf_fn, empty_tree_fn) == 25 #Trädet är ett löv
    assert traverse([6, 7, []], inner_node_fn, leaf_fn, empty_tree_fn) == 43 #Räknar inte med höger subträd
    assert traverse([], inner_node_fn, leaf_fn, empty_tree_fn) == 0 #Tomt träd ger 0
    #---ii---
    assert contains_key(6, [6, 7, 8]) == True
    assert contains_key(2, [6, 7, [[2, 3, 4], 0, []]]) == True
    assert contains_key(2, [[], 1, 5]) == False
    assert contains_key(2, []) == False #En tom lista kan inte innehålla en key
    assert contains_key(2, [[2, 3, 4], 3, []]) == True #Kan leta i vänster subträd
    assert contains_key(2, [[], 3, [3, 5, 2]]) == True #Kan leta i höger subträd
    #---iii---
    assert tree_size([2, 7, []]) == 2
    assert tree_size([]) == 0
    assert tree_size([[1, 2, []], 4, [[], 5, 6]]) == 5
    assert tree_size([[1, 2, 3], 5, []]) == 4 #Kan räkna med vänster subträd
    assert tree_size([[], 3, [2, 3, 4]]) == 4 #kan räkna med höger subträd
    assert tree_size([[], 6, []]) == 1 #Ifall båda subträden är tomma
    #---iv---
    assert tree_depth(9) == 1
    assert tree_depth([1, 5, [10, 7, 14]]) == 3
    assert tree_depth([]) == 0 #Tom lista har ingen depth
    assert tree_depth([3, 5, 6]) == 2 #Simpelt träd
    assert tree_depth([1, 3, [3, 5, [6, 4, [5, 5, 6]]]]) == 5 #En djup lista
    
#%%