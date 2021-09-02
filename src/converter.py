from PIL import Image
from collections import deque

def is_path(pixel):
    pass

def is_end(pixel):
    pass

def find_start(pixels):
    pass

def breadth_first_search(start, pixels):
    pass

def main(file):
    img = Image.open(file)
    pixels = img.load()
    start = find_start(pixels)
    breadth_first_search(start, pixels)
    
if __name__ == '__main__':
    main()