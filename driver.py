import numpy as np
import random
import q_functions
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



def main():
    maze = np.array([
        [1, 1, 1, 1, 1],
        [1, 2, 0, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 0, 3, 1],
        [1, 1, 1, 1, 1]
    ])
    actions = ['up', 'down', 'left', 'right']
    gamma = 0.9  # Discount factor
    alpha = 0.8  # Learning rate
    epsilon = 0.9  # Exploration rate
    decay_rate = 0.995  # Epsilon decay
    episodes = 100

    #### ***** preparations *******
    q_table  = q_functions.init_q_table(maze,actions)
    rewards = q_functions.init_rewards(maze)

    for i in range(episodes):
        pos = q_functions.get_starting_pos(maze)

        while maze[pos] != 3:
            action = q_functions.choose_action(pos,actions,epsilon,q_table)
            next_pos = get_next_position(pos,action)
            if is_valid_move(maze,next_pos):
                q_functions.update_q_table(rewards,next_pos,q_table,pos,actions,action,alpha,gamma)
                pos = next_pos
            else:
                q_functions.make_penalty(q_table,pos,actions,action)

        epsilon *= decay_rate



    pos = tuple(np.argwhere(maze == 2)[0])
    path = [pos]

    while maze[pos] != 3:
        action = actions[np.argmax(q_table[pos])]
        next_pos = get_next_position(pos, action)
        if is_valid_move(maze, next_pos):
            pos = next_pos
            path.append(pos)
        else:
            break  # Stop if the agent gets stuck





main()


