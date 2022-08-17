#%%

from match import *
from books import db

# Tar in: en databas(lista) och ett mönster(träd)
# Returnerar: de huvudelement i listan som matchar mönstret
def search(pattern, seq):
    """ Returnerar varje huvudelement i seq som matchar pattern """
    if not seq:
        return []
    if match(seq[0], pattern):
        return [seq[0]] + search(pattern, seq[1:])
    else:
        return search(pattern, seq[1:])

if __name__ == "__main__":
    assert search(['--', ['titel', ['&', '&']], '--'], db) == [[['forfattare', ['armen', 'asratian']], ['titel', ['diskret', 'matematik']], ['ar', 2012]]]
    assert search(['--', ['ar', 2042], '--'], db) == []
    assert search([['forfattare', ['&', 'zelle']], ['titel', ['--', 'python', '--']], ['ar', '&']], db) == [[['forfattare', ['john', 'zelle']],
    ['titel',
    ['python',
    'programming',
    'an',
    'introduction',
    'to',
    'computer',
    'science']],
    ['ar', 2010]],
    [['forfattare', ['john', 'zelle']],
    ['titel',
    ['data',
    'structures',
    'and',
    'algorithms',
    'using',
    'python',
    'and',
    'c++']],
    ['ar', 2009]]]
    
    assert search(['--'], [['hej', 'da'], ['da', 'hej']]) == [['hej', 'da'], ['da', 'hej']] #Vid '--' matchar båda huvudelementen
    assert search(['hej', '&', 'da'], db) == [] # Pattern doesnt match seq
    assert search([], db) == [] # If pattern is empty
    assert search([], []) == [] # If seq and pattern is empty
    assert search(['hej'], []) == [] # If seq is empty
    assert search(['--', '--', 'a', '&', 'b', '--'], ['a.b']) # Checking that all symbols work

#%%