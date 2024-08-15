import random


# Just added some colour codes. Displays coloured text on the console for clarity.
# Maynot work on some consoles so maybe remove the colour formatting is issues are seen 

RESET = "\033[0m"
RED = "\033[31m"
PURPLE = "\033[35m"
YELLOW = "\033[33m"

# Delete the <ColourName> and RESET variables from front and last to remove coloured text

bombSymbol = RED+ ' o '+RESET
markerSymbol = PURPLE + ' # ' + RESET
default = YELLOW + ' * '+ RESET

# Just some sketchy code lmao. stores numbers from 1 to 9, markers and bombs
searchHaltSymbols =[(' '+ str(i)+ ' ') for i in range(1,9)]
searchHaltSymbols.append(bombSymbol)
searchHaltSymbols.append(markerSymbol)


def bombLocation(board, bombCount = 10): #random number generator
    addressList =[]
    while len(addressList)<bombCount:
        x = random.randint(0,board.rowSpan-1)
        y = random.randint(0,board.colSpan-1)
        address = str(x)+'_' +str(y) 
        
        if address not in addressList:
            addressList.append(address)
    return addressList
        
def bombSet(board, addressList): # Updates the board and adds bombs to random locations
    for address in addressList:
        board.access(address).internal = bombSymbol
        # print('set bomb')
    
def setInternal(board): # Updates the board and decides where to add numbers where they're supposed to be
    for address in board.nodes:
        if board.access(address).internal != bombSymbol:
            counter = 0
            for node in board.neighbourhood(address): #iterates over addresses of all neighbouring nodes
                if board.access(node).internal == bombSymbol:
                    counter += 1 #if the node contains a bomb it increments

            if counter !=0: # 0 value means empty squares so ignoring it
                board.access(address).internal = ' '+ str(counter)+ ' '

    return