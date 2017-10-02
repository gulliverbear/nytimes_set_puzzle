import itertools

class Shape(object):
    def __init__(self, index, symbol, color, number, shading):
        self.index = index
        self.symbol = symbol
        self.color = color
        self.number = number
        self.shading = shading
        
def check_combo(combo):
   # to do
        
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

# to do - solve the combinations