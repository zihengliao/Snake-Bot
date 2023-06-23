import queue
import copy



def autopath(snake, head_x, head_y, tail, snake_length, default_path):    # head_x and head_y is my root vertex

    snake_map = copy.deepcopy(snake)
    tail_copy = copy.deepcopy(tail)
    length = copy.deepcopy(snake_length)
    # length += 1     # this is to account for the initial step at the beginning
    # q = queue.Queue()
    # q1 = queue.Queue()
    q = []
    q1 = []
    condition = False
    # capacity = 0
    distance = 0

    q.append((head_x, head_y))

    # while not q.empty() or not q1.empty():
    while len(q) != 0 or len(q1) != 0:
        

        # if q.empty() or q1.empty():
        if len(q) == 0 or len(q1) == 0:
            # length > 1 is so it can backtrack
            if length > 1 and distance > 1:    # capacity > is so it doesn't run for the first 2 iteration because it will eat its tail
                prev_x = tail_copy[0]
                prev_y = tail_copy[1]
                tail_copy = snake_map[prev_x][prev_y]
                snake_map[prev_x][prev_y] = 0
                length -= 1
            if len(q) == 0:
                condition = False
            else:
                condition = True
            distance += 1

        if condition:
            # x, y = q.get()          # the thread is fucked for this
            x, y = q.pop(0)
        else:
            # x, y = q1.get()
            x, y = q1.pop(0)
            
        # capacity += 1
        # print(capacity)

        # check left
        if x - 1 >= 0:      # if it is within the map
            if snake_map[x - 1][y] == 0:        # if it is empty
                if not condition:
                    q.append((x - 1,y))
                else:
                    q1.append((x - 1,y))
                snake_direction = "left"
                snake_map[x - 1][y] = [x, y, snake_direction]     # 1 means its a backtrack value
            elif snake_map[x -1][y] == -1:     # if it is an apple
                snake_direction = "left"
                snake_map[x - 1][y] = [x, y, snake_direction]
                x -= 1      # to set current co ordinates to that of apple
                apple_x = x
                apple_y = y
                break
            elif snake_map[x -1][y][2] == 0:   # if it is a snake
                pass    # don't do anything because we can't go there

        # check right
        if x + 1 < 26:      
            if snake_map[x + 1][y] == 0:     
                if not condition:   
                    q.append((x + 1,y))
                else:
                    q1.append((x + 1,y))
                snake_direction = "right"
                snake_map[x + 1][y] = [x, y, snake_direction]     
            elif snake_map[x +1][y] == -1:    
                snake_direction = "right"
                snake_map[x + 1][y] = [x, y, snake_direction]
                x += 1
                apple_x = x
                apple_y = y
                break
            elif snake_map[x +1][y][2] == 0: 
                pass  

        # check up
        if y - 1 >= 0:     
            if snake_map[x][y - 1] == 0:     
                if not condition: 
                    q.append((x,y - 1))
                else:
                    q1.append((x,y - 1))
                snake_direction = "up"
                snake_map[x][y - 1] = [x, y, snake_direction]   
            elif snake_map[x][y -1] == -1:    
                snake_direction = "up"
                snake_map[x][y - 1] = [x, y, snake_direction]
                y -= 1
                apple_x = x
                apple_y = y
                break
            elif snake_map[x][y -1][2] == 0:  
                pass   

        # check down
        if y + 1 < 26:      
            if snake_map[x][y + 1] == 0:       
                if not condition:
                    q.append((x,y + 1))
                else:
                    q1.append((x,y + 1))
                snake_direction = "down"
                snake_map[x][y + 1] = [x, y, snake_direction]    
            elif snake_map[x][y +1] == -1:   
                snake_direction = "down"
                snake_map[x][y + 1] = [x, y, snake_direction]
                y += 1
                apple_x = x
                apple_y = y
                break
            elif snake_map[x][y +1][2] == 0:  
                pass  


        # q.task_done()
        # q1.task_done() 


    # this is for calculating the amount of steps it takes to hit itself
    next_pos_x, next_pos_y = default_path[apple_x][apple_y][0], default_path[apple_x][apple_y][1]
    missing_len = 0
    for i in range(distance):   # possibly distance + 1
        # print(next_pos_x, next_pos_y, 1)
        if snake[next_pos_x][next_pos_y] != 0:
            missing_len = length - i - 1       #check this
            break
        next_pos_x, next_pos_y = default_path[next_pos_x][next_pos_y][0], default_path[next_pos_x][next_pos_y][1]



    default_path_backtrack = []
    next_pos_x, next_pos_y = head_x, head_y

    for i in range(missing_len):
        print(next_pos_x, next_pos_y, 1)
        default_path_backtrack.append(default_path[next_pos_x][next_pos_y])
        next_pos_x, next_pos_y = default_path[next_pos_x][next_pos_y][0], default_path[next_pos_x][next_pos_y][1]
            

    if len(default_path_backtrack) > 1:
        default_path_backtrack.reverse()
        # default_path_backtrack.append
        return default_path_backtrack











    # backtrack   - put into array and inside the array also have the direction as well as the coordinate
    backtrack_array = []
    while snake_map[x][y][2] != 0:
        backtrack_array.append(snake_map[x][y])
        x, y = snake_map[x][y][0], snake_map[x][y][1]


    snake_map[apple_x][apple_y] = -1
    return backtrack_array








# creating a hamiltonian cycle
def default_map():
    default_path = [[0 for i in range(26)] for j in range(26)]
    q = []
    # setting up the base case
    # default_path[0][0] = [0, 1]         # pointing downwards 
    q.append((0, 0))

    while len(q) != 0:
        x, y = q.pop(0)

        # check down
        if y + 1 < 26 and default_path[x][y + 1] == 0 :
            default_path[x][y] = [x, y + 1, "down"]
            # default_path[x][y + 1] = [x, y, "down"]
            # default_path[x][y] = [x, y, "down"]
            q.append((x, y + 1))

        # check right
        elif x + 1 < 26 and default_path[x + 1][y] == 0:
            default_path[x][y] = [x + 1, y, "right"]
            # default_path[x + 1][y] = [x, y, "right"]
            # default_path[x][y] = [x, y, "right"]
            q.append((x + 1, y))

        # check left
        elif x - 1 >= 0 and default_path[x - 1][y] == 0:
            default_path[x][y] = [x - 1, y, "left"]
            # default_path[x - 1][y] = [x, y, "left"]
            # default_path[x][y] = [x, y, "left"]
            q.append((x - 1, y))
        
        # check up and go up by 1 square
        elif y - 1 >= 0 and default_path[x][y - 1] == 0:
            default_path[x][y] = [x, y - 1, "up"]
            # default_path[x][y - 1] = [x, y, "up"]
            # default_path[x][y] = [x, y, "up"]
            q.append((x, y - 1))

    default_path[x][y] = [x - 1, y, "left"]

    return default_path


if __name__ == "__main__":
    print(default_map())
    # x = [1, 3]
    # y, z = x
    # print(y, z)