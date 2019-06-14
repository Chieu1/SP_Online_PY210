#!/usr/bin/env python

import pytest
from circle import Circle, Sphere

def test_default_initial_radius():
    circle = Circle(2)
    assert circle.radius == 2
    
def test_diameter():
    circle = Circle(2)
    assert circle.get_diameter == 4

def test_area():
    circle = Circle(2)
    assert round(circle.area(),2) == 12.56

def test_str():
    c1 = Circle(2)
    assert str(c1) == '2'

def test_repr():
    c1 = Circle(2)
    assert repr(c1) == '2'

def test_add():
    c  = Circle(2)
    c2 = Circle(3)
    assert repr(c + c2) == '5'

def test_mult():
    c = Circle(2)
    num = 3
    assert repr(c * num) == '6'

def test_gt():
    c = Circle(2)
    c2 = Circle(4)
    assert repr(c > c2) == 'False'

def test_le():
    c  = Circle(2)
    c2 = Circle(4)
    assert repr(c < c2) == 'True'

def test_eq():
    c  = Circle(2)
    c2 = Circle(4)
    assert repr(c == c2) == 'False'

def test_eq():
    c2 = Circle(4)
    c3 = Circle(4)
    assert repr(c2 == c3) == 'True'

def test_default_initial_radius():
    sphere = Sphere(10)
    assert sphere.radius == 10

def test_repr_sphere():
    c1 = Sphere(10)
    assert repr(c1) == '10'

def test_str_sphere():
    c1 = Sphere(10)
    assert str(10) == '10'

def test_volume():
    s1 = Sphere(10)
    assert round(s1.volume(), 2) == 4186.67
    
def test_sphereArea():
    s1 = Sphere(10)
    assert round(s1.sphereArea(), 2) == 1256.0


    

    
