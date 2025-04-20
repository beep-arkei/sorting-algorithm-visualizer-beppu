#Python Bogo Loop Sample
#by Ryan Kaito Beppu

"""tutorials and assets used:
https://www.youtube.com/watch?v=blLLtdv4tvo
https://www.youtube.com/watch?v=kDSdjsdoGOY
https://www.geeksforgeeks.org/python-display-text-to-pygame-window/
"""

#game proper
import pygame
import sys
import pygame_gui
from PIL import Image, ImageSequence
import os

pygame.init()

width, height = 720, 720
black = (0, 0, 0)
frame_top = height // 10
yOffset = frame_top
running = True

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Raxdflipnotes Bogo Sort | Beppu")

fontTitle = pygame.font.SysFont("comicsansms", 54) 
fontDefault = pygame.font.SysFont("comicsansms", 30) 

script_dir = os.path.dirname(os.path.abspath(__file__))
background_path = os.path.join(script_dir, "raxdBG.gif")

clock = pygame.time.Clock()
manager = pygame_gui.UIManager((width, height))
delta_time = 0.1

#background = pygame.image.load(background_path).convert_alpha()  
#background = pygame.transform.scale(background, (100, 200)) 
#background.set_alpha(255)

# Animation
frameIndex = 0
frameDelay = 5  # Adjust to control speed (higher = slower)
frameCounter = 0

#turning background to gif (dont understand too much, just copy pasted)
gif = Image.open(background_path)
gifSize = (100, 200)
frames = [
    pygame.image.fromstring(frame.convert("RGBA").resize(gifSize).tobytes(), gifSize, "RGBA")
    for frame in ImageSequence.Iterator(gif)
]
frameCount = len(frames)

titleText = fontTitle.render('Bogo Sort', True, black)
titleTextRect = titleText.get_rect()
titleTextRect.center = (width // 2, height // 10)
yOffset+=(fontTitle.get_height() + 5)

textStrings = [
    "a raxdflipnote themed bogo sort demo",
    "by Ryan Kaito Beppu",
    "",
    "Enter an array",
    "Separate with commas"
]

textSurfaces = []
for txt in textStrings:
    textSurface = fontDefault.render(txt, True, black)
    textRect = textSurface.get_rect(center=(width // 2, yOffset))  # Centered
    textSurfaces.append((textSurface, textRect))
    yOffset += fontDefault.get_height() + 5  # Move down for next line
  


while running:
    #text blit
    screen.fill((255, 255, 255))
    screen.blit(titleText, titleTextRect)
    #screen.blit(background, (50, height-250))  

    #bg implementation
    screen.blit(frames[frameIndex], (50, height-250))

    frameCounter += 1
    if frameCounter >= frameDelay:  # Change frame after delay
        frameIndex = (frameIndex + 1) % frameCount
        frameCounter = 0

    for textSurface, textRect in textSurfaces:
        screen.blit(textSurface, textRect)

    #exit application
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    delta_time = clock.tick(60) / 1000
    delta_time = max(0.001, min(0.1, delta_time))
pygame . quit() 

