import math
class Point2D(object):
    """Point du plan cartÃ©sien

    >>> p1 = Point2D(3, 4)
    >>> p1.x
    3
    >>> p1.y
    4
    >>> print(p1)
    Point2D(3,4)
    >>> p2 = Point2D()
    >>> p2.x
    0
    >>> p2.y
    0
    >>> print(p2)
    Point2D(0,0)
    >>> p1.move(1,1)
    >>> p1.x
    4
    >>> p1.y
    5
    >>> print(p1)
    Point2D(4,5)
    >>> p1.distance(p2)
    6.4031242374328485
    """
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def move(self,x,y):
        self.x += x
        self.y += y

    def __str__(self):
        return f"Point2D({self.x},{self.y})"

    def distance(self, other):
        dx=self.x-other.x
        dy=self.y-other.y
        return math.hypot(dx,dy)    
        
def main():
    p1=Point2D(2,3)
    p2=Point2D(1,1)
    p1.move(1,1)
    print(p1.distance(p2))
    pass

if __name__ == "__main__":
        main()