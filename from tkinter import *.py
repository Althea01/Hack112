from tkinter import *

def make2dList(data): 
    board = []
    boardPerRow = []
    for row in range(data.rows):
        for col in range(data.cols):
            boardPerRow.append(data.empty)
        board.append(boardPerRow)
        boardPerRow = [] 
    return board 
    
def init(data):
    (data.empty, data.Hcolor)= ("black", "grey")
    (data.margin, data.Hlevel) = (100, 4)
    (data.rows, data.cols) = (10, 16)
    data.board = make2dList(data)
    (data.stickWidth, data.hanoiS) = (20, 700)
    data.gap = (data.hanoiS - data.stickWidth*3)/3
    (data.blockY, data.blockX) = (50, (data.gap + data.stickWidth)/16)
    

def mousePressed(event, data):
    pass

def keyPressed(event, data):
    pass

def timerFired(data):
    pass

def drawCell(canvas,data,row,col,color):
    change = 200
    cx = data.blockX * col
    cy = change + data.blockY * row
    cxBottom = cx + data.blockX
    cyBottom = cy + data.blockY
    canvas.create_rectangle(cx, cy, cxBottom, cyBottom, 
                            fill = color, width = 0)
def drawDiscs(canvas,data):
    start = data.cols//2 - data.Hlevel
    for row in range(data.rows, data.rows - data.Hlevel , -1):
        for col in range(start, data.cols - start):
            drawCell(canvas, data, row, col, data.Hcolor)
        #canvas.create_line()
        start += 1

def drawBoard(canvas,data):
    for row in range(data.rows):
        for col in range(data.cols):
            drawCell(canvas, data, row, col, data.board[row][col])


def drawBackground(canvas, data):
    canvas.create_rectangle(0, 10, 1000, 790,  fill="grey")
    canvas.create_rectangle(0, 50, data.hanoiS, data.hanoiS, fill="black")

def drawStick(canvas, data):
    margin = 200
    canvas.create_rectangle(data.gap/2, margin, data.gap/2 + data.stickWidth, 
        data.hanoiS, fill = "dark orange")
    canvas.create_rectangle(1.5*data.gap + data.stickWidth , margin, 
        1.5*data.gap + data.stickWidth*2, data.hanoiS, fill = "dark orange")
    canvas.create_rectangle(2.5*data.gap + 2*data.stickWidth , margin, 
        2.5*data.gap + 3*data.stickWidth, data.hanoiS, fill = "dark orange")

def redrawAll(canvas, data):
    drawBackground(canvas, data)
    drawBoard(canvas, data)
    drawStick(canvas, data)
    drawDiscs(canvas,data)


def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='black', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(1000,800)