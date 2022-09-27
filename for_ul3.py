n= int(input("zadaj cislo n: "))
v = 0
for i in range(1,n+1):
    if i%7==0 and i%4==0:
        v += 1
print ("Počet čísel deliteľných 7 aj 4 od 1 do n je:",v)

