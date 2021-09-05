from reportlab.graphics import renderPM
from svglib.svglib import svg2rlg
from io import BytesIO
import regex

# Converts a SVG file to a png file
# Returns a python file object
def convert_svg(file):
    draw = svg2rlg(file)
    buff = BytesIO()
    renderPM.drawToFile(draw, buff, fmt='png')
    return buff

# Converts a premade Maze SVG File to 
# an array
def svg_to_array(file, color_dict):
    maze = []
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            color = regex.search(r'fill=\K"(.*?)"', line)
            if color:
                maze.append(color_dict.get(color.group(1), None))
    return maze

if __name__ == '__main__':
    svg_map = {'black': 'W', 'white': 'O', 'red': 'F',
               'green': 'S', 'orange': 'P'}
    test = svg_to_array('maze.svg', svg_map)
    pass