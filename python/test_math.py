from numpy import matrix
import random

class Board:
    def __init__(self, board_size):
        self.board_size = board_size

        #Make the Board
        board_string = "" #Used to init the matrix
        # Set Row Positions
        hoz = "["
        vert = ""
        for i in range(self.board_size):
            """ Generate the board generating string as inefficently as possible """
            row = ""
            for x in range(self.board_size):
                row = row + "0 "
            row = row+";"
            board_string = board_string + row

            # horizontal bar state
            hoz = hoz + "1, "
            # verticle bar state
            vert = vert + "3;"

        self.hoz_bars = matrix(hoz[:-2] + "]")
        self.vert_bars = matrix(vert[:-1])

        self.update_state()
        return

    def update_vert(self):
        vert_str = ""
        row = ""
        for bar in self.vert_bars.flat:
            #val = str(bar) +"," for testing
            val = str(random.randint(0, 5)) +","
            row = row + val
        row = row[:-1]+";"
        vert_str = row*self.board_size

        self.vert_state = matrix(vert_str[:-1])
        return

    def update_hoz(self):
        hoz_str = ""

        for bar in self.hoz_bars.flat:
            #val = str(bar) +"," for testing
            val = str(random.randint(0, 5)) + ","
            row = val*self.board_size # Apply to whole row
            row = "" + row[:-1] + ";"  #package row
            hoz_str = hoz_str + row

        self.hoz_state = matrix(hoz_str[:-1]) #Cleanup

    def update_state(self):

        self.update_hoz()
        self.update_vert()

        self.boardstate = self.hoz_state + self.vert_state



        return

    def move_row(self, row, value):
        #Make matrix to add
        #for i in range(self.size):
        #    adding_matrix = self.blank_state
        return

    """def bars_tostring(self): Prolly will delete this.
        h = "{0}".format(self.hoz_bars)

        h = h.replace("[","").replace(" ","").replace("]","").replace("\n","|\n")
        h = h + "|"
        v = "{0}".format(self.vert_bars)
        v = v.replace("[", "").replace(" ","|").replace("]","")
        bars = h + "\n" + " |"+ v + "|"
        return bars
    """



#### Code to Run
"""
bd = Board(3)

bd.update_vert()
bd.update_hoz()

print("Vert States")
print(bd.vert_state)
print(" "*(bd.board_size+1)+"+")
print("Hoz States")
print(bd.hoz_state)
print(" "*(bd.board_size+1)+"=")
print("Final State")
print(bd.boardstate)
print("..............")
"""



def pin_6d(h1, h2, h3, v1, v2, v3):
    pin = (h1 + h2 + h3 + v1 + v2 + v3)/6
    return pin

def pin_5d (h1, h2, v1, v2, v3):
    pin = (h1 + h2 + h3 + v1 + v2 + v3)/5

def pin_4d(h1, h2, v1, v2):
    pin = (h1 + h2 + v1 + v2)/4
    return pin

up_states = 0
down_states = 0
zero_states = 0
full_states = 0

low = -20
high = 21

full = 10

"""
for h1 in range(low,high):
    for h2 in range(low, side_bar_high):
        for h3 in range(low, side_bar_high):
            for v1 in range(low, high):
                for v2 in range(low, side_bar_high):
                    for v3 in range(low, side_bar_high):
                        pin = pin_6d(h1, h2, h3, v1, v2, v3)
                        if (pin > 0 ):
                            up_states += 1
                        else:
                            down_states += 1
                        if (pin == 0):
                            zero_states += 1
                        elif (pin == high-3):
                            full_states += 1
"""
for h1 in range(low,high):
    for h2 in range(low, high):
        for v1 in range(low, high):
            for v2 in range(low, high):
                pin = pin_4d(h1, h2, v1, v2)
                if (pin > 0 ):
                    up_states += 1
                else:
                    down_states += 1
                if (pin == 0):
                    zero_states += 1
                elif (pin == full):
                    full_states += 1


print("possible states: up={0}, down={1}, 0={2}, full={3}".format(up_states, down_states, zero_states, full_states))

#print("add and then")
