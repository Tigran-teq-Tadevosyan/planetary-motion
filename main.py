import pygame

import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

from CelestialBody import Bodies

pygame.init()

Window = pygame.display.set_mode([1500, 1200])

mass_slider =     Slider(Window, 50, 25, 100, 10, min=0, max=100, step=1)
angle_slider =    Slider(Window, 50, 75, 100, 10, min=-90, max=90, step=1)
velocity_slider = Slider(Window, 50, 125, 100, 10, min=0, max=100, step=1)

mass_output =     TextBox(Window, 175, 15, 150, 30, fontSize=25)
angle_output =    TextBox(Window, 175, 65, 150, 30, fontSize=25)
velocity_output = TextBox(Window, 175, 115, 150, 30, fontSize=25)


def drawBodies(Bodies, Window):
    for body in Bodies:
        pygame.draw.circle(Window, body.color, body.position, body.radius)




running = True

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    Window.fill((255, 255, 255))

    #pygame.draw.circle(Window, (0, 0, 255), (1000, 500), 250)

    drawBodies(Bodies, Window)
    
    mass_output.setText("Mass: %d X 10^10 kg" % mass_slider.getValue())
    angle_output.setText("Angle: %d deg" % angle_slider.getValue())
    velocity_output.setText("Velocity: %d km/s" % velocity_slider.getValue())
    
    # Flip the display
    pygame_widgets.update(events)
    pygame.display.update()

# Done! Time to quit.

pygame.quit()
