
file = open('font3.txt', 'r')
d={}
for line in file:
    x = line.split(",")
    a=x[0]
    b=x[1]
    c=len(b)-1
    b=b[0:c]
    d[a]=b

dictA=d
def GetKey(val):
    for key, value in dictA.items():
        if val == value:
            return key
input= input("please press any key")

print(GetKey('F'))
print(GetKey('G'))
print(GetKey('H'))
