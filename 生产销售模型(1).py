from  threading import  Thread
import threading
import time


# 全局变量
sum = 500
#你的总钱数
money = 3000
#面包单价
price = 3
# 为了防止厨师的打印比较的混乱，使用厨师的全局锁
# mutex = threading.Lock()

# 为了防止顾客的打印比较的混乱，使用顾客的全局锁
# mutex1 = threading.Lock()
start = time.time() # 获取现在时间

class Consumer(Thread):
    mutex1 = threading.Lock()
    count = 0

    username = ""


    def run(self) -> None:
        # global  mutex1
        global  sum
        while True:
            end = time.time()
            if end - start >= 300:
                SystemExit
            self.mutex1.acquire()  # 当执行该代码后，锁定当前人的打印的程序，其他人的打印暂且先排队，优先打印当前的程序
            if sum > 0 :
                self.count = self.count + 1
                sum = sum  - 1
                #消费的价格
                sum_price = self.count * price
                #剩余价格
                sum_prices = money - sum_price
                if sum_price <= money:
                    print(self.username,"--------------抢了1个面包！还剩",sum,"个面包！！已经买了",self.count,"个面包！","消费了",sum_price,"元","剩余",sum_prices,"元")
                    time.sleep(0.2)
                else:
                    print("您的",money,"已消费完毕！")
                    break
            else:
                print(self.username,"-------------面包不足，请等待2秒钟！",end="")
                for i in range(2):
                    time.sleep(2)
                    print(".",end="")
            self.mutex1.release()


class Chief(Thread):
    mutex = threading.Lock()
    username = ""
    count = 0

    def run(self) -> None:
        global  sum
        while True:
            self.mutex.acquire()  # 当执行该代码后，锁定当前人的打印的程序，其他人的打印暂且先排队，优先打印当前的程序
            if sum < 500:
                sum = sum + 1
                self.count = self.count + 1

                print(self.username , "-------------造了一个面包！还剩",sum,"个面包！已经造了",self.count,"个面包！")
                break

            else:
                print(self.username,"-----------面包篮子已满！请等待2秒.")
                for i in range(2):
                    time.sleep(2)
                    print("",end="")
            self.mutex.release()  # 释放这个打印锁，让排队的其他人继续执行

c1 = Consumer()
c2 = Consumer()
c3 = Consumer()
c4 = Consumer()
c5 = Consumer()
p1 = Chief()
p2 = Chief()
p3 = Chief()
# p4 = Chief()
# p5 = Chief()
p1.username = "李师傅"
p2.username = "王师傅"
p3.username = "纪师傅"
# p4.username = "赵师傅"
# p5.username = "张师傅"
c1.username = "小丽"
c2.username = "小采"
c3.username = "小六"
c4.username = "小美"
c5.username = "小玲"


c1.start()
p1.start()
c2.start()
p2.start()
c3.start()
p3.start()
c4.start()
# p4.start()
c5.start()
# p5.start()


















