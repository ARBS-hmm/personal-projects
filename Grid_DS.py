from collections import deque

def vectorSum(vec1, vec2):
    return [vec1[0]+vec2[0], vec1[1]+ vec2[1]]


def addressConverter(address): #converts coordinate array to corresponding address form
    coordinate = address.split('_')
    return [int(coordinate[0]), int(coordinate[1])]


def getNeighbourAddress(Grid, currentAddress, pointerList):
    currentNode = Grid.access(currentAddress)
    neighbour = []

    for pointer in pointerList: # takes different vectors
        new = vectorSum(currentNode.coordinates,pointer) #vectors give direnction so adding new direction to current location
        
        if 0<=new[0]<Grid.rowSpan and  0<=new[1]<Grid.colSpan: #checking if it's valid. prevents infinite loop
            
            newAddress = str(new[0])+'_'+ str(new[1])
            neighbour.append(newAddress)

    return neighbour

class Node:
    def __init__(self, coordinates, display, address):
        self.coordinates = coordinates
        
        self.pointers = [[1,0], [1,1], [0,1], [-1,1], [-1,0], [-1,-1], [0, -1], [1,-1]]
        self.constructionPointers = [[1,0], [1,1], [0,1]]
        #Just a really choppy algorithm
        #construction pointers are vectors only to be used for construction purposes. only 3 are neede so ive optimized it for that purpose
        # look at the __init__ part in Grid class for further clarification. Line 75 ig

        self.address = address
        self.internal = '   '
        self.displayValue = display
    

class Grid:
    def __init__(self, rowSpan, colSpan, default):

        print('constructing Grid: ')
        self.head = Node([0,0], default, '0_0' )
        self.nodes = {
            '0_0': self.head,
            }
        self.queue = deque()
        self.queue.append('0_0')
        self.default = default

        self.rowSpan = rowSpan
        self.colSpan = colSpan

        self.expanded =set([])

        # Tried doing this for debugging attempts doesnt seem to work using for. dunno why
        # for i in range(100):

        # A BFS algorithm. based on vector addition to get new addresses
        # runs through valid values of coordinates and creates instances of them stored inside of the nodes dictionary 

        while self.queue:
            currentAddress = self.queue.pop()

            if currentAddress not in self.nodes:

                currentCoordinate = addressConverter(currentAddress)
                # print(currentCoordinate)

                self.nodes[currentAddress] = Node(currentCoordinate, default, currentAddress) #assignment i.e. access() method cant be used. hmm
                # print(self.queue)
                
            for address in getNeighbourAddress(self, currentAddress, self.access(currentAddress).constructionPointers): 

                if address not in self.nodes:

                    self.queue.append(address)
                    # print('address', address)
                
    
    def access(self, address):
        return self.nodes[address]
    
# display and internal methods print the board on the console
#display shows what players see
#internal shows the real things inside the box
# useful for debugging the program since it shows everything like bomb location and number indicators
    def display(self):

        print("\nDisplay Grid:")
        print('    ', end='|')
        for i in range(0,self.colSpan):
            
            if len(str(i)) ==1:
                string = "\033[34m"+' '+ str(i) +' '+ "\033[0m"
                print(string, end='|')
            else:
                
                string = "\033[34m"+ str(i) +' '+ "\033[0m"
                print(string, end='|')
        print('\n--------------------------------------------')
        
        for i in range(self.rowSpan):
            if len(str(i))==2:
                print("\033[34m"+' '+str(i)+' '+ "\033[0m", end='|')
            elif len(str(i))==1:
                print("\033[34m"+'  '+str(i)+' '+ "\033[0m", end='|')

            for j in range(self.colSpan):
                address = str(i)+'_'+ str(j)
                print(self.access(address).displayValue, end='|')
            print('\n--------------------------------------------')

    def internal(self):
        print("\nInternal Grid:")
        print('    ', end='|')
        for i in range(0,self.colSpan):
            
            if len(str(i)) ==1:
                string = "\033[34m"+' '+ str(i) +' '+ "\033[0m"
                print(string, end='|')
            else:
                
                string = "\033[34m"+ str(i) +' '+ "\033[0m"
                print(string, end='|')
        print('\n--------------------------------------------')
        
        for i in range(self.rowSpan):
            if len(str(i))==2:
                print("\033[34m"+' '+str(i)+' '+ "\033[0m", end='|')
            elif len(str(i))==1:
                print("\033[34m"+'  '+str(i)+' '+ "\033[0m", end='|')

            for j in range(self.colSpan):
                address = str(i)+ '_'+str(j)
                print(self.access(address).internal, end='|')
            print('\n--------------------------------------------')      

    def neighbourhood(self, currentAddress):
        neighbours = getNeighbourAddress(self, currentAddress,self.access(currentAddress).pointers)
        return neighbours


# methods for changing the values
    def updateDisplay(self, currentAddress, newValue):
        self.access(currentAddress).displayValue = newValue

    def updateInternal(self, currentAddress, newValue):
        self.access(currentAddress).internal = newValue

#EXECUTION CODE:
# counter = 0
# board = Grid(10,10, '   ')
# board.display()

