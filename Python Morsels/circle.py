from math import pi

class Circle:
    # init for defaulr radius equals 1
    def __init__(self, rr=1):
        self.__radius = rr
        self.__diameter = rr * 2
        self.__area = pi * rr ** 2

    # representation of object
    def __repr__(self):
        repr = 'Circle(' + str(self.__radius) + ')'
        return repr

    # getter/setter for radius
    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        else:
            self.__radius = value
            self.__diameter = value * 2
            self.__area = pi * value ** 2

    # getter/setter for diameter
    @property
    def diameter(self):
        return self.__diameter

    @diameter.setter
    def diameter(self, value):
        if value < 0:
            raise ValueError("Diameter cannot be negative")
        else:
            self.__radius = value / 2
            self.__diameter = value
            self.__area = pi * (value / 2) ** 2

    # getter/setter for area
    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, value):
        raise AttributeError


if __name__ == '__main__':
    c = Circle(5)
