import numpy as np

class Shape(object):
    def __init__(self, name: str = "Shape"):
        self.name = name
    def generate_random_point(self):
        raise NotImplementedError


class Sphere(Shape):
    def __init__(self, radius: float = 1.0, center = np.array([0,0,0]) , name: str = "Sphere"):
        super().__init__(name)
        self.radius = radius
        self.center = center
        self.volume = 4/3 * np.pi * self.radius**3
    def generate_random_points(self, n):
        # generate n random points within the tumor
        # the points are generated in a cube of side 2*radius
        # then the points outside the tumor are discarded
        # initialize the points array as a list of 3D points
        points = np.array([[0, 0, 0]])
        while points.shape[0] <= n+2:
            points_new = np.random.uniform(-self.radius, self.radius, (n, 3))
            points_new = points_new + self.center
            points_new = points_new[np.linalg.norm(points_new - self.center, axis=1) < self.radius]
            points = np.concatenate((points, points_new))
        # make sure the number of points is n
        points = points[1:]
        points = points[:n]
        return points