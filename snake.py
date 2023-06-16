import pygame
import random
from bot import autopath




WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
SIZE = 20



pygame.display.set_caption("Snake")
clock = pygame.time.Clock()


def ran_pos_generator(snake):
    random_x_position = random.randint(0, 24) 
    random_y_position = random.randint(0, 24) 
    while snake[random_x_position][random_y_position] != 0:
        random_x_position = random.randint(0, 24) 
        random_y_position = random.randint(0, 24) 
    return random_x_position, random_y_position





def snake_update(head_pos_x, head_pos_y, ms_x, ms_y, tail, eat, snake):

    snake[head_pos_x][head_pos_y] = [head_pos_x, head_pos_y, 0]   # the 0 at index 2 is to signify that it is a snake and not the backtrack value
    snake[head_pos_x - ms_x][head_pos_y - ms_y] = [head_pos_x, head_pos_y, 0]    
     
    snake_head = pygame.Rect(head_pos_x * SIZE + 1, head_pos_y * SIZE + 1, SIZE - 1, SIZE - 1)
    pygame.draw.rect(WIN, "green", snake_head)

    if eat:
        pass        # don't need to delete the tail if it eats apple
        
    else:

        prev_x = tail[0]
        prev_y = tail[1]
        tail = snake[prev_x][prev_y]
        snake[prev_x][prev_y] = 0

        snake_tail = pygame.Rect(prev_x * SIZE + 1, prev_y * SIZE + 1, SIZE - 1, SIZE - 1)
        pygame.draw.rect(WIN, "black", snake_tail)

    return tail, snake
        

def apple(snake):
    # starting position of apple
    x, y = ran_pos_generator(snake)
    snake[x][y] = -1    # to signify apple is on the map
    apple = pygame.Rect(x * SIZE + 1, y * SIZE + 1, SIZE - 1, SIZE - 1) 
    pygame.draw.rect(WIN, "red", apple)

    return snake
















def main(human):
    # global snake
    # initialising snake head position
    snake = [[0 for i in range(25)] for j in range(25)]     # this is the map
    head_pos_x, head_pos_y = ran_pos_generator(snake)
    snake[head_pos_x][head_pos_y] = [head_pos_x, head_pos_y, 0]  # this is the head of the snake. snake will be represented thru backtracking sort of 

    snake_head = pygame.Rect(head_pos_x * SIZE + 1, head_pos_y * SIZE + 1, SIZE - 1, SIZE - 1)
    pygame.draw.rect(WIN, "green", snake_head)

    tail = [head_pos_x, head_pos_y, 0]  # this is the tail index of the snake
    snake_length = 1
    snake = apple(snake)
    pygame.display.update()


    ms_x = 0      # this is movement speed for x
    ms_y = 0      # this is movement speed for y
    time_delay = 80
    time = 0
    delayed = True      # this is so you can only mash one button at a time so if you were going left and you pressed down then right really quickly, it wouldn't go right
    path = []
    
    while True:
        clock.tick(15)
        if human:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w and ms_y != 1 and delayed:
                        ms_y = -1
                        ms_x = 0
                        delayed = False

                    if event.key == pygame.K_a and ms_x != 1 and delayed:
                        ms_x = -1    
                        ms_y = 0
                        delayed = False

                    if event.key == pygame.K_s and ms_y != -1 and delayed:
                        ms_y = 1
                        ms_x = 0
                        delayed = False

                    if event.key == pygame.K_d and ms_x != -1 and delayed:
                        ms_x = 1
                        ms_y = 0
                        delayed = False
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            if len(path) == 0:
                print("run")
                path = autopath(snake, head_pos_x, head_pos_y, tail, snake_length)
                print(path)
            direction = path.pop()
            print(direction)
            head_pos_x = direction[0]
            head_pos_y = direction[1]
            if direction[2] == "up":
                ms_y = -1
                ms_x = 0
            if direction[2] == "down":
                ms_y = 1
                ms_x = 0
            if direction[2] == "left":
                ms_x = -1
                ms_y = 0
            if direction[2] == "right":
                ms_x = 1
                ms_y = 0

        if human:
            time_now = pygame.time.get_ticks()
            if time_now - time > time_delay and (ms_x != 0 or ms_y != 0):       # don't want it to blank out the snake_head moving before key is pressed
                delayed = True
                time = time_now
                head_pos_x += ms_x
                head_pos_y += ms_y

                if head_pos_x < 0 or head_pos_y < 0 or head_pos_x > 24 or head_pos_y > 24:
                    WIN.fill("black")
                    return
                
                # checking if there is a collision or if it eats an apple
                eaten = False   # didn't eat apple
                if snake[head_pos_x][head_pos_y] == -1:
                    snake = apple(snake)
                    eaten = True
                    snake_length += 1

                if snake[head_pos_x][head_pos_y] == 0 or snake[head_pos_x][head_pos_y] == -1 or snake[head_pos_x][head_pos_y][2] != 0:
                    tail, snake = snake_update(head_pos_x, head_pos_y, ms_x, ms_y, tail, eaten, snake)
                    pygame.display.set_caption(f"Snake  Score: {snake_length}")
                    pygame.display.update()
                else:
                    WIN.fill("black")
                    return
                

        else:       # if the bot is playing
            head_pos_x += ms_x
            head_pos_y += ms_y

            if head_pos_x < 0 or head_pos_y < 0 or head_pos_x > 24 or head_pos_y > 24:
                WIN.fill("black")
                return
            
            # checking if there is a collision or if it eats an apple
            eaten = False   # didn't eat apple
            if snake[head_pos_x][head_pos_y] == -1:
                snake = apple(snake)
                eaten = True
                snake_length += 1

            if snake[head_pos_x][head_pos_y] == 0 or snake[head_pos_x][head_pos_y] == -1 or snake[head_pos_x][head_pos_y][2] != 0:
                tail, snake = snake_update(head_pos_x, head_pos_y, ms_x, ms_y, tail, eaten, snake)
                pygame.display.set_caption(f"Snake  Score: {snake_length}")
                pygame.display.update()
            else:
                WIN.fill("black")
                return


if __name__ == "__main__":
    while True:
        # ans = input("Press 1 to play or 0 for computer to play for you: \n")
        # if ans == "1":
        #     human = True
        # else:
        #     human = False
        human = False
        main(human)

