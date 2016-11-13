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
    (data.empty, data.Hcolor)= (None, "grey")
    (data.margin, data.Hlevel) = (100, 3)
    (data.rows, data.cols) = (10, 16)
    data.count = 0
    data.board = make2dList(data)
    data.board1 = make2dList(data)
    data.board2 = make2dList(data)
    (data.stickWidth, data.hanoiS) = (20, 690)
    data.gap = (data.hanoiS - data.stickWidth*3)/3
    (data.blockY, data.blockX) = (50, (data.gap + data.stickWidth)/16)
    data.scrollbarX = 780
    data.speed = (data.scrollbarX-780)//100
    data.step=0
    data.steps=recursiveHanoi(data, data.Hlevel)
    data.explanation="Haha"

def firstSecondThird(number):
    result = ""
    if(number == 1): result = "First"
    elif(number == 2): result = "Second"
    elif(number == 3): result = "Third"
    else: result = (str(number) + "th")
    return result

def findDisc(data, depth):
    if(depth != data.Hlevel- 1):
        disc = data.Hlevel - depth + 1
    else:
        if(data.count % 2 == 1):
            return 1
        else:
            return 2
    return disc

def recursiveHanoi(data, n, source=0, target=1, temp=2, depth=0):
    if (n == 1):
        data.count += 1
        if(depth != data.Hlevel - 1):
           data.count = 0
        stick = ["", ""]
        stick[0] = firstSecondThird(source + 1)
        stick[1] = firstSecondThird(target + 1)
        disc = firstSecondThird(findDisc(data, depth))
        print("Move the %s disc from %s stick to %s stick" 
            % (disc, stick[0], stick[1])) 
        print("recursiveHanoi(source=%d, target=%d, depth=%d)"
            % (source, target, depth))
        return [(source, target)]
    else:
        return (recursiveHanoi(data, n-1, source, temp, target, depth + 1) +
                recursiveHanoi(data, 1, source, target, temp, depth + 1) +
                recursiveHanoi(data, n-1, temp, target, source, depth + 1))

def mousePressed(event, data):
    if 720 <= event.x <= 770 and 150 <= event.y <= 200 and data.Hlevel - 1 >= 0:
        Hlevel=data.Hlevel-1
        init(data)
        data.Hlevel =Hlevel
    elif 930 <= event.x <= 980 and 150 <= event.y <= 200 and data.Hlevel + 1 <= 8:
        Hlevel=data.Hlevel+1
        init(data)
        data.Hlevel =Hlevel
    elif 720 <= event.x <= 980 and 210 <= event.y <= 260:
        init(data)
    elif 720 <= event.x <= 980 and 270 <= event.y <= 320:
        pass
    elif 720 <= event.x <= 770 and 390 <= event.y <= 440 and 790 <= data.scrollbarX:
        data.scrollbarX -= 5
    elif 930 <= event.x <= 980 and 390 <= event.y <= 440 and 910 >= data.scrollbarX:
        data.scrollbarX += 5
    elif 780 <= event.x <= 920 and 390 <= event.y <= 440:
        data.scrollbarX = event.x - 15
    elif 720 <= event.x <= 770 and 510 <= event.y <= 560 and data.step - 1 >= 0:
        data.step -= 1
    elif 930 <= event.x <= 980 and 510 <= event.y <= 560 and data.step + 1 <= 8:
        data.step += 1

def keyPressed(event, data):
    pass

def timerFired(data):
    pass

def drawCell(canvas,data,row,col,color,change):
    cx = change + data.blockX * col
    cy = 200 + data.blockY * row
    cxBottom = cx + data.blockX
    cyBottom = cy + data.blockY
    canvas.create_rectangle(cx, cy, cxBottom, cyBottom, 
                            fill = color, width=0)
    if data.board[row][col] == "grey":
        canvas.create_line(cx,cyBottom-1,cxBottom,cyBottom-1,fill="black",width=2)

def drawCell1(canvas,data,row,col,color,change):
    cx = change + data.blockX * col
    cy = 200 + data.blockY * row
    cxBottom = cx + data.blockX
    cyBottom = cy + data.blockY
    canvas.create_rectangle(cx, cy, cxBottom, cyBottom, 
                            fill = color, width=0)
    if data.board1[row][col] == "grey":
        canvas.create_line(cx,cyBottom-1,cxBottom,cyBottom-1,fill="black",width=2)

def drawCell2(canvas,data,row,col,color,change):
    cx = change + data.blockX * col
    cy = 200 + data.blockY * row
    cxBottom = cx + data.blockX
    cyBottom = cy + data.blockY
    canvas.create_rectangle(cx, cy, cxBottom, cyBottom, 
                            fill = color, width=0)
    if data.board2[row][col] == "grey":
        canvas.create_line(cx,cyBottom-1,cxBottom,cyBottom-1,fill="black",width=2)

def drawDiscs(canvas, data):
    start = data.cols//2 - data.Hlevel
    for row in range(data.rows-1, data.rows - data.Hlevel-1, -1):
        for col in range(start, data.cols - start): 
            data.board[row][col] = data.Hcolor
        start += 1

def drawBoard(canvas, data):
    for row in range(data.rows):
        for col in range(data.cols):
            drawCell(canvas, data, row, col, data.board[row][col],0)
    for row in range(data.rows):
        for col in range(data.cols):
            drawCell1(canvas, data, row, col, data.board1[row][col],
                data.gap + data.stickWidth)
    for row in range(data.rows):
        for col in range(data.cols):
            drawCell2(canvas, data, row, col, data.board2[row][col],
                2 * data.gap + 2 * data.stickWidth)

def drawStick(canvas, data):
    margin = 200
    canvas.create_rectangle(data.gap/2, margin, data.gap/2 + data.stickWidth, 
        data.hanoiS, fill = "dark orange")
    canvas.create_rectangle(1.5*data.gap + data.stickWidth , margin, 
        1.5*data.gap + data.stickWidth*2, data.hanoiS, fill = "dark orange")
    canvas.create_rectangle(2.5*data.gap + 2*data.stickWidth , margin, 
        2.5*data.gap + 3*data.stickWidth, data.hanoiS, fill = "dark orange")


def drawBackground(canvas,data):
    canvas.create_rectangle(0, 10, 1000, 790,  fill="grey")
    canvas.create_rectangle(0, 50, data.hanoiS, data.hanoiS, fill="black")

    canvas.create_rectangle(0,10,1000,790,fill="grey")
    canvas.create_rectangle(0,50,700,690,fill="black")
    #title
    canvas.create_text(100,30,text="Tower of Hanoi",font="Arial 24")
    #discs
    canvas.create_text(850,125,text="DISCS",font="Arial 24")
    #level choose
    # -
    canvas.create_rectangle(720,150,770,200,fill="white",width=0)
    canvas.create_text(745,175,text="-",font="Arial 24")
    # +
    canvas.create_rectangle(930,150,980,200,fill="white",width=0)
    canvas.create_text(955,175,text="+",font="Arial 24")
    #level
    canvas.create_rectangle(780,150,920,200,width=2,outline="white")
    canvas.create_text(850,175,text=data.Hlevel,font="Arial 24")
    #restart
    canvas.create_rectangle(720,210,980,260,fill="white",width=0)
    canvas.create_text(850,235,text="RESTART",font="Arial 24")
    #automatic
    canvas.create_rectangle(720,270,980,320,fill="white",width=0)
    canvas.create_text(850,295,text="PLAY",font="Arial 24")
    #speed
    canvas.create_text(850,355,text="SPEED",font="Arial 24")
    #slow
    canvas.create_rectangle(720,390,770,440,fill="white",width=0)
    canvas.create_text(745,415,text="<<",font="Arial 24")
    #fast
    canvas.create_rectangle(930,390,980,440,fill="white",width=0)
    canvas.create_text(955,415,text=">>",font="Arial 24")
    #scrollbar
    canvas.create_line(780,415,920,415,fill="black",width=5)
    canvas.create_rectangle(data.scrollbarX,390,data.scrollbarX+25,440,
                        fill="light grey",width=0)
    #step choose
    canvas.create_text(850,475,text="STEPS",font="Arial 24")
    # last
    canvas.create_rectangle(720,510,770,560,fill="white",width=0)
    canvas.create_text(745,535,text="-",font="Arial 24")
    # next
    canvas.create_rectangle(930,510,980,560,fill="white",width=0)
    canvas.create_text(955,535,text="+",font="Arial 24")
    # step
    canvas.create_rectangle(780,510,920,560,width=2,outline="white")
    canvas.create_text(850,535,text=data.step,font="Arial 24")
    #Explanation
    canvas.create_rectangle(100,710,650,770,fill="black",width=0)
    canvas.create_text(110,740,anchor=W,text=data.explanation,
        font="Arial 24",fill="white")

def redrawAll(canvas, data):
    drawBackground(canvas,data)
    drawStick(canvas, data)
    drawBoard(canvas, data)
    drawDiscs(canvas,data)

def run(width=1000, height=800):
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

run()