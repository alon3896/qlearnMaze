import pygame
from constant import *
import numpy as np
import q_functions
from smile import Smile

def is_valid_move(maze, pos):
    """Check if a move is valid within the maze."""
    x, y = pos
    return maze[x, y] != 1


def get_next_position(pos, action):
    """Get the next position based on the action."""
    x, y = pos
    if action == 'up':
        return (x - 1, y)
    elif action == 'down':
        return (x + 1, y)
    elif action == 'left':
        return (x, y - 1)
    elif action == 'right':
        return (x, y + 1)


def init_screen():
    maze = np.array([
        [1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 2, 0, 0, 1],
        [1, 1, 1, 0, 0, 0, 1],
        [1, 3, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1]
    ])
    row, col = maze.shape
    for i in range(row):
        for j in range(col):
            if maze[i, j] == 1:
                add_cube(100 * j, 100 * i, 'black')
            if maze[i, j] == 2:
                add_cube(100 * j, 100 * i, 'green')
            if maze[i, j] == 3:
                add_cube(100 * j, 100 * i, 'blue')


def add_cube(x, y, color):
    square = pygame.Rect(x, y, 100, 100)
    pygame.draw.rect(screen, color, square)
def add_text(epi):
    font = pygame.font.SysFont("Ariel",32)
    text = font.render(epi, True, "white")
    screen.blit(text, [0, 0])
def q_move(smile,clock):
    maze = np.array([
        [1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 2, 0, 0, 1],
        [1, 1, 1, 0, 0, 0, 1],
        [1, 3, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1]
    ])
    actions = ['up', 'down', 'left', 'right']
    gamma = 0.9  # Discount factor
    alpha = 0.8  # Learning rate
    epsilon = 0.9  # Exploration rate
    decay_rate = 0.9  # Epsilon decay
    episodes = 100
    q_table = q_functions.init_q_table(maze, actions)
    rewards = q_functions.init_rewards(maze)

    for i in range(episodes):
        pos = q_functions.get_starting_pos(maze)
        while maze[pos] != 3:
            action = q_functions.choose_action(pos, actions, epsilon, q_table)
            next_pos = get_next_position(pos, action)
            if is_valid_move(maze, next_pos):
                q_functions.update_q_table(rewards, next_pos, q_table, pos, actions, action, alpha, gamma)
                pos = next_pos


                smile.xpos = pos[1] * 100
                smile.ypos = pos[0] * 100
                screen.fill("white")
                init_screen()
                smile.add(screen)
                add_text(str(i))
                pygame.display.flip()
                clock.tick(15)

            else:
                q_functions.make_penalty(q_table, pos, actions, action)

        epsilon *= decay_rate
        print("end episode", i)


def main():
    clock = pygame.time.Clock()

    tomove=0




    pygame.init()
    global screen
    screen_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
    screen = pygame.display.set_mode(screen_size)
    finish = False

    smile = Smile(300,100)
    while not finish:
        screen.fill("white")
        init_screen()
        smile.add(screen)

            #### ***** preparations *******
        if tomove ==0:
            q_move(smile,clock)
            tomove+=1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True

        pygame.display.flip()
    pygame.quit()


main()
