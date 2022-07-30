import pygame.math as math

G_const = 6.67 * pow(10, -11)
iteration_count = 500

class CelestialBody:
    def __init__(self, name, color, mass, radius, velocity, position):
        self.name = name
        self.mass = mass
        self.color = color
        self.radius = radius
        self.velocity = velocity
        self.position = position
        

    def update(self, millisec, Bodies, speed):
        if self.mass == 0:
            return

        dt =  millisec * speed / iteration_count
        for i in range(1, iteration_count):
            a = math.Vector2(0, 0)
            self.position += dt * self.velocity
        
            for body in Bodies:
                if body.name == self.name:
                    continue

                self2BodyVec = self.position - body.position
                a += -1 * self2BodyVec.normalize() * G_const * body.mass/self2BodyVec.length_squared()

            
            # if i == 250 and self.name == "":
            #     print(a)
                
            self.velocity += dt * a
        

Sun = CelestialBody("Sun", (235, 211, 0), 1.989* pow(10, 30), 5,
                    math.Vector2(0, 0), math.Vector2(0, 0))
Mercury = CelestialBody("Mercury", (235, 176, 100), 3.3 * pow(10, 23), 2,
                        math.Vector2(47870, 0), math.Vector2(0, 58 * pow(10, 9)))
Venus = CelestialBody("Venus", (235, 188, 57), 48.67*pow(10, 23), 9,
                      math.Vector2(35020, 0), math.Vector2(0, 108 * pow(10, 9)))
Earth = CelestialBody("Earth", (8, 173, 135), 59.72*pow(10, 23), 5,
                      math.Vector2(29780, 0), math.Vector2(0, 150 * pow(10, 9)))
Mars = CelestialBody("Mars", (219, 93, 237), 6.417*pow(10, 23), 2.5,
                     math.Vector2(24077, 0), math.Vector2(0, 228 * pow(10, 9)))
Jupiter = CelestialBody("Jupiter", (125, 0, 125), 18990*pow(10, 23), 40,
                        math.Vector2(13070, 0), math.Vector2(0, 778 * pow(10, 9)))
Saturn = CelestialBody("Saturn", (200, 200, 200), 5685*pow(10, 23), 30,
                       math.Vector2(9690, 0), math.Vector2(0, 1400 * pow(10, 9)))
Uranus = CelestialBody("Uranus", (51, 200, 125), 868.2*pow(10, 23), 15,
                       math.Vector2(6810, 0), math.Vector2(0, 2900 * pow(10, 9) ))
Neptun = CelestialBody("Neptun", (0, 200, 0), 1024*pow(10, 23), 13,
                       math.Vector2(5430, 0), math.Vector2(0, 4500 * pow(10, 9)))

CustomBody = CelestialBody("", (255, 0, 0), 0, 10,
                           math.Vector2(0, 0), math.Vector2(0, -5000 * pow(10, 9)))

Bodies = [CustomBody, Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptun]

