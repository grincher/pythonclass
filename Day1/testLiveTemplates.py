import math

class Point:
    """
    Point does wonderful things
    Represents a point in 2D geometric space
    """
    def __init__(self, x = 0, y = 0):
        """
        Initialize the position of a new point.
        if they are not specified, the point defaults to the origin
        :param x: x coordinate (default 0)
        :param y: y coordinate (default 0)
        """
        self.x = x
        self.y = y

    def reset(self):
        """
        Reset point to the origin in 2D space
        :return: None
        """
        self.move(0,0)

    def move(self, x, y):
        """
        Move a point to a new location in 2D space
        :param x: New x value
        :param y: New y value
        :return: None
        """
        self.x = x
        self.y = y

    def print(self, name):
        """
        Display the point values
        :param name: point's name (not currently stored in class)
        :return: None
        """
        print(name, "is (", self.x, ",", self.y, ")")


    def distance(self, otherPoint):
        """
        Compute the distance between two Points using the Pythagorean Theorem
        :param otherPoint: The Other Point
        :return: Distance between self and otherPoint (float)
        """
        return(math.sqrt(((otherPoint.x - self.x)**2) + ((otherPoint.y - self.y)**2)))


def main():
    """
    Test code for Point class
    :return: None
    """
    p1 = Point()
    p1.print("p1")
    p2 = Point(5,8)
    p2.print("p2")
    p2.reset()
    p2.print("p2 reset")
    p2.move(8,10)
    p2.print("p2 moved")
    print("distance between p1 and p2 is:", p1.distance(p2))
    print("distance between p2 and p1 is:", p2.distance(p1))

    # Test tool (assert)
    # program will exit if False (or zero, empty, None)
    assert(p1.distance(p2) == p2.distance(p1))


if __name__ == '__main__':
    main()
    exit(0)