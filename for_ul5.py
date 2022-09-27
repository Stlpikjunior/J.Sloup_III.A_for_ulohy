n= int(input("zadaj číslo n:"))
v = 0
for i in range(1,n+1):
    if i%2 ==0:
        v +=1
print ("Počet pármych čísel v intervale od 1 do n je:",v)
