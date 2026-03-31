import sys
import pygame as pgm

pgm.init()

WIDTH, HEIGHT = 800, 600
screen = pgm.display.set_mode((WIDTH, HEIGHT))
pgm.display.set_caption("Animated Circle with Keyboard Control")

WHITE = (255, 255, 255)
BLUE = (0, 100, 255)

x, y = WIDTH // 2, HEIGHT // 2
radius = 30
speed = 5

clock = pgm.time.Clock()

while True:
    screen.fill(WHITE)

    for event in pgm.event.get():
        if event.type == pgm.QUIT:
            pgm.quit()
            sys.exit()

    keys = pgm.key.get_pressed()
    if keys[pgm.K_LEFT]:
        x -= speed
    if keys[pgm.K_RIGHT]:
        x += speed
    if keys[pgm.K_UP]:
        y -= speed
    if keys[pgm.K_DOWN]:
        y += speed

    x = max(radius, min(WIDTH - radius, x))
    y = max(radius, min(HEIGHT - radius, y))

    pgm.draw.circle(screen, BLUE, (x, y), radius)

    pgm.display.flip()
    clock.tick(60)