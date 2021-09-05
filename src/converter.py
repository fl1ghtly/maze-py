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

# Gets the x by y dimension size of a maze
def get_dimensions(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        # maximum is guaranteed to be above or at 0
        x_max = 0
        x_count = 0

        y_max = 0
        y_count = 0
        y_passed_max = False
        for line in lines:
            x = regex.search(r'x=\K"(.*?)"', line)
            y = regex.search(r'y=\K"(.*?)"', line)

            if y:
                if int(y.group(1)) >= y_max:
                    y_max = int(y.group(1))
                else:
                    y_passed_max = True

                if not y_passed_max:
                    y_count += 1
            if x:
                if int(x.group(1)) > x_max:
                    x_max = int(x.group(1))
                    x_count += 1


        height = y_count
        # Count the last x that was missed
        width = x_count + 1
        return width, height

# Converts a 1d Maze to a 2d Maze
# Using information from the SVG
def maze_2d_converter(maze, width, height):
    x_counter = 0
    y_counter = 0
    maze_2d = [[None for x in range(width)] for y in range(height)]
    for cell in maze:
        maze_2d[y_counter][x_counter] = cell
        x_counter += 1
        
        if x_counter >= width:
            # TODO replace mutable
            x_counter = 0
            y_counter += 1
    return maze_2d

# Converts a premade Maze SVG File to 
# an array
def svg_to_array(file):
    maze = []
    svg_map = {'black': 'W', 'white': 'O', 'red': 'F',
               'green': 'S', 'orange': 'P'}
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            color = regex.search(r'fill=\K"(.*?)"', line)
            if color:
                maze.append(svg_map.get(color.group(1), None))
    return maze

if __name__ == '__main__':
    svg_to_array('maze.svg')