import numpy as np
import random


def init_q_table(maze,actions):
    q_table = np.zeros((*maze.shape, len(actions)))
    return q_table

def init_rewards(maze):
    rewards = np.zeros(maze.shape)
    rewards[maze == 3] = 1  # Reward for reaching the goal
    rewards[maze == 1] = -1  # Penalty for hitting a wall
    return rewards

def get_starting_pos(maze):
    return tuple(np.argwhere(maze == 2)[0])

def choose_action(pos,actions,epsilon,q_table):
    if random.uniform(0, 1) < epsilon:
        return random.choice(actions)  # Explore
    else:
        return actions[np.argmax(q_table[pos])]  # Exploit
def make_penalty(q_table,pos,actions,action):
    q_table[pos + (actions.index(action),)] = -1

def update_q_table(rewards,next_pos,q_table,pos,actions,action,alpha,gamma):
    reward = rewards[next_pos]
    old_q_value = q_table[pos + (actions.index(action),)]
    next_max_q_value = np.max(q_table[next_pos])

    # Update Q-value
    new_q_value = (1 - alpha) * old_q_value + alpha * (reward + gamma * next_max_q_value)
    q_table[pos + (actions.index(action),)] = new_q_value