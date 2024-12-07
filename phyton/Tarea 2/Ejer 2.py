continuar=True
max= 0
min= float("inf")
media= 0
n= 0
while continuar== True:
    esPrimo = True
    num= int(input("Inserte N:"))
    if num<= 1:
        break
    for i in range (2,num):
        if num % i == 0:
            esPrimo=False
    if esPrimo==True:   
        break
    n=n+1
    media= media+num
    if max<num:
        max=num
    if min>num:
        min=num
media= media/n
print ("min:", min)
print ("max:", max)
print ("media:", media)
