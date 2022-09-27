a = int(input("zadaj začiatok intervalu:" ))
b = int(input("zadaj koniec intervalu:" ))
v = 0
for i in range(a,b+1):
    if i%8 ==0 and i!=0:
        v +=1
print("Počet čísel deliteľných 8 je:",v)
