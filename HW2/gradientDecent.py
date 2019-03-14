def gradDecent(gradFunc,learningRate,start,limit=1000000):
    x, y = start
    for i in range(0,limit):
        dx, dy = gradFunc(x,y)
        if dx==0 and dy==0:
            break
        x -= dx*learningRate
        y -= dy*learningRate
    return x, y

if __name__ == "__main__":
    f = lambda x, y : (10*x)**2 + (y + 2)**2
    gradF = lambda x, y : (200*x, 2*(y+2))

    g = lambda x, y : (x-10)**2 + (x - y + 5)**4
    gradG = lambda x, y : (2*(2*(x - y + 5)**3 + x - 10), -4*(x - y + 5)**3)

    resF=gradDecent(gradF,0.5,(0,0),10)
    print("After 10 itterations, x is {} and y is {}, making f(x,y)={}".format(
        resF[0],
        resF[1],
        f(resF[0],resF[1])
    ))
    resG=gradDecent(gradG,0.005,(0,0),10)
    print("After 10 itterations, x is {} and y is {}, making g(x,y)={}".format(
        resG[0],
        resG[1],
        g(resG[0],resG[1])
    ))