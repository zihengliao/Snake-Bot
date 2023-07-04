# Snake-Bot
A bot that plays snake for you so you don't have to

## Examples of the bot
### The bot running
    ![going_for_apple_1](https://github.com/zihengliao/Snake-Bot/assets/119108854/0391f043-99aa-41b5-985b-11d88b601132)
    ![going_for_apple_2](https://github.com/zihengliao/Snake-Bot/assets/119108854/99e030b5-7b0d-4c2d-9638-25dccf253f9a)

### The bot not going to the apple directly
  * If the snake feels like it will be trapped, it will avoid eating the apple straight away
    ![not_going_for_apple2](https://github.com/zihengliao/Snake-Bot/assets/119108854/ca866752-0c78-40ed-aa7a-ef5212c3134b)
  * If it believes it will be trapped even slightly
    ![not_going_for_apple1](https://github.com/zihengliao/Snake-Bot/assets/119108854/b38984c4-4bd4-4c84-a11a-49c8d72e85dc)


# Alogrithm in a nutshell
* Completes BFS to find the apple
* Whilst completing BFS, use a memo array to keep track of the path taken. This also ensures the most efficient path is taken
* Once apple is found, complete BFS again to find if it is possible to reach the tail of the snake (Want to maintain a hamiltonian cycle at all times)
* If it isn't possible to maintain a hamiltonian cycle if the apple is eaten, the snake will attempt travel its own tail (completing the hamiltonian cycle)
* Else, travel to the apple using the memo array created earlier 
* Repeat the above steps

# Running the bot
* To run the bot, just run the snake.py file

# Try beat the bot
* To play the game yourself, uncomment the code at the bottom of the file so it looks like this:
![image](https://github.com/zihengliao/Snake-Bot/assets/119108854/f271e1fc-fbcd-4e33-acc0-575f4d20c96d)

