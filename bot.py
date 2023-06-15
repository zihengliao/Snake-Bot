import queue
import copy


def autopath(snake, head_x, head_y):    # head_x and head_y is my root vertex
    # if it is 0, it is empty
    # if it is -1, it is an apple
    # if the third element in the list is 1, it is a snake
    snake_map = copy.deepcopy(snake)
    q = queue.Queue()

    q.put((head_x, head_y))

    while not q.empty():
        x, y = q.get()

        # check left
        if x - 1 >= 0:      # if it is within the map
            if snake_map[x - 1][y] == 0:        # if it is empty
                q.put((x - 1,y))
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
                q.put((x + 1,y))
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
                q.put((x,y - 1))
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
                q.put((x,y + 1))
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

       
            



      

    # backtrack   - put into array and inside the array also have the direction as well as the coordinate
    backtrack_array = []
    while snake_map[x][y][2] != 0:
        # print("found")
        backtrack_array.append(snake_map[x][y])
        x, y = snake_map[x][y][0], snake_map[x][y][1]

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