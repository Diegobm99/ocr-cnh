import numpy as np
import datetime

import cv2
import re

def validaCNH(cnh):
    if cnh == '' or len(cnh) != 11 or len(set(cnh)) == 1:
        return False

    dsc = 0
    s = 0
    for i in range(9,0,-1):
        s += int(cnh[9-i]) * i

    first_value = s%11
    if first_value >= 10:
        first_value, dsc = 0, 2
    digito1 = first_value

    s = 0
    for i in range(1,10):
        s += int(cnh[i-1]) * i

    rest = s%11

    second_value = rest - dsc
    if rest >= 10:
        second_value = 0
    digito2 = second_value

    if digito1 == int(cnh[9]) and digito2 == int(cnh[10]):
        return True
    else:
        return False

def validaCPF(cpf):
    if cpf == '' or len(cpf) != 11 or len(list(set(cpf))) == 1:
        return False

    add = 0
    for i in range(9):
        add += int(cpf[i])*(10 - i)
    rev = (add*10)%11
    if rev == 10:
        rev = 0
    if rev != int(cpf[9]):
        return False
    add = 0
    for i in range(10):
        add += int(cpf[i])*(11 - i)
    rev = (add*10)%11
    if rev == 10:
        rev = 0
    if rev != int(cpf[10]):
        return False

    return True

def load_image_into_numpy_array(image):
    (im_width, im_height) = image.size
    return np.array(image.getdata()).reshape((im_height, im_width, 3)).astype(np.uint8)
