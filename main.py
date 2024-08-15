from Grid_DS import *
from Setup import *
from collections import deque

def play(row, col, bombCount):
    #Setup:
    board = Grid(row,col, default)
    board.display

    bombAddress = bombLocation(board,bombCount)
    bombSet(board, bombAddress)
    setInternal(board)

    #Execution:
    game = True
    while game:

        if winCheck(board, bombAddress): #wincheck returns boolean
            print('YOU WIN!!!!')
            board.internal()
            return

        board.display()
        selection = input("Enter the square: ")
        selection = selection.strip() 
        option = input("select your task: ")
        
        if selection not in board.nodes:
            print('selection error')

        else:    
            if option == 'dig':
                box = board.access(selection).internal #variable for what's in the square
                if box == bombSymbol:
                    board.internal()
                    print('Game Over')
                    return
                
                elif box in [i for i in range(9)]: #executes if box is a number between 0 to 9

                    # Kinda seems like i could remove this part of code or replace it but not sure about it. Sematic related stuff ig...
                    # The code may or maynot work if i remove this elif... not sure 
                    board.access(selection).updateDisplay(box)

                else:
                    expand(board,selection)

            elif option == 'mark':
                board.updateDisplay(selection, markerSymbol)

            elif option == 'skip': #option to skip current selection without any action. 
                #just realized there was some issue with it in the code i sent last time. Ive correncted some issues here
                return

            elif option =='unmark':
                if board.access(selection).displayValue == markerSymbol:
                    board.updateDisplay(selection, default)
               

def winCheck(board, bombAddress): #Checks if all safe squares on the grid are open. Set based operations

    expandedSquares = board.expanded
    nodes = set(board.nodes)
    freeSquares = nodes - set(bombAddress)

    if expandedSquares == freeSquares:
        return True
    else:
        return False
    #     print('nodes ', nodes)
    #     print('bombs ', bombAddress)
    #     print('free Squares = ', freeSquares)
    #     print('expanded= ', expandedSquares)
    #     print('not equal yet')
    
def expand(board, currentAddress): # A BFS implementation. Just travels like a expansion scheme checking the conditions

    queue = deque()
    queue.append(currentAddress) 
    marked ={

    }

    while queue:
        currentAddress = queue.pop()

        if currentAddress not in marked:
            board.updateDisplay(currentAddress, board.access(currentAddress).internal)
            # print('updated address: ', currentAddress, 'to ', board.access(currentAddress).internal)
            marked[currentAddress]= True
        
        #checking for neighbours of current node
        for neighbour in getNeighbourAddress(board,currentAddress, board.access(currentAddress).pointers): 
            if neighbour not in marked and board.access(currentAddress).internal not in searchHaltSymbols: #check if current is a symbol not to be opened
                queue.append(neighbour)

    # Keeping a record of the opened sqares in the board object. Set oprations
    # marked is the local variable for each BFS search initialted here. Keeps record of which squares have been travelled through onclick

    board.expanded = board.expanded | set(marked) # Takes union. adds new values if not already present
    # adds newly opned ones from marked into the main List
    
    #  print('added ', board.expanded)

#EXECUTION CODE
play(5, 5, 8)

