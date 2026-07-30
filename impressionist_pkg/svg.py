class SVG:
    def __init__(self,width: int, height: int, background_color: tuple[int,int,int]):
        self.content = '<?xml versio="1.0" encoding="utf-8"?>\n' \
                        f'<svg version="1.1" baseProfile="full" width="{width}" ' \
                        f'height="{height}" xmlns="http://www.w3.org/2000/svg">\n' \
                        f'<rect width="100%" height="100%" fill="rgb{background_color}" />'

    def draw_ellipse(self, x1: int, y1: int, x2: int, y2: int, color: tuple[int, int, int]):
        self.content += f'<ellipse cx="{(x1 + x2) // 2 }" cy="{(y1 + y2) // 2}" ' \
                        f'rx="{abs(x1 - x2) // 2}" ry"{abs(y1 - y2) // 2 }" ' \
                        f'fill="rgb{color}" />\n'

    def draw_line(self, x1: int, y1: int, x2: int, y2: int, color: tuple[int, int, int]):
            self.content += f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="rgb{color}" ' \
            'stroke-width="1px" shape-rendering="crispEdges" />\n'

    def draw_polygon(self, coordinates: list[int], color: tuple[int, int, int]):
        points = ""
        for index in range(0, len(coordinates), 2):
            points += f"{coordinates[index]},{coordinates[index + 1]} "
        self.content += f'<polygon points="{points}" fill="rgb{color}" />\n'

    def write(self, path: str):
         self.content += '</svg>\n'
         with open(path, 'w') as f:
              f.write(self.content)
    