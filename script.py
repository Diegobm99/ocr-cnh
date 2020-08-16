
import os
import argparse

import utils_cnh
import read_model
import inference
import ocr_cnh

# Argumentos passados com path da pasta ou imagem
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str,
    help="path to input image")
ap.add_argument("-f", "--folder", type=str,
    help="path to input folder")

args = vars(ap.parse_args())

# Função para extrair e organizar os dados extraídos num dicionário
def dict_cnh(imgs):
    # Exrtação do CPF do documento
    cpf = ocr_cnh.cpf_(imgs[0])
    # Extração da Data Nascimento do documento
    nasc = ocr_cnh.nasc_(imgs[1])
    # Extração da CNH do documento
    cnh = ocr_cnh.cnh_(imgs[2])

    # Organização dos dados extraídos
    names = ["CPF", "Nascimento", "CNH"]
    data = [cpf.strip(), nasc.strip(), cnh.strip()]

    CNH = {}
    for i in range(len(names)):
        CNH[names[i]] = data[i]

    return(CNH)

# Leitura do modelo '.pb' para deteção dos campos do documento
detection_graph = read_model.model()

# Caso o argumento passado seja uma pasta, faz o processo de extração para todas as imagens contidas nela
if args['folder'] != None:
    path_img = os.listdir(args['folder'])
    for path in path_img:
        try:
            imgs = inference.crop(args['folder'] + '/' + path, detection_graph)
            print('\n', path, dict_cnh(imgs))

        except:
            print('\n', path, '-- Campos não encontrados.')

# Caso o argumento passado seja uma imagem, faz o processo de exrtação na imagem
elif args['image'] != None:
    try:
        imgs = inference.crop(args['image'], detection_graph)
        print('\n', args['image'].split('/')[-1], dict_cnh(imgs))
    except:
        print('\n', args['image'].split('/')[-1], '-- Campos não encontrados.')
