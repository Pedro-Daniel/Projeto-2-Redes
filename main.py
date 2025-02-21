from ipaddress import IPv4Network
import Rede

network=Rede.Rede()

nos=["c1","a1","a2",
     "e1","e2","e3","e4",
     "h1","h2","h3","h4","h5","h6","h7","h8"
	]
links=[
    ("c1","a1"),("a1","e1"),("a1","e2"),("e1","h1"),("e1","h2"),("e2","h3"),("e2","h4"),
    ("c1","a2"),("a2","e3"),("a2","e4"),("e3","h5"),("e3","h6"),("e4","h7"),("e4","h8"),
	]

net_c1    = IPv4Network("10.0.?.?/30") #2 subredes

subnet_a1 = IPv4Network("10.0.?.?/30") #4 subredes
subnet_a2 = IPv4Network("10.0.?.?/30") #4 subredes

subnet_e1 = IPv4Network("10.0.1.0/27") #32 hosts
subnet_e2 = IPv4Network("10.0.2.0/27") #32 hosts
subnet_e3 = IPv4Network("10.0.3.0/28") #16 hosts
subnet_e4 = IPv4Network("10.0.4.0/28") #16 hosts


for _ in links:
    no1=_[0]
    no2=_[1]
    network.adicionar_link(no1,no2)

network.printar()
