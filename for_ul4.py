n= int(input("zadaj cislo n: "))
v = 0
for i in range(1,n+1):
    v += i
    print(i, end =",")
print("Súčet čísel od 1 do n je:",v)
