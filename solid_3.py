class Rectangle:
    def __init__(self, w: int, h: int):
        self._w = w
        self._h = h


    @property
    def width(self) -> int:
        return self._w


    @width.setter
    def width(self, v: int) -> None:
        self._w = v  # Меняет только ширину


    @property
    def height(self) -> int:
        return self._h

    @height.setter
    def height(self, v: int) -> None:
        self._h = v  # Меняет только высоту


    def area(self) -> int:
        return self._w * self._h


class Square:
    def __init__(self, side: int):
        self._side = side


    @property
    def side(self) -> int:
        return self._side


    @side.setter
    def side(self, v: int) -> None:
        self._side = v  # Меняет только сторону


    def area(self) -> int:
        return self._side * self._side


def resize_and_get_area(r: Rectangle) -> int:
    r.width = 10
    r.height = 5
    return r.area()  
