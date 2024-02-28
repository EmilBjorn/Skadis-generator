"""
Skådis Generator
------------
Emil Bjørn, Bjoern.emil@gmail.com
Feb 28th, 2024

This script generates IKEA SKÅDIS design files of customizable width and length.
"""

import svg

MARGIN = 20
GAP = 20
WIDTH = 200
HEIGHT = 500
STROKE = 0.02

SHIFT = MARGIN
STEP = GAP


def draw() -> svg.SVG:
    """
    Draws the Skådis sheet
    """
    elements: list[svg.Element] = []

    # Draw bounding box
    elements.append(
        svg.Rect(x=0,
                 y=0,
                 rx=8,
                 ry=8,
                 width=WIDTH,
                 height=HEIGHT,
                 stroke_width=STROKE,
                 fill="pink",
                 stroke="black"))

    # Draw Pill-shapes
    do_shift = True
    for y in range(MARGIN, HEIGHT, STEP):
        do_shift = not do_shift
        start_x = MARGIN
        if do_shift:
            start_x += SHIFT
        for x in range(start_x, WIDTH, STEP * 2):
            elements.append(
                svg.Path(d=[
                    svg.M(x - 2.5, y - 5),
                    svg.a(2.5, 2.5, 0, 0, 1, 5, 0),
                    svg.v(10),
                    svg.a(2.5, 2.5, 0, 0, 1, -5, 0),
                    svg.Z()
                ],
                         stroke_width=STROKE,
                         stroke="black",
                         fill="white"))

    return svg.SVG(
        viewBox=svg.ViewBoxSpec(0, 0, WIDTH, HEIGHT),
        width=str(WIDTH) + "mm",
        height=str(HEIGHT) + "mm",
        elements=elements,
    )


canvas = draw()
print(canvas)
with open('output.svg', 'w', encoding='UTF-8') as file:
    file.write(str(canvas))
