from mininet.cli import CLI
from mininet.net import Mininet
from mininet.node import RemoteController

#controller c0 並不存在，需要編寫相應的code
if '__main__' == __name__:
    net = Mininet(contronller=RemoteController)

    c0 =net.addController('c0',ip='Contreller ip', port=1234)

    s0 = net.addSwitch('s0')  #加入switch0-3
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')
    s3 = net.addSwitch('s3')

    h1 = net.addHost('h1', mac='00:00:00:00:00:01')     #加入host
    h2 = net.addHost('h2', mac='00:00:00:00:00:02')
    h3 = net.addHost('h3', mac='00:00:00:00:00:03')
    h4 = net.addHost('h4', mac='00:00:00:00:00:04')
    h5 = net.addHost('h5', mac='00:00:00:00:00:05')

    net.addLink(s0, s1, port1=1, port2=1)    #switch之間連綫
    net.addLink(s0, s2, port1=1, port2=1)
    net.addLink(s0, s3, port1=1, port2=1)
    net.addLink(s1, s3, port1=2, port2=2)
    net.addLink(s2, s3, port1=2, port2=3)


    net.addLink(s0, h1, port1=2, port2=1)      #switch與host之間連綫
    net.addLink(s1, h2, port1=3, port2=1)
    net.addLink(s2, h3, port1=3, port2=1)
    net.addLink(s3, h4, port1=4, port2=1)
    net.addLink(s3, h5, port1=5, port2=1)

    net.build()  #建立mininet

    c0.start()  #啓動controller

    s0.start(c0)  #啓動switch並指定controller c0
    s1.start(c0)
    s2.start(c0)
    s3.start(c0)
    #之後需要加入flow table等一些code

    CLI(net)

    net.stop()