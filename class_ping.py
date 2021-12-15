from scapy_ping_one_new import qytang_ping
import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)
from kamene.all import *
class QYTPING:
    def __init__(self, dstip,length=100,srcip='117.187.210.84'):
        self.srcip = srcip
        self.dstip = dstip
        self.srcip = srcip
        self.length = length
    def one(self):
        result = qytang_ping(self.dstip)
        if result[1]:
                print(f'{result[0]} 可达!')
        else:
                print(f'{result[0]} 不可达!')
    def ping(self):
        ping_pkt = IP(src=self.srcip,dst=self.dstip)/ICMP()
        ping_result = sr1(ping_pkt,timeout=2,verbose=False)
        if ping_result:
                print('!!!!!')
        else:
                print('.....')

    def __str__(self):
        if self.srcip == '117.187.210.84':
            return f'<{self.__class__.__name__} => dstip: {self.dstip}, size: {self.length}>'
        else:
            return f'<{self.__class__.__name__} => srcip: {self.srcip}, dstip: {self.dstip}, size: {self.length}>'

class NewPing(QYTPING):
    def ping(self):
        ping_pkt = IP(src=self.srcip,dst=self.dstip)/ICMP()
        ping_result = sr1(ping_pkt,timeout=2,verbose=False)
        if ping_result:
            print('+++++')
        else:
            print('?????')


if __name__ == '__main__':
    ping = QYTPING('114.114.114.114') # 使用类QYTPING，产生实例
    total_le = 70

    def print_new(word,s='-'):
        print('{0}{1}{2}'.format(s * int((70 - len(word))/2), word, s * int((70 - len(word))/2)))
    print_new('print class')
    print(ping) #打印类
    print_new('ping one for sure reachable')
    ping.one() #判断一个包的可达性
    print_new('ping five')
    ping.ping() #模拟正常ping程序ping五个包，'!'表示通，'.'表示不通
    print_new('set payload lenth')
    ping.length = 200 #设置负载长度
    print(ping) #打印类
    ping.ping() #使用修改长度的包进行ping测试
    print_new('set ping src ip address')
    ping.srcip = '192.168.1.123' #修改源IP地址
    print(ping)
    ping.ping() #使用修改长度又修改源的包ping测试
    print_new('new class NewPing','=')
    newping = NewPing('114.114.114.114')
    newping.length = 300
    print(newping) #打印类
    newping.ping() # NewPing类自定义过ping()这个方法，'+'表示通，'?'表示不通

