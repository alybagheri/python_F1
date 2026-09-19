chess = set(["ali" , "mohsen" , "sadegh" , "tara" , "alireza" , "masoud" , "tina"])
classes = set(["1" , "2" , "2" , "3" , "4" , "4" , "5" , "5"])

print(type(chess))
print(chess)


print(classes)
classes.add(18)
print(classes)
#---------practice-------------#

SetA = {1, 2, 3, 4}
SetB = {3, 4, 5, 6}


print(type(SetA))
print(SetA)

Unions = SetB.union(SetA)
print(Unions)
InterS = SetB.intersection(SetA)
print(InterS)


#------------------
servers = {"web-01", "web-02", "web-02"}
print(servers)

ips = [
    "192.168.1.10",
    "192.168.1.20",
    "192.168.1.10",
    "192.168.1.30",
    "192.168.1.20",
]

unique_ips = set(ips)
print(unique_ips)



allowed_ports = {22, 80, 443}

if 443 in allowed_ports: print("HTTPS is allowed")


