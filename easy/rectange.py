board = [[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
]

print(board)

rectangles = {}
# create a dictionary to keep track of existing rectangles using char as the key and [rows, col], origin as value

def draw_rectangle(char, x1, y1, x2, y2):
    cols = x2 - x1 + 1
    rows = y2 - y1 + 1

    while rows >= 0:
        for col in range(0, cols):
                if col == cols - 1:
                    print (char)
                    # board[rows][col] = char
                else:
                    print (char),
        rows -= 1
    
    rectangles[char] = [rows, cols]

print draw_rectangle('L', 1, 1, 4, 4)
print draw_rectangle('R', 2, 1, 4, 4)
print board
print rectangles


def erase_area(x1, y1, x2, y2):
    cols = x2 - x1 + 1
    rows = y2 - y1 + 1

    while (rows):
        for col in range(0, cols):
                if col == cols - 1:
                    print ("")
                else:
                    print (""),
        rows -= 1
    

print erase_area(2, 1, 4, 4)

def drag_and_drop(x1, y1, x2, y2):
    character = board[x1][y1]
    if character and character in rectangles:
        # erase the old rectangle
        # draw new rectangle from x2, y2 

def print_canvas:
    print (board)


