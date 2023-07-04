# import queue
import copy



def autopath(snake, head_x, head_y, tail, snake_length):    # head_x and head_y is my root vertex

    snake_map = copy.deepcopy(snake)
    tail_copy = copy.deepcopy(tail)
    length = copy.deepcopy(snake_length)

    # q = queue.Queue()
    # q1 = queue.Queue()
    q = []
    q1 = []
    condition = False
    distance = 0


    q.append((head_x, head_y))

    # while not q.empty() or not q1.empty():
    while len(q) != 0 or len(q1) != 0:
        

        # if q.empty() or q1.empty():
        if len(q) == 0 or len(q1) == 0:
            if length > 1 and distance > 1:    # distance > is so it doesn't run for the first 2 iteration because it will eat its tail
                prev_x = tail_copy[0]   # tail's x coordinate
                prev_y = tail_copy[1]   # tail's y coordinate
                tail_copy = snake_map[prev_x][prev_y]
                snake_map[prev_x][prev_y] = 0
                length -= 1
            if len(q) == 0:
                condition = False
            else:
                condition = True
            distance += 1

        if condition:
            # x, y = q.get()          
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



def find_tail_from_head(tail, head_x, head_y, snake):
    snake_map = copy.deepcopy(snake)


    q = []

    tail_x = tail[0]
    tail_y = tail[1]

    q.append((head_x, head_y))

    while len(q) != 0:
        
        x, y = q.pop(0)

        if x - 1 >= 0:      # if it is within the map
            if snake_map[x - 1][y] == 0 or snake_map[x -1][y] == -1:        # if it is empty
                q.append((x - 1,y))
                snake_direction = "left"
                snake_map[x - 1][y] = [x, y, snake_direction]     # 1 means its a backtrack value

            elif x - 1 == tail_x and y == tail_y:
                snake_direction = "left"
                snake_map[x - 1][y] = [x, y, snake_direction]
                x -= 1      # to set current co ordinates to that of apple
                break
            elif snake_map[x -1][y][2] == 0:   # if it is a snake
                pass    # don't do anything because we can't go there

        # check right
        if x + 1 < 26:      
            if snake_map[x + 1][y] == 0 or snake_map[x +1][y] == -1:     
                q.append((x + 1,y))
                snake_direction = "right"
                snake_map[x + 1][y] = [x, y, snake_direction]     

            elif x + 1 == tail_x and y == tail_y:
                snake_direction = "right"
                snake_map[x + 1][y] = [x, y, snake_direction]
                x += 1
                break
            elif snake_map[x +1][y][2] == 0: 
                pass  

        # check up
        if y - 1 >= 0:     
            if snake_map[x][y - 1] == 0 or snake_map[x][y -1] == -1:     
                q.append((x,y - 1))
                snake_direction = "up"
                snake_map[x][y - 1] = [x, y, snake_direction]   
 
            elif y -1 == tail_y and x == tail_x:
                snake_direction = "up"
                snake_map[x][y - 1] = [x, y, snake_direction]
                y -= 1
                break
            elif snake_map[x][y -1][2] == 0:  
                pass   

        # check down
        if y + 1 < 26:      
            if snake_map[x][y + 1] == 0 or snake_map[x][y +1] == -1:       
                q.append((x,y + 1))
                snake_direction = "down"
                snake_map[x][y + 1] = [x, y, snake_direction]    

            elif y +1 == tail_y and x == tail_x:
                snake_direction = "down"
                snake_map[x][y + 1] = [x, y, snake_direction]
                y += 1
                break
            elif snake_map[x][y +1][2] == 0:  
                pass  


        # q.task_done()
        # q1.task_done() 



# backtrack   - put into array and inside the array also have the direction as well as the coordinate
    backtrack_array = []
    
    #  due to the positioning of the tail, the snake will reach the tail quicker than the tail can escape
    # so one solution which doesn't work is a for loop which is meant to make sure the head is behind the tail by 2 steps at all times
    # the issue with that is that it won't be able to backtrack 
    while snake_map[x][y][2] != 0:
        backtrack_array.append(snake_map[x][y])
        x, y = snake_map[x][y][0], snake_map[x][y][1]
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

    while len(q) != 0:
        
        x, y = q.pop(0)
        
        # check left
        if x - 1 >= 0:      # if it is within the map
            if snake_map[x - 1][y] == 0:        # if it is empty
                q.append((x - 1,y))
                snake_direction = "left"
                snake_map[x - 1][y] = [x, y, snake_direction]     # 1 means its a backtrack value

            if x - 1 == tail_x and y == tail_y and snake_map[x - 1][y][2] == 0 and length > 1:  
                snake_direction = "left"
                snake_map[x - 1][y] = [x, y, snake_direction]
                found = True
                break


        # check right
        if x + 1 < 26:      
            if snake_map[x + 1][y] == 0:        # if it is empty
                q.append((x + 1,y))
                snake_direction = "right"
                snake_map[x + 1][y] = [x, y, snake_direction]     # 1 means its a backtrack value
            
            if x + 1 == tail_x and y == tail_y and snake_map[x + 1][y][2] == 0 and length > 1:  
                snake_direction = "right"
                snake_map[x + 1][y] = [x, y, snake_direction]
                found = True
                break  


        # check up
        if y - 1 >= 0:     
            if snake_map[x][y - 1] == 0:     
                q.append((x,y - 1))
                snake_direction = "up"
                snake_map[x][y - 1] = [x, y, snake_direction]   
           
            if x == tail_x and y - 1 == tail_y and snake_map[x][y - 1][2] == 0 and length > 1:  
                snake_direction = "up"
                snake_map[x][y - 1] = [x, y, snake_direction]
                found = True
                break  


        # check down
        if y + 1 < 26:      
            if snake_map[x][y + 1] == 0:       
                q.append((x,y + 1))
                snake_direction = "down"
                snake_map[x][y + 1] = [x, y, snake_direction]    
            
            if x == tail_x and y + 1 == tail_y and snake_map[x][y + 1][2] == 0 and length > 1:  
                snake_direction = "down"
                snake_map[x][y + 1] = [x, y, snake_direction]
                found = True
                break

    return found



if __name__ == "__main__":
    print("running wrong file")
