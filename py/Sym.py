class Sym:
    def __init__(self, T, V):
        self.tag = T ; self.val = V         # <T:V> pair
        self.nest = []                      # nest[]ed elements
        self.attr = {}                      # attr{}ibutes
    def __repr__(self): return self.head()
    def head(self):
        '<T:V> header'
        return '<%s:%s>' % (self.tag, self.val)

def test_hello():
    assert 'hello' != 'world'

def test_symbol_simplest_dump():
    assert '%s' % Sym('sym', 'X') == '<sym:X>'
