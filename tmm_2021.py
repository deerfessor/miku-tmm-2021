import random
def d_car() :  #длина машины
    a=random.random()
    if a<0.25 :
        b=3.5
    elif a<0.5 :
        b=4
    else :
        b=4.5
    return (b+(random.random()%(0.5))+0.01)    
area=float(input())
useful_1=area//6.5
useful_2=0
car=d_car()
while (area - 1.2) > car :
    area=area - car - 1.2
    useful_2+=1
    car=d_car()
print(useful_1)
print(useful_2,area)
