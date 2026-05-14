from abc import ABC, abstractmethod

class Renderer(ABC):

        @abstractmethod
        def draw_circle(self, x: int, y: int, radius: int) -> None:
            pass

        @abstractmethod
        def draw_square(self, x: int, y: int, side: int) -> None:
            pass

class SVGRenderer(Renderer):

    def draw_circle(self, x: int, y: int, radius: int) -> None:
        print(f'<circle cx="{x}" cy="{y}" r="{radius}" />')

    def draw_square(self, x: int, y: int, side: int) -> None:
        print(f'<rect x="{x}" y="{y}" width="{side}" height="{side}" />')

class CanvasRenderer(Renderer):

    def draw_circle(self, x: int, y: int, radius: int) -> None:
        print(f'ctx.arc({x}, {y}, {radius}, 0, 2 * Math.PI);')
        print('ctx.stroke();')

    def draw_square(self, x: int, y: int, side: int) -> None:
        print(f'ctx.strokeRect({x}, {y}, {side}, {side});')

class Shape(ABC):

    def __init__(self, renderer: Renderer) -> None:
        self._renderer = renderer

    @abstractmethod
    def draw(self) -> None:
        pass

class Circle(Shape):

    def __init__(self, renderer: Renderer, x: int, y: int, radius: int) -> None:
        super().__init__(renderer)
        self._x = x
        self._y = y
        self._radius = radius

    def draw(self) -> None:
        self._renderer.draw_circle(self._x, self._y, self._radius)

class Square(Shape):

    def __init__(self, renderer: Renderer, x: int, y: int, side: int) -> None:
        super().__init__(renderer)
        self._x = x
        self._y = y
        self._side = side

    def draw(self) -> None:
        self._renderer.draw_square(self._x, self._y, self._side)


def main() -> None:
    svg_renderer = SVGRenderer()
    canvas_renderer = CanvasRenderer()

    shapes = [
        Circle(svg_renderer, 10, 10, 5),
        Square(svg_renderer, 20, 20, 10),
        Circle(canvas_renderer, 30, 30, 15),
        Square(canvas_renderer, 40, 40, 20)
    ]

    for shape in shapes:
        shape.draw()
        print()


if __name__ == '__main__':
    main()
