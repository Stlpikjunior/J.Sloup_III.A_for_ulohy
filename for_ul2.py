n= int(input("zadaj číslo n:"))
s = 0
for i in range(1,n+1):
    if i%2 ==0:
        print(i, end = ",")
        s +=i
print ("\nSúčet všetkých párnych čísel do n je: ",s)
