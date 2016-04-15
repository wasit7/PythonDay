class Obj:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y
    
    def update(self, _x, _y):
        self.x += _x
        self.y += _y  
        
    def __str__(self):
        return "x:%d, y:%d"%(self.x,self.y)

class Obj2:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y
    
    def update(self, _x, _y):
        self.x += _x
        self.y += _y  
        
    def __str__(self):
        return "x:%d, y:%d"%(self.x,self.y)

def foo(x):
	return x*x;