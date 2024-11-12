"""
v1 : pareil mais au moins on peut sortir du programme
avec la touche 'q', ou avec la souris en fermant la fenêtre
"""

from random import randint

import pygame as pg

WIDTH = 20
HEIGHT = 20

RED = (255, 0, 0)
GREEN = (0, 255, 0)
SCREEN_SIZE = (600, 600)


def handle_event(event, direction):
    running = True
    if event.type == pg.QUIT:
        running = False
    # un type de pg.KEYDOWN signifie que l'on a appuyé une touche du clavier
    elif event.type == pg.KEYDOWN:
        # si la touche est "Q" on veut quitter le programme
        if event.key == pg.K_q:
            running = False
        elif event.key == pg.K_RIGHT and direction != (-1, 0):
            direction = (1, 0)
        elif event.key == pg.K_LEFT and direction != (1, 0):
            direction = (-1, 0)
        elif event.key == pg.K_UP and direction != (0, 1):
            direction = (0, -1)
        elif event.key == pg.K_DOWN and direction != (0, -1):
            direction = (0, 1)

    return direction, running


def draw_snake(snake):
    for pos_i, pos_j in snake:
        rect = pg.Rect(pos_i * WIDTH, pos_j * HEIGHT, WIDTH, HEIGHT)
        pg.draw.rect(screen, RED, rect)


def eat_snake(snake, pomme, direction):
    if (snake[-1][0] + direction[0], snake[-1][1] + direction[1]) == pomme:
        snake = snake + [(snake[-1][0] + direction[0], snake[-1][1] + direction[1])]
        pomme = (randint(0, 29), randint(0, 29))
        print(pomme)
    else:
        snake = snake[1:] + [(snake[-1][0] + direction[0], snake[-1][1] + direction[1])]


if __name__ == "__main__":
    pg.init()
    screen = pg.display.set_mode(SCREEN_SIZE)
    clock = pg.time.Clock()

    snake = [(10, 15), (11, 15), (12, 15)]
    direction = (1, 0)
    running = True

    pomme = (5, 5)

    while running:

        clock.tick(20)

        for event in pg.event.get():
            direction, running = handle_event(event, direction)

        screen.fill((0, 0, 0))

        draw_snake(snake)

        x = pomme[0] * 20
        y = pomme[1] * 20
        rect = pg.Rect(x, y, WIDTH, HEIGHT)
        pg.draw.rect(screen, GREEN, rect)

        eat_snake(snake, pomme, direction)

        for i in range(len(snake)):
            snake[i] = (snake[i][0] % 30, snake[i][1] % 30)

        pg.display.update()

    # Enfin on rajoute un appel à pg.quit()
    # Cet appel va permettre à Pygame de "bien s'éteindre" et éviter des bugs sous Windows
    pg.quit()
