class Point:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def add_point(self, point):
        return Point(self.x + point.x, self.y + point.y, self.z + point.z)

    def subtract_point(self, point):
        return Point(self.x - point.x, self.y - point.y, self.z - point.z)

    def get_distance_squared(self, point):
        dx = self.x - point.x
        dy = self.y - point.y
        return (dx * dx) + (dy * dy)

    def same_as(self, point):
        return self.x == point.x and self.y == point.y