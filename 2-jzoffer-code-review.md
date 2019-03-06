### TIPS
- 0 int [] array  数组自带属性。C/C++ 使用sizeof()
  - array.length
- pow()
- java.lang包是由解释器自动导入的。主要包括
- 1.Collections 在java.util里
   - 1 ArrayList
     
   - 2 Stack
    - empty()
    - pop()
    - push()
    - peek() 栈顶值
    - 
- - Queue接口与List、Set同一级别，都是继承了Collection接口。LinkedList实现了Queue接 口。Queue接口窄化了对LinkedList的方法的访问权限（即在方法中的参数类型如果是Queue时，就完全只能访问Queue接口所定义的方法 了，而不能直接访问 LinkedList的非Queue的方法），以使得只有恰当的方法才可以使用。
### 题目
- 1.旋转数组最小的值
- 2.变态跳台阶  
 - https://www.nowcoder.com/practice/22243d016f6b47f2a6928b4313c85387?tpId=13&tqId=11162&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
- 3.二进制中1的个数
 - 右移然后与1做与计数即可。或者n与n-1做与运算
- 4.栈的压入 弹出序列
 - https://www.nowcoder.com/practice/d77d11405cc7470d82554cb392585106?tpId=13&tqId=11174&tPage=2&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
- 5.最小的K个数。本质就是排序算法。
https://www.nowcoder.com/practice/6a296eb82cf844ca8539b57c23e6e9bf?tpId=13&tqId=11182&tPage=2&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
- 6.把数组排成最小的数
- https://www.nowcoder.com/practice/8fecd3f8ba334add803bf2a06af1b993?tpId=13&tqId=11185&tPage=2&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
这个问题的解法主要是由这么一个理论即:最小的数结合的时候肯定是在最左边，类似于贪心算法。此次结合这俩数这么排是最小 那么在任何形式里面 他俩这么排还是最小。
- 7.第K个丑数
- https://www.nowcoder.com/practice/6aa9e04fc3794f68acf8778237ba065b?tpId=13&tqId=11186&tPage=2&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
- 8.数组中的逆序对
- https://www.nowcoder.com/practice/96bd6684e04a44eb80e6a68efc0ec6c5?tpId=13&tqId=11188&tPage=2&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
>> 模运算的性质:
( a + b ) % c = ( ( a % c ) + ( b % c ) ) % c
( a * b ) % c = ( ( a % c ) * ( b % c ) ) % c
( a – b ) % c = ( ( a % c ) – ( b % c ) ) % c
( a / b ) % c NOT EQUAL TO ( ( a % c ) / ( b % c ) ) % c
(a / b ) % c = ( a * b^ -1 ) % c
the answer ( a % b) always be less than b.
基本上是要记住上面这几条的，基本够用。。而b经常取的数为一个比较大的素数。