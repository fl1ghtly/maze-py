from reportlab.graphics import renderPM
from svglib.svglib import svg2rlg
from io import BytesIO

# Converts a SVG file to a png file
# Returns a python file object
def convert_svg(file):
    draw = svg2rlg(file)
    buff = BytesIO()
    renderPM.drawToFile(draw, buff, fmt='png')
    return buff

if __name__ == '__main__':
    convert_svg('maze.svg')