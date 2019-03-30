t = int(input())
for case in range(t):
    _str = input()
    R,C = int(_str.split()[0]),int(_str.split()[1])
    mar = []
    for r in range(R):
        _str = input()
        mar.append([int(item) for item in _str ])
    one = []
    for i in range(R):
        for j in range(C):
            if mar[i][j] == 1:
                one.append((i,j))
    k = 0
    kuozhang = []
    while k<(R+C-2):
        if sum([sum(row) for row in mar]) == R * C:
            break
        else:
            for item in one:
                if item[0] - 1 >= 0 :
                    kuozhang.append((item[0]-1,item[1]))
                if item[0] + 1 <=R - 1:
                    kuozhang.append((item[0]+1,item[1]))
                if item[1] - 1 >= 0 :
                    kuozhang.append((item[0],item[1]-1))
                if item[1] + 1 <=C - 1:
                    kuozhang.append((item[0],item[1]+1))
            one = kuozhang[:] #next one
        for item in kuozhang:
            mar[item[0]][item[1]] = 1
        #print('kuozhang',mar)
        
        zero = []
        for i in range(R):
            for j in range(C):
                if mar[i][j] == 0:
                    zero.append((i,j))
        all1 = True
        for i in range(len(zero)):
            left0 = zero[:i] + zero[i+1:]
            for item in left0:
                dis= abs(zero[i][0] - item[0]) + abs(zero[i][1] - item[1])
                if dis > k:
                    all1 = False
                    break
                    
        if all1 == True and len(zero)!=1:
            break
        
        k +=1
    print("Case #",end='')
    print(case+1,end='')
    print(": ",end='')
    print(k)