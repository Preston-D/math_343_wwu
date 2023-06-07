y1 = 0.77175
ya = 0.76509
yb = 0.55811
yab = 0.50524
yc = 0.23177
yac = 0.22599
ybc = 0.14187
yabc = 0.11824

std_order = [y1, ya, yb, yab, yc, yac, ybc, yabc]

contrasts = [
    [1,1,1,1,1,1,1,1], #I
    [-1,1,-1,1,-1,1,-1,1], #A
    [-1,-1,1,1,-1,-1,1,1], #B
    [1,-1,-1,1,1,-1,-1,1], #AB
    [1,1,1,1,-1,-1,-1,-1], #C
    [1,-1,1,-1,-1,1,-1,1], #AC
    [1,1,-1,-1,-1,-1,1,1], #BC
    [-1,1,1,-1,1,-1,-1,1]  #ABC
    ]
    
for c in contrasts:
    # effect = ((c[0]*y1) + (c[1]*ya) + (c[2]*yb) + (c[3]*yab) + (c[4]*yc) + (c[5]*yac) + (c[6]*ybc) + (c[7]*yabc))/4
    effect = 0
    for i in [0,1,2,3,4,5,6,7]:
        temp = (std_order[i] * c[i])
        # print(temp)
        effect += temp
    effect = (effect/4)/2
    print(effect)
