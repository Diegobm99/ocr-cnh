import utils_cnh
import read_model
from PIL import Image, ExifTags
import numpy as np
import cv2

# Função para fazer o Crop dos campos detectados pelo Modelo
def crop(path, detection_graph):
    lbs = ['nome', 'rg', 'cpf', 'nasc', 'pais', 'cnh', 'validade', 'cat']

    # Leitura da imagem e ajustamento da posição
    image = Image.open(path)
    try:
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation]=='Orientation':
                break
        exif = dict(image._getexif().items())

        if exif[orientation] == 3:
            image=image.rotate(180, expand=True)
        elif exif[orientation] == 6:
            image=image.rotate(270, expand=True)
        elif exif[orientation] == 8:
            image=image.rotate(90, expand=True)
    except (AttributeError, KeyError, IndexError):
        pass

    image_np = utils_cnh.load_image_into_numpy_array(image)

    h, w = image_np.shape[0:2]
    if h > 1800:
        r = 1800/h
        image_np = cv2.resize(image_np, (int(r*w),int(r*h)))

    # Inferência e deteção dos campos
    image_np_expanded = np.expand_dims(image_np, axis=0)
    output_dict = read_model.run_inference_for_single_image(image_np, detection_graph)

    caixa = output_dict['detection_boxes'][output_dict['detection_scores'] > 0.6]
    classe = output_dict['detection_classes'][output_dict['detection_scores'] > 0.6]

    # Crop dos campos detectados
    lista_img = []
    h, w = image_np.shape[:2]
    for i in range(len(classe)):
        h1 = int(round(h*caixa[i][0]))
        h2 = int(round(h*caixa[i][2]))
        w1 = int(round(w*caixa[i][1]))
        w2 = int(round(w*caixa[i][3]))
        if classe[i] == 'nome':
            p = int(round((w2 - w1)*0.03))
        else:
            p = int(round((w2 - w1)*0.02))
        crop = image_np[h1:h2,(w1-p):(w2+p)]
        lista_img.append(crop)

    cpf_img = lista_img[np.where(classe == lbs.index('cpf') + 1)[0][0]].copy()
    nasc_img = lista_img[np.where(classe == lbs.index('nasc') + 1)[0][0]].copy()
    cnh_img = lista_img[np.where(classe == lbs.index('cnh') + 1)[0][0]].copy()

    return(cpf_img, nasc_img, cnh_img)
