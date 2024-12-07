num= (input("Inserte Numero:"))
Dis=""
for i  in num :
    x= int(i)
    if x%2== 0:
        x=x+1
    else:
        x= x-1
    y=str(x)
    Dis += y
print("Tu numero Dislocado es:", Dis)
