import itertools

class Shape(object):
    def __init__(self, index, symbol, color, number, shading):
        self.index = index
        self.symbol = symbol
        self.color = color
        self.number = number
        self.shading = shading
        
def check_combo(combo):
    symbol_set = set(i.symbol for i in combo)
    color_set = set(i.color for i in combo)
    number_set = set(i.number for i in combo)
    shading_set = set(i.shading for i in combo)

    for set_to_test in (symbol_set, color_set, number_set, shading_set):
        if len(set_to_test) != len(combo) and len(set_to_test) != 1:
            return False

    return True
        
shapes = []
shapes.append(Shape((0,0),'squiggle', 'red', 1, 'full'))
shapes.append(Shape((0,1),'squiggle', 'red', 2, 'empty'))
shapes.append(Shape((0,2),'triangle', 'red', 3, 'full'))
shapes.append(Shape((1,0),'oval', 'red', 2, 'full'))
shapes.append(Shape((1,1),'squiggle', 'red', 3, 'dash'))
shapes.append(Shape((1,2),'oval', 'red', 1, 'empty'))
shapes.append(Shape((2,0),'oval', 'red', 1, 'full'))
shapes.append(Shape((2,1),'triangle', 'red', 2, 'empty'))
shapes.append(Shape((2,2),'triangle', 'red', 2, 'dash'))

combos = itertools.combinations(shapes, 3)
for combo in combos:
    if check_combo(combo):
        for elem in combo:
            print elem.index
        print
