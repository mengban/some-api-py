t = int(input())
for case in range(t):
    _str = input()
    N,P = _str.split()[0],[1]
    skill = input().split()
    skill = [int(item) for item in skill]
    print(skill)
    skill.sort() #sort
    selected = skill[:P] 
    total = sum([skill[-1] - item for item in skill])
    print("Case #",end='')
    print(case+1,end='')
    print(": ",end='')
    print(total)
