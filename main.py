def q_move(smile,clock,tomove):
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
                pygame.display.flip()
                clock.tick(15)

            else:
                q_functions.make_penalty(q_table, pos, actions, action)

        epsilon *= decay_rate
        print("end episode", i)
        tomove += 1