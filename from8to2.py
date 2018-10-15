# -*-coding:utf8;-*-
#qpy:3
#qpy:console

import formulas as syschis

print ("Офлайн перевод из 8-иричной в двоичную системы счисления.")
number = input("Введите 8-иричное число: \n")
print ("\n-------------------------------------\n")
rezul = syschis.vosemTo2(number)
rezult = "".join(str(s) for s in rezul)
print ("Результат: "+rezult)