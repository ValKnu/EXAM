
import csv
from distutils.log import error
import errno

fileN='dataT.csv'

# def perevirka(n):
#     while (int (n)<=0 or n==str):
#         print ("Введіть число білье 0")
#         p=input()
#     retu

def obchusl(n):
    summ=0
    n = int(n)
    while(n>0):
        summ+=n*5
        n-=1
    return summ

if __name__ == "__main__":
    print("Введіть кількість перших n чисел які потрібно додати")
    k=input()
    print("Сума першиш n елементів = ", obchusl(k))
    
