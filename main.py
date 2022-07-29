import pygame
import pygame.math as math

import pygame_widgets
from pygame_widgets.button import Button
from pygame_widgets.toggle import Toggle
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

import numpy as np

from CelestialBody import Bodies
from CelestialBody import CustomBody

pygame.init()

frameWidth = 1500
frameHeight = 1200
frameSize = math.Vector2(1500, 1200)

Window = pygame.display.set_mode(frameSize)

mass_slider =     Slider(Window, 1050, 25, 100, 10, min=0, max=1000000, step=1, initial=1000)
angle_slider =    Slider(Window, 1050, 75, 100, 10, min=-90, max=90, step=1)
velocity_slider = Slider(Window, 1050, 125, 100, 10, min=0, max=100000, step=1)
scale_slider =    Slider(Window, 1050, 175, 100, 10, min=500000000, max=10000000000, step=1, initial=3000000000)
speed_slider =    Slider(Window, 1050, 225, 100, 10, min=1000, max=400000, step=1, initial=6000)

mass_output =     TextBox(Window, 1175, 15, 150, 30, fontSize=25)
angle_output =    TextBox(Window, 1175, 65, 150, 30, fontSize=25)
velocity_output = TextBox(Window, 1175, 115, 150, 30, fontSize=25)
scale_output =    TextBox(Window, 1175, 165, 150, 30, fontSize=25)
speed_output =    TextBox(Window, 1175, 215, 150, 30, fontSize=25)
daysPassed_output=TextBox(Window, 1050, 265, 300, 30, fontSize=25)

showNamesLabel = TextBox(Window, 1050, 300, 300, 30, fontSize=25)
showNamesLabel.setText("Show planet names: ")
showNamesToggle = Toggle(Window, 1240, 307, 40, 15, startOn = True)

staticSunLabel = TextBox(Window, 1050, 335, 300, 30, fontSize=25)
staticSunLabel.setText("Static Sun: ")
staticSunToggle = Toggle(Window, 1240, 342, 40, 15, startOn = False)

font = pygame.font.SysFont('Comic Sans MS', 15)

def addCustomBody():
    CustomBody.position = math.Vector2(0, -5000 * pow(10, 9))
    
    CustomBody.mass = mass_slider.getValue() * pow(10, 20)

    theta = np.deg2rad(angle_slider.getValue())
    CustomBody.velocity = velocity_slider.getValue() * math.Vector2(np.sin(theta), np.cos(theta))
    
startButton = Button(Window, 1150, 375, 100, 25, text='Start', fontSize=25, margin=5, radius=20, onClick= addCustomBody)
    
def drawText(text, Window, x, y):
    textsurface = font.render(text, False, (0, 0, 0))
    Window.blit(textsurface, (x, y))

def drawBodies(Bodies, Window):
    for body in Bodies:
        pygame.draw.circle(Window, body.color, frameSize/2+body.position/scale_slider.getValue(), body.radius)
    if showNamesToggle.getValue():
        for body in Bodies:    
            drawText(body.name, Window, frameSize.x/2+body.position.x/scale_slider.getValue(), frameSize.y/2+body.position.y/scale_slider.getValue())


running = True
clock = pygame.time.Clock()
fps = 30

days_passed = 0

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    Window.fill((255, 255, 255))

    tick = clock.tick(50)
    
    for body in Bodies:
        if staticSunToggle.getValue() and body.name == "Sun":
            continue
        
        body.update(tick, Bodies, speed_slider.getValue())
    
    drawBodies(Bodies, Window)
    
    mass_output.setText("Mass: %d kg" % mass_slider.getValue())
    angle_output.setText("Angle: %d deg" % angle_slider.getValue())
    velocity_output.setText("Velocity: %d m/s" % velocity_slider.getValue())
    scale_output.setText("Scale: %.1f bilion m/p" % (scale_slider.getValue()/pow(10,9)))
    
    speed = speed_slider.getValue()*1000/3600 # hours per second
    speed_output.setText("Speed: %d h/s" % speed)

    days_passed += speed*tick/24000
    daysPassed_output.setText("%d earth days have passed" % days_passed)
    
    # Flip the display
    pygame_widgets.update(events) 
    pygame.display.update()

# Done! Time to quit.

pygame.quit()                   
