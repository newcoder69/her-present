import pygame
import os
from datetime import datetime
import json



# os.environ['SDL_FBDEV'] = '/dev/fb1'
# os.environ['SDL_VIDEODRIVER'] = 'fbcon'

screenWidth = 480
screenHeight = 320



messagesFile = "C:/Users/Gabe/Desktop/miscCode/herPresent/pythonPart/messages.json"

pygame.init()
pygame.font.init()
pygame.display. set_mode((0,0),pygame.FULLSCREEN)
font_path = "C:/Users/Gabe/Desktop/miscCode/herPresent/pythonPart/PixelatedEleganceRegular-ovyAA.ttf"

pixel_font = pygame.font.Font(font_path)

screen =  pygame.display.set_mode((screenWidth, screenHeight))

running = True

time_font = pygame.font.Font(font_path,68)
date_font = pygame.font.Font(font_path,28)
message_font = pygame.font.Font(font_path,20)

softWhite = (235,235,235)
softgrey = (150,150,150)
pink = (255,140,160)

background = (15,56,15)
primary = (155,188,15)
secondary = (139,172,15)
text = (233,239,236)

while running:
    screen.fill(background)
    
    currentTime = datetime.now().strftime("%I:%M:%S %p")
    currentDate = datetime.now().strftime("%A, %B %d")
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    
    
    try:
        with open(messagesFile, 'r') as f:
         data = json.load(f)
         message = data.get('message')
         message = message + " <3"
    except(FileNotFoundError, json.JSONDecodeError):
        message = "no message yet, I love you <3"
    
    text_surface = message_font.render(message, True, secondary)
    text_box = text_surface.get_rect()
    text_box.center = (screenWidth // 2, screenHeight // 2 + 20)
    
    heart = message_font.render("♥", True, pink)
    # heart_box = heart.get_rect(midleft=(text_box.right + 4, text_box.center))
    
    
    time_surface = time_font.render(currentTime, True, primary)
    time_box = time_surface.get_rect()
    time_box.center = ((screenWidth // 2) , (screenHeight // screenHeight) + 50)
    
    date_surface = date_font.render(currentDate, True, primary)
    date_box = date_surface.get_rect()
    date_box.center = (screenWidth // 2, (screenHeight // screenHeight) + 120)
    
    
    
    
    screen.blit(time_surface,time_box)
    screen.blit(text_surface, text_box )
    screen.blit(date_surface, date_box)
    # screen.blit(heart, heart_box)
    
    
    pygame.display.flip()


pygame.quit()
