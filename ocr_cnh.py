import pytesseract as ocr

import numpy as np
import datetime
import cv2
import re
from utils_cnh import validaCPF, validaCNH

ocr.pytesseract.tesseract_cmd = "./Tesseract-OCR/tesseract.exe"

def cpf_(cpf_img):
    h = cpf_img.shape[0]

    cpf_img = cpf_img[int(0.1*h):int(0.9*h),:]

    cpf_img_gray = cv2.cvtColor(cpf_img, cv2.COLOR_RGB2GRAY)

    cpf_img_gray = np.concatenate((cpf_img_gray, cpf_img_gray), axis=0)
    cpf_img_gray = np.concatenate((cpf_img_gray, cpf_img_gray), axis=1)

    cpf_img_gray_th1 = cv2.adaptiveThreshold(cpf_img_gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,8)
    cpf_img_gray_th2 = cv2.adaptiveThreshold(cpf_img_gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,6)


    cpf_img_rgb = np.concatenate((cpf_img, cpf_img), axis=0)
    cpf_img_rgb = np.concatenate((cpf_img_rgb, cpf_img_rgb), axis=1)

    cpf_ocr_gray = ocr.image_to_string(cpf_img_gray, lang='por')
    cpf_ocr_rgb = ocr.image_to_string(cpf_img, lang='por')
    cpf_ocr_gray_th1 = ocr.image_to_string(cpf_img_gray_th1, lang='por')
    cpf_ocr_gray_th2 = ocr.image_to_string(cpf_img_gray_th2, lang='por')

    cpf_ocr = cpf_ocr_gray + ' ' + cpf_ocr_rgb + ' ' + cpf_ocr_gray_th1 + ' ' + cpf_ocr_gray_th2

    cpf_ocr = cpf_ocr.replace('.', '')
    cpf_ocr = cpf_ocr.replace('-', '')
    cpf_ocr = cpf_ocr.replace(',', '')
    cpf_ocr = cpf_ocr.replace(' ', '')

    cpf_ocr = re.findall(r'\d{11}\b', cpf_ocr)


    cpf_ocr_u = list(set(cpf_ocr))

    cpf = ''
    if len(cpf_ocr_u) > 0:
        for c in cpf_ocr_u:
            if validaCPF(c):
                cpf = c

    return(cpf)

def nasc_(nasc_img):
    nasc_img_gray = cv2.cvtColor(nasc_img, cv2.COLOR_RGB2GRAY)

    nasc_img_gray = np.concatenate((nasc_img_gray, nasc_img_gray), axis=0)
    nasc_img_gray = np.concatenate((nasc_img_gray, nasc_img_gray), axis=1)

    nasc_ocr = ocr.image_to_string(nasc_img_gray, lang='por')

    nasc_img_gray2 = cv2.adaptiveThreshold(nasc_img_gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,8)
    nasc_img_gray3 = cv2.adaptiveThreshold(nasc_img_gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,6)

    nasc_ocr2 = ocr.image_to_string(nasc_img_gray2, lang='por')
    nasc_ocr3 = ocr.image_to_string(nasc_img_gray3, lang='por')

    nasc_ocr = nasc_ocr + ' ' + nasc_ocr2 + ' ' + nasc_ocr3

    nasc_ocr = re.findall(r'\d{2}\b/\d{2}\b/\d{4}\b', nasc_ocr)

    count_nasc = nasc_ocr
    nasc_ocr = list(set(nasc_ocr))

    nasc = ''
    if len(nasc_ocr) > 0:
        ns = nasc_ocr.copy()
        for n in ns:
            try:
                n_date = datetime.datetime.strptime(n, '%d/%m/%Y').date()
            except:
                nasc_ocr.remove(n)
                count_nasc.remove(n)
                continue
            y = (datetime.datetime.now().date() - n_date).days
            if y/365 < 16 or y/365 > 110:
                nasc_ocr.remove(n)
                count_nasc.remove(n)
            if n_date.day < 1 or n_date.day > 31:
                nasc_ocr.remove(n)
                count_nasc.remove(n)
            if n_date.month < 1 or n_date.month > 12:
                nasc_ocr.remove(n)
                count_nasc.remove(n)

        if len(nasc_ocr) > 0:
            values, counts = np.unique(count_nasc, return_counts=True)
            nasc = values[np.argmax(counts)]

    return(nasc)

def cnh_(cnh_img):
    h = cnh_img.shape[0]

    cnh_img = cnh_img[int(0.1*h):int(0.9*h),:]

    cnh_img_gray = cv2.cvtColor(cnh_img, cv2.COLOR_RGB2GRAY)

    cnh_img_gray = np.concatenate((cnh_img_gray, cnh_img_gray), axis=0)
    cnh_img_gray = np.concatenate((cnh_img_gray, cnh_img_gray), axis=1)

    cnh_img_gray_th1 = cv2.adaptiveThreshold(cnh_img_gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,8)
    cnh_img_gray_th2 = cv2.adaptiveThreshold(cnh_img_gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,6)

    cnh_img_rgb = np.concatenate((cnh_img, cnh_img), axis=0)
    cnh_img_rgb = np.concatenate((cnh_img_rgb, cnh_img_rgb), axis=1)

    cnh_ocr_gray = ocr.image_to_string(cnh_img_gray, lang='por')
    cnh_ocr_rgb = ocr.image_to_string(cnh_img, lang='por')
    cnh_ocr_gray_th1 = ocr.image_to_string(cnh_img_gray_th1, lang='por')
    cnh_ocr_gray_th2 = ocr.image_to_string(cnh_img_gray_th2, lang='por')

    cnh_ocr = cnh_ocr_gray + ' ' + cnh_ocr_rgb + ' ' + cnh_ocr_gray_th1 + ' ' + cnh_ocr_gray_th2

    cnh_ocr = cnh_ocr.replace('.', '')
    cnh_ocr = cnh_ocr.replace('-', '')
    cnh_ocr = cnh_ocr.replace(',', '')
    cnh_ocr = cnh_ocr.replace(' ', '')

    cnh_ocr = re.findall(r'\d{11}\b', cnh_ocr)

    cnh_ocr_u = list(set(cnh_ocr))

    cnh = ''
    if len(cnh_ocr_u) > 0:
        for c in cnh_ocr_u:
            if validaCNH(c):
                cnh = c

    return(cnh)
