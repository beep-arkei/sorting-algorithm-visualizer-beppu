# tutorials used:
# https://www.youtube.com/watch?v=twRidO-_vqQ&t=159s


import pygame
import random
pygame.init()

class DrawInformation:
    #basic colors
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    BLUE = 0, 0, 255
    GREY = 128, 128, 128

    #planned theme colors
    BACKGROUND = 15, 18, 34      
    DARK_GRAY = 30, 33, 50         
    MID_GRAY = 60, 65, 90          
    LIGHT_GRAY = 120, 130, 160    

    BLUE = 100, 120, 255
    BLUE_LIGHT = 140, 170, 255
    BLUE_DARK = 40, 60, 140
    BLUE_PURPLE = 90, 70, 220

    PINK = 255, 100, 180
    PINK_LIGHT = 255, 140, 200
    PINK_DARK = 180, 60, 130
    PINK_PURPLE = 200, 80, 200

    VIOLET = 150, 90, 220
    CYAN = 80, 200, 255
    HOT_PINK = 255, 80, 160

    GRADIENTS = [
        

    BACKGROUND_COLOR = BACKGROUND

    SIDE_PAD = 100
    TOP_PAD = 150   

    def __init__(self, width, height, lst):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("beep's Sorting Algorithm Visualizer")
        self.set_list(lst)

    def set_list(self, lst):
        self.lst = lst
        self.max_val = max(lst)
        self.min_val = min(lst)

        self.block_width = round((self.width -self.SIDE_PAD) / len(lst))
        self.block_height = round((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        self.start_x = self.SIDE_PAD // 2

def draw(draw_info):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)
    pygame.display.update()

def draw_list(draw_info):


def generate_starting_list(n, min_val, max_val):
    lst = []

    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)

    return lst

def main():
    run = True
    clock = pygame.time.Clock()

    n = 50
    min_val = 0
    max_val = 100

    lst = generate_starting_list(n, min_val, max_val)
    draw_info = DrawInformation(800, 600, lst)

    while run:
        clock.tick(60)
        
        draw(draw_info)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
    pygame.quit()

if __name__ == "__main__":
    main()