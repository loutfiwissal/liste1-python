tab=[]
N=int(input("enter the size of the list: "))
for x in range (N):
    a=int(input("enter a number: "))
    tab.append(a)
for i in range (N):
    min=tab[i]
    for j in range (i,N):
        if min>tab[j]:
           min=tab[j]
           tab[j]=tab[i]
           tab[i]=min
print(tab)