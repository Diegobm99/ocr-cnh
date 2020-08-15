
import os
import argparse

import utils_cnh
import read_model
import inference
import ocr_cnh

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str,
	help="path to input image")
ap.add_argument("-f", "--folder", type=str,
	help="path to input folder")

args = vars(ap.parse_args())

def dict_cnh(imgs):
    cpf = ocr_cnh.cpf_(imgs[0])
    nasc = ocr_cnh.nasc_(imgs[1])
    cnh = ocr_cnh.cnh_(imgs[2])
    names = ["CPF", "Nascimento", "CNH"]

    data = [cpf.strip(), nasc.strip(), cnh.strip()]

    CNH = {}
    for i in range(len(names)):
        CNH[names[i]] = data[i]

    return(CNH)


detection_graph = read_model.model()

if args['folder'] != None:
    path_img = os.listdir(args['folder'])
    for path in path_img:
        imgs = inference.crop(args['folder'] + path, detection_graph)
        print('\n', path, dict_cnh(imgs))

elif args['image'] != None:
    imgs = inference.crop(args['image'], detection_graph)
    print('\n', args['image'].split('/')[-1], dict_cnh(imgs))
