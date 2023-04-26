class Color:
    def __init__(self, color,):
        self._color = color

    @property  # generamos el get para la variable color
    def color(self):
        return self._color

    @color.setter  # generamos  set para la variable color
    def color(self, color):
        self._color = color

    def __str__(self):
        return f'Color [color: {self._color}]'
