from ..operation import element

def triangle_area(base, height):
    return element.mul(base, height) / 2
    
def rectangle_area(width, height):
    return element.mul(width, height)