from multiprocessing import Process,Queue
import random,time,os 

def procducer(q):
    for i in range(50):
        res = '视频%s' %i
        time.sleep(0.1)
        q.put(res)
        print('%s 读取 %s' %(os.getpid(),res))

def consumerPost(q,q2):
    while True:
        res = q.get()
        if res is None:
            break
        q2.put(res + 'Response')
        print('%s Post %s' %(os.getpid(),res))
        time.sleep(random.randint(1,2))
def consumerWrite(q2):
    print(q2)
    try :
        while True:
            res = q2.get(timeout = 2)  # wait 1s
            print('%s write %s' %(os.getpid(),res))
            time.sleep(random.random()/2)
    except Exception:
        print('Write Done!')

if __name__ == '__main__':
    q = Queue()
    q2 = Queue()
    p = Process(target=procducer,args=(q,))
    p.start()
    ProcessNumber = 5
    for i in range(ProcessNumber):
        c = Process(target=consumerPost,args=(q,q2))
        c.start()

    pw = Process(target=consumerWrite,args=(q2,))
    pw.start()

    p.join() # 等待p完成
    for i in range(ProcessNumber):
        q.put(None)

    print('Main Done.')

