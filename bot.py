import queue
import copy


def autopath(snake, head_x, head_y, tail, snake_length):    # head_x and head_y is my root vertex

    snake_map = copy.deepcopy(snake)
    tail_copy = copy.deepcopy(tail)
    length = copy.deepcopy(snake_length)
    # length += 1     # this is to account for the initial step at the beginning
    # q = queue.Queue()
    # q1 = queue.Queue()
    q = []
    q1 = []
    condition = False
    capacity = 0

    q.append((head_x, head_y))

    # while not q.empty() or not q1.empty():
    while len(q) != 0 or len(q1) != 0:
        capacity += 1
        print(capacity)

        # if q.empty() or q1.empty():
        if len(q) == 0 or len(q1) == 0:
            if length > 1:
                prev_x = tail_copy[0]
                prev_y = tail_copy[1]
                tail_copy = snake_map[prev_x][prev_y]
                snake_map[prev_x][prev_y] = 0
                length -= 1
            if condition == True:
                condition = False
            else:
                condition = True

        if condition:
            # x, y = q.get()          # the thread is fucked for this
            x, y = q.pop(0)
        else:
            # x, y = q1.get()
            x, y = q1.pop(0)
            

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
        if x + 1 < 25:      
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
        if y + 1 < 25:      
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



      

    # backtrack   - put into array and inside the array also have the direction as well as the coordinate
    backtrack_array = []
    while snake_map[x][y][2] != 0:
        print("found")
        backtrack_array.append(snake_map[x][y])
        x, y = snake_map[x][y][0], snake_map[x][y][1]

    print("fuck")
    snake_map[apple_x][apple_y] = -1
    return backtrack_array

# perform bfs
# have a memo array to backtrack
# let it die if it decides to go to a dead end


if __name__ == "__main__":
    lst = [1, 3, 4, 5]
    lst1 = lst.copy()
    lst1[0] = 2
    print(lst)