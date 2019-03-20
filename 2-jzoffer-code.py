### 最大滑动窗口
### 基本原则 窗口里的某一元素 其前面的数值一定比他大
def maxInWindow(nums,size):
    """queue 只保存角标
    >>> maxInWindow([2,3,4,2,6,2,5,1])

    """
    
    _max = []
    queue = [] 
    for i in range(size): 
        queue.append(i)
        while nums[queue[len(queue)-1]] > nums[queue[len(queue)-2]]:
            queue.pop(len(queue)-2)  #最后一个数的前面没有比他小的数
    _max.append(nums[queue[0]])
    
    for i in range(size,len(nums)):
        queue.append(i)
        while nums[queue[len(queue)-1]] > nums[queue[len(queue)-2]]:
            queue.pop(len(queue)-2)  #最后一个数的前面没有比他小的数
        if queue[len(queue) - 1] - queue[0] >= size: ## 队尾 与队首差大于窗口长度 则把队首元素踢出去
            queue.pop(0)
        _max.append(nums[queue[0]])
    return _max

### 插入排序
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


## 只出现一次的字符
def appearfirst(_str):
    index = [0 for item in range(256)]
    queue = []
    for ch in _str:
        queue.append(ch)
        index[ord(ch)] += 1
        while len(queue)!=0 and index[ord(queue[0])] > 1:  #保证第一个只出现一次
            queue.pop(0)
        if len(queue) == 0:
            print('#')
        else:
            print(queue[0])
appearfirst("googlehile len(queue)!=0 and index[ord(queue[0])] > 1")
        

