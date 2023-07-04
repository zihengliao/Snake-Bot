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
            if length > 1 and distance > 2:    # capacity > is so it doesn't run for the first 2 iteration because it will eat its tail
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



# backtrack   - put into array and inside the array also have the direction as well as the coordinate
    backtrack_array = []
    while snake_map[x][y][2] != 0:
        backtrack_array.append(snake_map[x][y])
        x1, y1 = x, y
        x, y = snake_map[x][y][0], snake_map[x][y][1]
        snake_map[x1][y1] = 1       # this represents that there is a snake there

    # snake_map[apple_x][apple_y] = -1

    for i in range(len(snake_map)):
        for j in range(len(snake_map[0])):
            try:
                if snake_map[i][j][2] != 0:     # this is the problem
                    snake_map[i][j] = 0
                    continue
                else:
                    continue
            except TypeError:
                pass
            if snake_map[i][j] != 1:
                snake_map[i][j] = 0
            
    
    # basically when it doesn't find the apple, it will just go find the tail
    try:
        tail_bool = find_tail(tail_copy, apple_x, apple_y, snake_map, snake_length +1)
    except UnboundLocalError:       
        return find_tail_from_head(tail, head_x, head_y, snake)
    
    if tail_bool:
        return backtrack_array
    else:
        return find_tail_from_head(tail, head_x, head_y, snake)
    # if len(tail_bool) > 0:
    #     return backtrack_array      # if u can reach the tail from the position of the apple
    # else:
    #     backtrack_array = find_tail(tail, head_x, head_y, snake, snake_length +1)   # this logic is wrong
    #     return backtrack_array      # goal of this is for the head to go to the tail


def find_tail_from_head(tail, head_x, head_y, snake):
    snake_map = copy.deepcopy(snake)


    q = []

    tail_x = tail[0]
    tail_y = tail[1]

    found = False

    q.append((head_x, head_y))

    # while not q.empty() or not q1.empty():
    while len(q) != 0:
        
        x, y = q.pop(0)

        if x - 1 >= 0:      # if it is within the map
            if snake_map[x - 1][y] == 0 or snake_map[x -1][y] == -1:        # if it is empty
                q.append((x - 1,y))
                snake_direction = "left"
                snake_map[x - 1][y] = [x, y, snake_direction]     # 1 means its a backtrack value
            # elif snake_map[x -1][y] == -1:     # if it is an apple
            elif x - 1 == tail_x and y == tail_y:
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
            if snake_map[x + 1][y] == 0 or snake_map[x +1][y] == -1:     
                q.append((x + 1,y))
                snake_direction = "right"
                snake_map[x + 1][y] = [x, y, snake_direction]     
            # elif snake_map[x +1][y] == -1:    
            elif x + 1 == tail_x and y == tail_y:
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
            if snake_map[x][y - 1] == 0 or snake_map[x][y -1] == -1:     
                q.append((x,y - 1))
                snake_direction = "up"
                snake_map[x][y - 1] = [x, y, snake_direction]   
            # elif snake_map[x][y -1] == -1:    
            elif y -1 == tail_y and x == tail_x:
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
            if snake_map[x][y + 1] == 0 or snake_map[x][y +1] == -1:       
                q.append((x,y + 1))
                snake_direction = "down"
                snake_map[x][y + 1] = [x, y, snake_direction]    
            # elif snake_map[x][y +1] == -1:   
            elif y +1 == tail_y and x == tail_x:
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
        backtrack_array.append(snake_map[x][y])
        x1, y1 = x, y
        x, y = snake_map[x][y][0], snake_map[x][y][1]
        snake_map[x1][y1] = 1 
        # backtrack_array.append(snake_map[x][y])
    return backtrack_array

# need to have the snake_map where everything is 0 except the snake itself
def find_tail(tail, head_x, head_y, snake, length):
    if length <= 3:
        return True
    
    snake_map = copy.deepcopy(snake)

    q = []

    tail_x = tail[0]
    tail_y = tail[1]

    found = False

    q.append((head_x, head_y))

    # while not q.empty() or not q1.empty():
    while len(q) != 0:
        
        x, y = q.pop(0)
        

        if x == tail_x and y == tail_y:
            found = True
            # break
            return found


        # check left
        if x - 1 >= 0:      # if it is within the map
            if snake_map[x - 1][y] == 0:        # if it is empty
                q.append((x - 1,y))
                snake_direction = "left"
                snake_map[x - 1][y] = [x, y, snake_direction]     # 1 means its a backtrack value
            
            # elif snake_map[x -1][y] == 1:   # if it is a snake
            #     if x - 1 == tail_x and y == tail_y:
            #         # x -= 1
            #         found = True
            #         break
            #     else:
            #         pass    # don't do anything because we can't go there

            # try:
            #     # if snake_map[x -1][y][0] == tail_x and snake_map[x -1][y][1] == tail_y:     # if it is the tail
            if x - 1 == tail_x and y == tail_y and snake_map[x - 1][y][2] == 0 and length > 1:  
                snake_direction = "left"
                snake_map[x - 1][y] = [x, y, snake_direction]
                # x -= 1      # to set current co ordinates to that of tail
                found = True
                break
            # except TypeError:
            #     pass

        # check right
        if x + 1 < 26:      
            if snake_map[x + 1][y] == 0:        # if it is empty
                q.append((x + 1,y))
                snake_direction = "right"
                snake_map[x + 1][y] = [x, y, snake_direction]     # 1 means its a backtrack value
            
            # elif snake_map[x +1][y] == 1:   # if it is a snake
            #     if x + 1 == tail_x and y == tail_y:
            #         # x += 1
            #         found = True
            #         break
            #     else:
            #         pass    # don't do anything because we can't go there

            # try:
            #     # if snake_map[x +1][y][0] == tail_x and snake_map[x +1][y][1] == tail_y:     # if it is the tail
            if x + 1 == tail_x and y == tail_y and snake_map[x + 1][y][2] == 0 and length > 1:  
                snake_direction = "right"
                snake_map[x + 1][y] = [x, y, snake_direction]
                # x += 1      # to set current co ordinates to that of tail
                found = True
                break  
            # except TypeError:
            #     pass

        # check up
        if y - 1 >= 0:     
            if snake_map[x][y - 1] == 0:     
                q.append((x,y - 1))
                snake_direction = "up"
                snake_map[x][y - 1] = [x, y, snake_direction]   
           
            # elif snake_map[x][y -1] == 1:  
            #     if x == tail_x and y - 1 == tail_y:
            #         # y -= 1
            #         found = True
            #         break
            #     else:
            #         pass 

            # try:
            #     # if snake_map[x][y -1][0] == tail_x and snake_map[x][y-1][1] == tail_y:    
            if x == tail_x and y - 1 == tail_y and snake_map[x][y - 1][2] == 0 and length > 1:  
                snake_direction = "up"
                snake_map[x][y - 1] = [x, y, snake_direction]
                # y -= 1
                found = True
                break  
            # except TypeError:
            #     pass


        # check down
        if y + 1 < 26:      
            if snake_map[x][y + 1] == 0:       
                q.append((x,y + 1))
                snake_direction = "down"
                snake_map[x][y + 1] = [x, y, snake_direction]    
            
            # elif snake_map[x][y +1] == 1:  
            #     if x == tail_x and y + 1 == tail_y:
            #         # y += 1
            #         found = True
            #         break
            #     else:
            #         pass   

            # try:
            #     # if snake_map[x][y +1][0] == tail_x and snake_map[x][y+1][1] == tail_y:   
            if x == tail_x and y + 1 == tail_y and snake_map[x][y + 1][2] == 0 and length > 1:  
                snake_direction = "down"
                snake_map[x][y + 1] = [x, y, snake_direction]
                # y += 1        # for some reason, already does this 
                found = True
                break
            # except TypeError:
            #     pass
    return found
    # backtrack_array = []
    # if found:
    #     try:
    #         while snake_map[x][y][2] != 0:
    #             backtrack_array.append(snake_map[x][y])
    #             x1, y1 = x, y
    #             x, y = snake_map[x][y][0], snake_map[x][y][1]
    #             snake_map[x1][y1] = 1       # this represents that there is a snake there
    #     except TypeError:
    #         pass
    # return backtrack_array

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
    
    for i in range(5):
        if True:
            print(i)
            pass

        try:
            print(i[1])
        except:
            print("ran")