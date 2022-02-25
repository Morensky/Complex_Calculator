import math, colorama
from colorama import Fore, Back, Style
##======================================================================
## z = (a1+...+an)+i(b1+...+bn)
def COMPLEX_PLUS(n):
    real, immag = 0, 0
    print('plus complex numbers in z')
    for i in range(n):
        real1 = int(input('print real for z' + str(i)))
        immag1 = int(input('print immag for z' + str(i)))
        real += real1
        immag += immag1
    z = (real, immag)
    return('z = ' + str(z[0]) + '+i' + str(z[1]))

## z = |z1*...*zn|*cos(a1+...+an)+isin(a1+...an) = |z1*...*zn|*e^(i(a1+...+an))
def COMPLEX_MNOJ(n):
    z, all_angle, all_leng = [], 0, 1
    for i in range(n):
        print('print nums for z' + str(i) + ' >>> ')
        piece = (int(input()), int(input()))
        alpha, leng = math.degrees(math.atan2(piece[1],piece[0])), math.sqrt(piece[0]**2 + piece[1]**2)
        all_angle += alpha
        all_leng *= leng
    z.append(all_leng)
    z.append(all_angle)
    return('z = ' + str(z[0]) + 'e^(i' + str(z[1]) + ')')

## (z1 * !z2*...!zn) / ((x2^2 + y2^2)*...*(xn^2 + yn^2))
def COMPLEX_DEL(n):
    z, z_angle, z_reald, podz_ = [], 0, 1, 1
    real = int(input('real z1 >>> '))
    image = int(input('image z1 >>> '))
    piece = (math.degrees(math.atan2(image, real)), math.sqrt(real**2 + image**2))
    for i in range(n):
        delyashi = (int(input('print real !z' + str(i))), int(input('print image !z' + str(i))))
        delyashi1 = (math.sqrt(delyashi[0]**2 + delyashi[1]**2), math.degrees(math.atan2((-1)*delyashi[1], delyashi[0])))
        pod_real = delyashi[0]**2 + delyashi[1]**2
        z_angle += delyashi1[1]
        z_reald *= delyashi1[0]
        podz_ *= pod_real
    z_reald *= piece[1]
    z.append(piece[0] + z_angle)
    z.append(z_reald / podz_)
    return('z = ' + str(z[1]) + 'e^(i' + str(z[0]) + ')')

##re^ia -> x+iy
def POCAS_to_ALG(r, phi):
    x = r / (math.sqrt(1 + math.tan(phi)**2))
    y = x * math.tan(phi)
    return ('X = ' + str(x) + ' +i' + str(y))

##x+iy -> re^ia
def ALG_to_POCAS(x, y):
    r = math.sqrt(x**2 + y**2)
    phi = math.degrees(math.atan2(y, x))
    return('X = ' + str(r) + ' +e^i' + str(phi))

#x^(1/n) -> x1, x2, x3
def COMPLEX_KOR(n, x, y):
    phi, leng = math.degrees(math.atan2(y, x)), math.sqrt(x**2 + y**2) ** (1 / n)
    for i in range(n):
        print('z' + str(i) + '=' + str(leng) + 'e^i(' + str((phi + (2 * math.pi * i)) / n) + ')')

#x^n = |x|^n * e^i(n*phi) Muavra
def Muavra(n, x, y):
    return ('z' + '=' + str(math.sqrt(x**2 + y**2) ** n) + 'e^i(' + str(math.degrees(math.atan2(y, x)) * n) + ')')


##======================================================================
colorama.init()
print("\033[3;32;40m                      _        _                                             \033[0;32;40m")
print("\033[3;32;40m                     | |      | |                                            \033[0;32;40m")
print("\033[3;32;40m  _ __ ___   __ _  __| | ___  | |__  _   _   _ __ ___   ___  _ __ ___ _ __   \033[0;32;40m")
print("\033[3;32;40m | '_ ` _ \ / _` |/ _` |/ _ \ | '_ \| | | | | '_ ` _ \ / _ \| '__/ _ \ '_ \  \033[0;32;40m")
print("\033[3;32;40m | | | | | | (_| | (_| |  __/ | |_) | |_| | | | | | | | (_) | | |  __/ | | | \033[0;32;40m")
print("\033[3;32;40m |_| |_| |_|\__,_|\__,_|\___| |_.__/ \__, | |_| |_| |_|\___/|_|  \___|_| |_| \033[0;32;40m")
print("\033[3;32;40m                                      __/ |                                  \033[0;32;40m")
print("\033[3;32;40m                                     |___/                                   \033[0;32;40m")
print('-=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=-')
print("| 1 - sum of complex nums                                  |")
print("| 2 - multiplication of complex nums                       |")
print("| 3 - division of complex nums                             |")
print("| 4 - indicative form -> algebraic form                    |")
print("| 5 - algebraic form -> indicative form                    |")
print("| 6 - extracting the roots of a complex number in a power n|")
print("| 7 - De Moivre's formula                                  |")
print("| contacts: Herman Garsky#2574                             |")

while True:
    key = int(input('choose your type complex operation >>> '))
    if key == 1:
        n = int(input('print amount >>> '))
        if n == 0:
            print('ERROR! PLS, TRY AGAIN!')
        else:
            print(COMPLEX_PLUS(n))
    elif key == 2:
        n = int(input('print amount >>> '))
        if n == 0:
            print('ERROR! PLS, TRY AGAIN!')
        else:
            print(COMPLEX_MNOJ(n))
    elif key == 3:
        n = int(input('print amount >>> '))
        if n == 0:
            print('ERROR! PLS, TRY AGAIN!')
        else:
            print(COMPLEX_DEL(n))
    elif key == 4:
        print(ALG_to_POCAS(int(input('print x >>> ')), int(input('print y >>> '))))
    elif key == 5:
        print(POCAS_to_ALG(int(input('print |x| >>> ')), int(input('print angle in degrees >>> '))))
    elif key == 6:
        n = int(input('print amount >>> '))
        if n == 0:
            print('ERROR! PLS, TRY AGAIN!')
        else:
            num1, num2 = int(input('print x >>> ')), int(input('print y >>> '))
            print(COMPLEX_KOR(n, num1, num2))
    elif key == 7:
        n = int(input('print amount >>> '))
        if n == 0:
            print('ERROR! PLS, TRY AGAIN!')
        else:
            num1, num2 = int(input('print x >>> ')), int(input('print y >>> '))
            print(Muavra(n, num1, num2))
    else:
        break
