class Point:
    def __init__(self, cx, cy, desc='p'):
        self.x = cx
        self.y = cy
        self.descripcion = desc


def to_string(point):
    r = str(point.descripcion) + '(' + str(point.x) + ', ' + str(point.y) + ')'
    return r
