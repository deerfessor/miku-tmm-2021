import random
def d_car() :  #возвращает длину машины
    a=random.random()
    if a<0.20 :
        b=3.5
    elif a<0.4 :
        b=4.5
    else :
        b=4
   #print(b+(random.random()%(0.5))+0.01)
    return (b+(random.random()%(0.5))+0.01)  

def car_placer(open_space,count2) :  #возвращает колличество машин на участке
    car=d_car()
    while (open_space - 1.2) > car :
        c=random.random()
        if c<0.7 :                       # машина встала в край зоны , 0.7 заменить на вероятность этого
            open_space=open_space - car - 1.2
            count2+=1
            car=d_car()
        else :                           # машина встала посреди зоны
            d=random.random()      
            open_space2=(open_space - 1.2 - car)*d  # вторая половина
            open_space=open_space-open_space2       # первая половина
            count2+=1
            count2=(car_placer(open_space2,count2))  # количество машин на второй половине
            car=d_car()
    return count2
area=float(input())
repetition = int(input())    #число повторений
useful_1=area//6.5  #машины при первом варианте
useful_2=0          #машины при втором варианте
useful_2=car_placer(area,useful_2)
for t in range(repetition) :     
    useful_2=car_placer(area,useful_2)
    useful_1+=useful_1
print(useful_1/useful_2) #если >1 то первый вариант эффективней
print(useful_1)      #машины при первом варианте
print(useful_2)      #машины при втором варианте
