def maxInWindow(nums,size):
    """queue 只保存角标
    >>> [2,3,4,2,6,2,5,1]
    
    """
    
    _max = []
    queue = [] 
    for i in range(size): 
        queue.append(i)
    while(nums[queue[len(nums) - 1]] > nums[queue[0]] ): #前面只保留比队列尾大的数
        queue.pop()
    
    _max.append(nums[queue[0]]) #第一个max
    
    while(size<len(nums) - 1 ): #开始出队列
        while(nums[size] > nums[queue[0]]): #新数据大 将队列删除
            queue.pop()
        queue.apend(size)
        while():
            pass
        
        
        
        
        size += 1

nums = [2,3,4,2,6,2,5,1]
maxInWindow(nums,3)

nums = [2,3,4,1,6,8]
def insert_sort(arr):
    _len = len(arr)
    index = [_ for _ in range(_len) ] #保存角标
    print(index)
    for i in range(1,_len):
        if arr[i-1] > arr[i]: #如果比前面的小
            for j in range(0,i):
                if arr[i-j-1] > arr[i-j]: #交换
                    tmp = arr[i-j]
                    arr[i-j] = arr[i-j-1]
                    arr[i-j-1] = tmp
                else:
                    break
        else:
            continue
    return arr
print(insert_sort(nums))


nums = [5,3,4,1,6,8]
def insert_sort(arr):
    _len = len(arr)
    ret = []
    index = [_ for _ in range(_len) ] #保存角标
    #print(index)
    for i in range(1,_len):
        if arr[index[i-1]] > arr[index[i]]: #如果比前面的小
            for j in range(0,i):
                if arr[index[i-j-1]] > arr[index[i-j]]: #交换
                    tmp = index[i-j]
                    index[i-j] = index[i-j-1]
                    index[i-j-1] = tmp
                else:  #right pos
                    print('pos',arr[index[i-j]])
                    ab1 = abs(arr[index[i-j]] - arr[index[i-j - 1]])
                    ab2 = abs(arr[index[i-j]] - arr[index[i-j + 1]])
                    if ab2 > ab1:
                        ret.append([ab1,i-j -1])
                    else:
                        ret.append([ab2,i-j + 1])
                    break
        else:
            print('xx',arr[index[i-1]])
            ret.append([abs(arr[index[i-1]] - arr[index[i]]),i - 1 ])
            continue
    #print('index',index)
    return ret
print(insert_sort(nums))




arr = [1,9,8,2,3,5,4]
ret = []
for index,item in  enumerate(arr):
    ret.append((index,item))
print(sorted(ret,key = lambda x : x[1]))

