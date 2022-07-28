import pygame.math as math

class CelestialBody:
    def __init__(self, name, color, mass, radius, velocity, position):
        self.name = name
        self.mass = mass
        self.color = color
        self.radius = radius
        self.velocity = velocity
        self.position = position

Sun = CelestialBody("Sun", (0, 125, 125), 10, 50, math.Vector2(100, 100), math.Vector2(400, 400))
Mercury = CelestialBody("Mercury", (0, 125, 125), 10, 50, math.Vector2(100, 100), math.Vector2(400, 400))
Venus = CelestialBody("Venus", (0, 125, 125), 10, 50, math.Vector2(100, 100), math.Vector2(400, 400))
Earth = CelestialBody("Earth", (0, 125, 125), 10, 50, math.Vector2(100, 100), math.Vector2(400, 400))
Mars = CelestialBody("Mars", (0, 125, 125), 10, 50, math.Vector2(100, 100), math.Vector2(400, 400))
Jupiter = CelestialBody("Jupiter", (0, 125, 125), 10, 50, math.Vector2(100, 100), math.Vector2(400, 400))
Saturn = CelestialBody("Saturn", (0, 125, 125), 10, 50, math.Vector2(100, 100), math.Vector2(400, 400))
Uranus = CelestialBody("Uranus", (0, 125, 125), 10, 50, math.Vector2(100, 100), math.Vector2(400, 400))
Neptun = CelestialBody("Neptun", (0, 125, 125), 10, 50, math.Vector2(100, 100), math.Vector2(400, 400))

Bodies = [Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptun]

