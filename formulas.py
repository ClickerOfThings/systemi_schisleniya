# -*-coding:utf-8;-*-
# qpy:3
# qpy:console

def vosemTo2(num):
    error = "error"
    noerror = "noerror"
    for x in num:
        if (x in """89.,;:?!*+=- !@#$%^&*()_+-=~`[]йцукенгшщзхъфывапролджэячсмитьбюqwertyuiopasdfghjkl;zxcvbnm,./\\
            ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮQWERTYUIOPASDFGHJKLZXCVBNM"""):
            # как мне еще проверять наличие символов /\/\ ? внезапный ерор никому не нужен
            return error
    rezultat = []
    desyat = vosemTo10(num)
    print("Перевод из десятичной СС в двоичную:\n")
    while desyat != 0:
        x = desyat % 2
        print("Берем " + str(desyat) + ", делим на 2. Остаток " + str(x) + ". ", end="")
        rezultat.append(x)
        # print ("остаток "+str(x)) #debug
        desyat = desyat // 2
        print("Остается " + str(desyat))
    vrem = "".join(str(s) for s in rezultat)
    print("")
    print("В итоге получается " + str(vrem) + ". Нам это число нужно перевернуть.")
    rezultat.reverse()
    print("\n-------------------------------------\n")
    return rezultat


# -------------

def vosemTo10(num):
    error = "error"
    noerror = "noerror"
    for x in num:
        if (x in """89.,;:?!*+=- !@#$%^&*()_+-=~`[]йцукенгшщзхъфывапролджэячсмитьбюqwertyuiopasdfghjkl;zxcvbnm,./\\
            ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮQWERTYUIOPASDFGHJKLZXCVBNM"""):
            return error
    desyatich = []
    print("Перевод из восьмиричной СС в десятичную:\n")
    kol = len(num)
    kol = kol - 1
    # print ("Моему индусскому коду лень вычислять триадами, поэтому")
    # print ("cначала переводим в десятичные, да-да.\n")
    for x in num:
        x = int(x)
        print("Берем число " + str(x) + ", умножаем на 8 в " + str(kol) + " степени, ", end=" ")
        x = x * (8 ** kol)
        print("получаем " + str(x) + ".")
        desyatich.append(x)
        kol = kol - 1
    # print ("дебаг - десятичные"+str(desyatich)) #debug
    desyat = 0
    for x in desyatich:
        desyat = desyat + x
        # print("сложение "+str(desyat)) #debug
    print("Итоговое десятичное число: " + str(desyat))
    print("\n-------------------------------------\n")
    return desyat

# -------------

def vosemTo16(num):
    error = "error"
    noerror = "noerror"
    for x in num:
        if (x in """.,;:?!*+=- !@#$%^&*()_+-=~`[]йцукенгшщзхъфывапролджэячсмитьбюqwertyuiopasdfghjkl;zxcvbnm,./\\
            ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮQWERTYUIOPASDFGHJKLZXCVBNM"""):
            # как мне еще проверять наличие символов /\/\ ? внезапный ерор никому не нужен
            return error
    rezultat = []
    desyat = vosemTo10(num)
    print("Перевод из десятичной СС в шестнадцатиричную:\n")
    while desyat != 0:
        x = desyat % 16
        print("Берем " + str(desyat) + ", делим на 16. Остаток " + str(x) + ". ", end="")
        if (x == 10 or x == 11 or x == 12 or x == 13 or x == 14 or x == 15):
            y = x
            y = str(y)
            y = y.replace("10", "A")
            y = y.replace("11", "B")
            y = y.replace("12", "C")
            y = y.replace("13", "D")
            y = y.replace("14", "E")
            y = y.replace("15", "F")
            # print (str(y)+" debugdebug") #debug
            print("Числа больше 9 заменяются на символы от A до F соответсвенно. В данном случае " + str(x) + " заменяется на "+str(y)+". ", end="")
            x = y
        rezultat.append(x)
        # print ("остаток "+str(x)) #debug
        desyat = desyat // 16
        print("Остается " + str(desyat))
    vrem = "".join(str(s) for s in rezultat)
    print("")
    print("В итоге получается " + str(vrem) + ". Нам это число нужно перевернуть.")
    rezultat.reverse()
    print("\n-------------------------------------\n")
    return rezultat