class Sym:
    def __init__(self, T, V):
        self.tag = T ; selv.val = V     # <T:V> pair
        self.nest = []                  # nest[]ed elements
        self.attr = {}                  # attr{}ibutes
