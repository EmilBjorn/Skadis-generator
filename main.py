"""
Skådis Generator
------------
Emil Bjørn, Bjoern.emil@gmail.com
Feb 28th, 2024

This script generates IKEA SKÅDIS design files of customizable width and length.

This project uses svg.py to generate the svg code.
"""

import svg
import fpdf

STRICT = True  # Trim board to preserve standard margin or not
X_MARGIN = 20  # Default 20
Y_MARGIN = 20  # Default 20
GAP = 20  # Default 20
WIDTH = 200  # Multiple of 20
HEIGHT = 500  # Multiple of 20
STROKE = 0.02
LANDSCAPE = True

SHIFT = 20  # Default 20

# Trim the sheet dimensions to multiple of 20
if STRICT:
    WIDTH = (WIDTH // 20) * 20
    HEIGHT = (HEIGHT // 20) * 20


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
    for y in range(Y_MARGIN, HEIGHT - Y_MARGIN + 1, GAP):
        do_shift = not do_shift
        start_x = X_MARGIN
        if do_shift:
            start_x += SHIFT
        for x in range(start_x, WIDTH - X_MARGIN + 1, GAP * 2):
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

    if LANDSCAPE:
        group = svg.G(elements=elements,
                      transform=[
                          svg.Translate(0, WIDTH),
                          svg.Rotate(-90),
                      ])
        W = HEIGHT
        H = WIDTH
    else:
        group = svg.G(elements=elements)
        W = WIDTH
        H = HEIGHT

    return svg.SVG(
        viewBox=svg.ViewBoxSpec(0, 0, W, H),
        width=str(W) + "mm",
        height=str(H) + "mm",
        elements=[group],
    )


canvas = draw()
with open('output.svg', 'w', encoding='UTF-8') as file:
    file.write(str(canvas))

svg_object = fpdf.svg.SVGObject.from_string(str(canvas))

pdf = fpdf.FPDF(unit="pt", format=(svg_object.width, svg_object.height))
pdf.add_page()
svg_object.draw_to_page(pdf)

pdf.output("my_file.pdf")
