import math

class Vec2D:

    def __init__(self,x:float,y:float):
        self.x = float(x)
        self.y = float(y)
   
    def length(self) -> float:
        return math.sqrt( self.x**2 + self.y**2 )

    def __add__(self, v):
        return Vec2D(self.x + v.x, self.y + v.y)
    
    def __sub__(self, v):
        return Vec2D(self.x - v.x, self.y - v.y)
    
    def __eq__(self, __value: object) -> bool:
        return __value.x == self.x and __value.y == self.y
    
    def __bool__(self):
        return not(self.x==0. and self.y==0.)

    def __str__(self) -> str:
        return "Vec.x = {}, Vec.y = {}".format(self.x,self.y)


v1 = Vec2D(2,3)
v2 = Vec2D(3,5)
v3 = v1 + v2
print(v3)
print(bool(Vec2D(0.,0.)))
print(bool(v1))
print(v1==Vec2D(2.,3.))
