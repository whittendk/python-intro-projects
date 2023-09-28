from pynput import keyboard
from random import randint
import threading
import time
import os

global length
global apple


def print_matrix(fld):
    for i in range(len(fld)):
        for j in range(len(fld)):
            if [j, i] in snake:
                print('@', end='  ')
            else:
                print(fld[i][j], end='  ')
        print()


def print_matrix(fld):
    for i in range(len(snake)):
        if snake[i][0] == snake[i+1][0]:                    # if two points have the same x coord


def random_position():
    return randint(0, WIDTH - 1), randint(0, HEIGHT - 1)


def process_press(key):
    global direction
    match key:
        case keyboard.Key.left:
            if direction != (1, 0):
                direction = (-1, 0)
        case keyboard.Key.up:
            if direction != (0, -1):
                direction = (0, 1)
        case keyboard.Key.right:
            if direction != (-1, 0):
                direction = (1, 0)
        case keyboard.Key.down:
            if direction != (0, 1):
                direction = (0, -1)
        case _:
            direction = prev_dir()


def prev_dir():
    if snake[0][0] - snake[1][0] > 0:
        return (1, 0)
    elif snake[0][0] - snake[1][0] < 0:
        return (-1, 0)
    elif snake[0][1] - snake[1][1] > 0:
        return (0, 1)
    elif snake[0][1] - snake[1][1] < 0:
        return (0, -1)


def Move(s):
    if direction != prev_dir():                             # creates new joint
        snake.insert(1, snake[0])
    match direction:                                        # moves head
        case (-1, 0):   # left
            snake[0][0] -= 1
        case (0, 1):  # up
            snake[0][1] += 1
        case (1, 0):  # right
            snake[0][0] += 1
        case (0, -1):  # down
            snake[0][1] -= 1
    if snake[0][0] == apple:                                # eats apple
        length += 1
    else:                                                   # moves tail
        if snake[len(snake) - 2][0] - snake[len(snake) - 1][0] > 0:
            snake[len(snake) - 1][0] += 1
        elif snake[len(snake) - 2][0] - snake[len(snake) - 1][0] < 0:
            snake[len(snake) - 1][0] -= 1
        elif snake[len(snake) - 2][1] - snake[len(snake) - 1][1] > 0:
            snake[len(snake) - 1][1] += 1
        elif snake[len(snake) - 2][1] - snake[len(snake) - 1][1] < 0:
            snake[len(snake) - 1][1] -= 1
    if snake[len(snake) - 1] == snake[len(snake) - 2]:
        snake.pop(len(snake) - 1)
    print(snake)


WIDTH, HEIGHT = 10, 10
field = [['*']*HEIGHT]*WIDTH
direction = (1, 0)
apple = random_position()
length = 2
snake = [[WIDTH//2, HEIGHT//2], [WIDTH//2 - 2, HEIGHT//2]]
print('start', snake)

with keyboard.Listener(on_press=process_press) as listener:
    while True:
        Move(snake)
        print_matrix(field)
        time.sleep(1)
        os.system('cls')
