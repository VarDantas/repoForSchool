for A in range(500):
    k = 0
    for x in range(500):
        for y in range(500):
            if (x>=27) or (2*x<3*y) or (A > (x+2)*(y-3)):
                k += 1
    if k == 250000:
        print(A)
        break
                


