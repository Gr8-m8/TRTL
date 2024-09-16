import turtle as ttrtl
import random

xc = 0
yc = 1
maxforward = 50
maxturn = 180
trtls = []
ssize = ttrtl.screensize()

def init():
    
    match input("Type [1, 2, 3]: "):
        case "1":
            trtlnr = 1
        case "2":
            trtlnr = 2
        case "3":
            trtlnr = 4
        case _:
            trtlnr = 4

    for t in range(trtlnr):
        trtls.append(ttrtl.Turtle())

    for trtl in trtls:
        trtl.shape('circle')
        trtl.shapesize(0.25, 0.25)
        #turtle.

    main()


def main(rd = 0):
    try:
        turn = -maxturn+random.random()*(2*maxturn)
        forward = random.random()*maxforward
        if len(trtls) >= 1:
            trtls[0].right(turn)
            trtls[0].forward(forward)
        if len(trtls) >= 2:
            trtls[1].right(-turn)
            trtls[1].forward(-forward)
        if len(trtls) >= 4:
            trtls[2].right(turn)
            trtls[2].forward(-forward)
            trtls[3].right(-turn)
            trtls[3].forward(forward)
            
                

        if trtls[0].xcor() < -ssize[xc] or trtls[0].ycor() < -ssize[yc] or trtls[0].xcor() > ssize[xc] or trtls[0].ycor() > ssize[yc]:
            for trtl in trtls:
                trtl.goto(0,0)

        rd+=1
        if rd < 1000:
            main(rd)
        else:
            input("Confirm")
            return
    except KeyboardInterrupt:
        return

init()