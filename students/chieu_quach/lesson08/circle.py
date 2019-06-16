
import math

class Circle(object):
 
    def __init__(self, radius):

        self.radius = radius

    @property
    def get_diameter(self):
   # def get_diameter(self, value):
      
        return self.radius * 2   

    @get_diameter.setter
    def get_diameter(self, value):
        self.radius = value

    @classmethod
    def from_diameter(cls, radius):
        cls.radius = radius / 2
        
        return cls(cls.radius)
   
    def area(self):
        
        PI = 3.14
        return PI * self.radius * self.radius    
           
    def perimeter(self):
 
        return 2*math.pi*self.radius

          
    # Add two Cicle values
    def __add__(self, other):

        total_num = self.radius + other.radius
        return Circle(total_num)

    def __radd__(self):
        
        return self.__add__(other)

    # Multiply two Cicle values (use __mul__  and __rmul)
    def __mul__(self, other):

        total_num = self.radius * 3
        return Circle(total_num)

    def __rmul__(self):
        
        return self.__mul__(other)

    def __repr__(self):
        return repr(self.radius)

    def __str__(self):
        return str(self.radius)

    # Compare values of two circles

    # compare if c1 greater than c2
    def __gt__(self, other): 
        
        if self.radius > other.radius:
            return True
        else:
            return False

    # compare if c1 less than c2
    def __le__(self, other): 
        
        if self.radius < other.radius:
            return True
        else:
            return False

   # compare if c1 equal c2 
    def __eq__(self, other):
        
        if self.radius == other.radius:
            return True
        else:
            return False

    
    
    name = property(get_diameter, area)


class Sphere(Circle):
    
    def __init__(self, radius):
        super().__init__(self)
        self.radius = radius

    def __repr__(self):
        return repr(self.radius)

    def __str__(self):
        return str(self.radius)
    
    # Volume of Sphere
    def volume(self):   
        PI = 3.14
        return 4 * PI * self.radius * self.radius * self.radius /3

    try:
        # Surface area of Sphere
        def sphereArea(self):
        
            PI = 3.14
            self.area = 4 * PI * (self.radius * self.radius)
            return(self.area)
    except NotImplementedError as o:
        print ("Not Implemented ")
        print(o)
        
c1 =Circle(2)
c2 = Circle(4)
print( "Radius :", c1.radius)
print("Area of circle:",round(c1.area(),2))
c_total = c1 + c2
#print (c1.name)
print ("Diameter area of cicle ", c1.get_diameter)
c1.get_diameter = (2)
print ("New Diameter of circle ", c1.get_diameter)

c3 = Circle(4)

print ("total circle ", c_total)

multi_circles = c2 * 3
print ("Multi. circle ", multi_circles)

c = Circle.from_diameter(8)
print ("Set Diameter ", int(c.get_diameter))
print ("Set Radius ", int(c.radius))
 
print("Perimeter of circle:",round(c1.perimeter(),2))

print ("Repr Method ", repr(Circle(c1)))
print ("Str Method ",  str(Circle(c1)))

# compare and print outputs of two values
print ("c1 > c2 ", bool(c1 > c2))
print ("c1 < c2 ", bool(c1 < c2))
print ("c1 == c2 ", bool(c1 == c2))
print ("c2 == c3 ", bool(c2 == c3))

circle = Circle(10)
print ("circle ", circle)

s1 = Sphere(10)
print ("Sphere Radius ", s1.radius)
print ("Repr Method ", repr(Sphere(s1)))
print ("Str Method ",  str(Sphere(s1)))
print ("Volume of Sphere ", round(s1.volume(),2))
print ("Surface area of Sphere ", round(s1.sphereArea(),2))







