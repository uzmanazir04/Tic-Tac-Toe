#import random module
import random        
 
#draw grid and pass parameters
def draw_grid(grid):
    print(grid[1]+" | "+grid[2]+" | "+grid[3])
    print("----------")
    print(grid[4]+" | "+grid[5]+" | "+grid[6])
    print("----------")
    print(grid[7]+" | "+grid[8]+" | "+grid[9])

#assign letter to player    
def player_letter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):                 #will keep asking for symbol until user enters relevent symbol
        letter = input("Choose a symbol( X / O )? ").upper()#prompt the player to choose a symbol and capitalise the symbol entered
        print()

    if letter == 'X':                         #if player choose "X", "O" will be assigned to computer else "X" will be assigned to computer
        return ['X', 'O']                     #list containing player letter at index 0 and computer letter at index 1
    else:
        return ['O', 'X']

#this will decide who will play first
def first_turn():
    if random.randint(0, 1) == 0:       #toss for first turn using random module    
        return 'computer'               #if player wins the task, player will play first else computer will go first
    else:
        return 'player'

#enter move to the grid
def make_move(grid, letter, move):  
    grid[move] = letter              #place symbol of the player in the grid

#check for winning conditions 
def winning_conditions(grid, letter):
    return((grid[1] == letter and grid[2] == letter and grid[3] == letter) or   #this will return True if any of the moves in a verticle or horizontal lines or a diagonals matches
    (grid[4] == letter and grid[5] == letter and grid[6] == letter) or
    (grid[7] == letter and grid[8] == letter and grid[9] == letter) or
    (grid[1] == letter and grid[4] == letter and grid[7] == letter) or
    (grid[2] == letter and grid[5] == letter and grid[8] == letter) or
    (grid[3] == letter and grid[6] == letter and grid[9] == letter) or
    (grid[1] == letter and grid[5] == letter and grid[9] == letter) or
    (grid[3] == letter and grid[5] == letter and grid[7] == letter)) 

#generate a copy of grid after every move
def copy_grid(grid):                             #this will generate a grid without changing the original grid 
    grid_copy = []                               #generate an empty grid

    for i in grid:
        grid_copy.append(i)       #append the values in grid
        
    return grid_copy

#check for empty box
def free_space(grid, move):        
    return grid[move] == ' '            #will return true if the grid is empty

#prompt the player to enter their move
def player_move(grid):         
    move = ' '     
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not free_space(grid, int(move)):  #keep prompting player to enter move until player enter free space
        move = input(Player+ ", enter a valid box(1-9): ")                             #prompt player to enter move
    return int(move)

#random move 
def random_move(grid, moveList):    #check for possible move 
    possibleMoves = []
    for i in moveList:
        if free_space(grid, i):       #if possible move available it will be appended
            possibleMoves.append(i)
#this will be used for making computer moves
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)   #will make a move if there is any possible move left
    else:
        return None      # this will return none if there is no possible move left. None value return when value does not exist

#computer will make its move 
def computer_move(grid, computerLetter):
    if computerLetter == 'X':    #assigning symbol
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    for i in range(1, 10):            #this loop will run to check if computer could win or not
        copy = copy_grid(grid)         #grid will be displayed
        if free_space(copy, i):         #check for free space
            make_move(copy, computerLetter, i)     #if available, it will move
            if winning_conditions(copy, computerLetter):     #check for winning conditions
                return i         #will return that particular box 

    for i in range(1, 10):            #this loop will run to check if the player could win or not
        copy = copy_grid(grid)          #grid will be displayed
        if free_space(copy, i):        #check for free space
            make_move(copy, playerLetter , i)       #if available, it will move
            if winning_conditions(copy, playerLetter):      #check for winning conditions
                return i               #will return that particular box
            
    move = random_move(grid, [1,3,7,9])    #it will try to make a corner move that will logically help to win
    if move != None:    #if corner space is available
        return move        #return that move 

    if free_space(grid, 5):   #if corner places are not free it will check for center as it is the central point make move that is involve in winning moves
        return 5
    return random_move(grid, [2,4,6,8])     #else it will check for sides

#check for full grid
def grid_full(grid):  
    for i in range(1, 10):   #this loop iterates through every grid
        if free_space(grid, i):   
            return False         #if there is no any space free, this will return false
    return True    #then this function will return true

#replay game
def play_again():
    print("Do you want to play again? Press y if yes and press any other key to quit: ")    #this will ask player whether they want to play again or not  
    return input().lower().startswith('y')   #this will turn the letter into lowercase and the game will start again if the player enter anyting starts with y



while True:     #keep looping until it encounters a break statement
    theGrid = [" "] * 10    #creates grid
    
    print("W E L C O M E   T O   T I C   T A C   T O E ! ")    #display welcome message
    print("----------------------------------------------")
    print()
    Player = input("Enter your name: ").capitalize() #prompt the player to enter their name
    print()
    
    playerLetter, computerLetter = player_letter()   #player_letter() function will ask user to choose a symbol and assign the letters to computer and player
    
    turn  = first_turn()  #first_turn() will decide who will play first
    print("The "+ turn +" will play first.")   #display the turn
    print()
    
    gameIsPlaying = True

    while gameIsPlaying:        #the game will execute as long as this is set to True
        if turn == 'player':    #if the turn goes to player
            draw_grid(theGrid)            #the grif will be displayed
            move = player_move(theGrid)     #prompting player to enter move
            make_move(theGrid, playerLetter, move)     #entered move will be placed in grid
            if winning_conditions(theGrid, playerLetter):     #will check for winning conditions whether player make a win after entering a box
                draw_grid(theGrid)
                print("You Won the match! ")    #If player make a win this message will be displayed
                gameIsPlaying = False         #and the game will stop here
            else:
                if grid_full(theGrid):    #else it will check whether the grid is full or not
                    draw_grid(theGrid)
                    print("The game is tie!")       #if it is full, it will display this message
                    break     #loop will break
                else:
                    turn = 'computer'  #else the turn will go to computer 
                     
        else:   #if turn is not equal to player, it will be computers turn
            move = computer_move(theGrid, computerLetter)    #computer will make its move
            make_move(theGrid, computerLetter, move)
            if winning_conditions(theGrid, computerLetter):     #after computers move, this will check for winning conditions
                draw_grid(theGrid) 
                print("The computer has won! ")     #if winning conditions turn True, this message will be displayed
                gameIsPlaying = False     #the game will be ended 
            else: 
                if grid_full(theGrid):  #else it will check whether grid is full or not
                    draw_grid(theGrid)
                    print("The game is tie!")   #if the grid is full it will display this message
                    break   #loop will break
                else: 
                    turn = 'player'   #turn will go to player

    if not play_again():     #if player does not want to play again the game will quit here
        print("---------")
        break
            
            
                
                
