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