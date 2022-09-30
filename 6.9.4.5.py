# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

исправленный кусок задачи

f = open('dz40.txt', 'r')
list_5 = str(f.readline()).split('+')
c1=b1=a1=0
if 'x' not in list_5[1]:
    c1 = list_5[len(list_5)]
    print(c1) 
if 'x' in list_5[1]:
    b1 = list_5[1][:1] 
a1 = list_5[0][:4]
print(a1)
f.close()
        