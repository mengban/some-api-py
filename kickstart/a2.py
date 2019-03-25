t = int(input())
for case in range(t):
    n = int(input())
    s = input()
    l = []
    for i in range(len(s)):
        l.append(int(s[i]))
    # print(l)
    l1 = (n+1)//2
    count = sum(l[:l1])
    temp = count
    for i in range(l1,len(l)):
        temp = temp + l[i] - l[i-l1]
        count = max(count,temp)
    print("Case #",end='')
    print(case+1,end='')
    print(": ",end='')
    print(count)
    