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
x_margin = 20  # Default 20
y_margin = 20  # Default 20
gap = 20  # Default 20
WIDTH = 200  # Multiple of 20
HEIGHT = 500  # Multiple of 20
stroke = 0.02
landscape = True

SHIFT = 20  # Default 20

# Trim the sheet dimensions to multiple of 20
if STRICT:
    WIDTH = (WIDTH // 20) * 20
    HEIGHT = (HEIGHT // 20) * 20


def draw(width,
         height,
         x_margin=20,
         y_margin=20,
         landscape=False,
         trim=True,
         gap=20,
         stroke=0.02) -> svg.SVG:
    """
    Draws the Skådis sheet
    """
    elements: list[svg.Element] = []
    SHIFT = 20

    # Trim the sheet dimensions to multiple of 20
    if trim:
        width = (width // 20) * 20
        height = (height // 20) * 20

    # Draw bounding box
    elements.append(
        svg.Rect(x=0,
                 y=0,
                 rx=8,
                 ry=8,
                 width=width,
                 height=height,
                 stroke_width=stroke,
                 fill="pink",
                 stroke="black"))

    # Draw Pill-shapes
    do_shift = True
    for y in range(y_margin, height - y_margin + 1, gap):
        do_shift = not do_shift
        start_x = x_margin
        if do_shift:
            start_x += SHIFT
        for x in range(start_x, width - x_margin + 1, gap * 2):
            elements.append(
                svg.Path(d=[
                    svg.M(x - 2.5, y - 5),
                    svg.a(2.5, 2.5, 0, 0, 1, 5, 0),
                    svg.v(10),
                    svg.a(2.5, 2.5, 0, 0, 1, -5, 0),
                    svg.Z()
                ],
                         stroke_width=stroke,
                         stroke="black",
                         fill="white"))

    if landscape:
        group = svg.G(elements=elements,
                      transform=[
                          svg.Translate(0, width),
                          svg.Rotate(-90),
                      ])
        width, height = height, width
    else:
        group = svg.G(elements=elements)

    return svg.SVG(
        viewBox=svg.ViewBoxSpec(0, 0, width, height),
        width=str(width) + "mm",
        height=str(height) + "mm",
        elements=[group],
    )


if __name__ == '__main__':

    WIDTH = 200
    HEIGHT = 380

    canvas = draw(WIDTH, HEIGHT)
    with open('output.svg', 'w', encoding='UTF-8') as file:
        file.write(str(canvas))

    svg_object = fpdf.svg.SVGObject.from_string(str(canvas))

    pdf = fpdf.FPDF(unit="pt", format=(svg_object.width, svg_object.height))
    pdf.add_page()
    svg_object.draw_to_page(pdf)

    pdf_filename = f"IKEA_Skådis_{WIDTH}X{HEIGHT}_{'Landscape' if landscape else 'Portrait'}.pdf"
    pdf.output(pdf_filename)
