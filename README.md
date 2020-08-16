# ocr-cnh

## Requisitos
- Objetivo: Extrair informações de uma CNH;

- Solução: Devido ao grande número de ruídos em um documento CNH, decidi criar um modelo de detecção de objetos com TensorFlow 1, capaz de extrair de forma eficiente as caixas de diferentes campos da CNH.

## Treinamento do modelo
Para treinar o modelo, usei a API de Detecção de Objetos do Tensorflow. Como modelo base foi utilizado o <b>Faster-RCNN-Inception-V2-COCO</b>.

- Pros: O modelo consegue detectar com facilidade os campos de uma CNH.
- Cons: Tempo de processamento.

## Dataset para Treinamento
A base de treinamento foi construída utilizando diversas fotos de apenas uma CNH em ambientes e com qualidades diferentes. Para criar os labels em cada imagem foi utilizado o software <a href="https://github.com/tzutalin/labelImg">labelImg</a>. Os labels anotados para treinamento foram: Nome, RG, CPF, Data Nascimento, Filiação(pais), CNH, Validade e Categoria.

## Leitura dos campos com OCR
Nesta etapa foram utilizados apenas os labels CPF, Data Nascimento e CNH.

Para extração de texto dos campos foi utilizado o <a href="https://github.com/tesseract-ocr/tesseract">tesseract</a>. Cada campo recebeu tratamentos específicos de imagem com o uso do OpenCV e logo em seguida foi utilizado o pytesseract para extração dos textos.

Desafios: Devido ao grande número de ruídos, foi preciso utilizar em cada imagem diversos tipos de tratamentos, para logo em seguida tratar cada texto com regex para construir o output final. Um problema não resolvido foi a dificuldade na extração de documentos em baixa qualidade ou com reflexos/blur em excesso.

## Como testar o código
Clonar o git e instalar os requirements. Para testar o código, foi utilizado CNHs de tamanhos e qualidades diferentes, contidos na pasta './cnhs/'.

 - É possível rodar o código pelo Jupyter Notebook. Um exemplo foi feito em <a href="https://github.com/Diegobm99/ocr-cnh/blob/master/ocr-cnh.ipynb">ocr-cnh.ipynb</a>.


 - Ou pelo próprio prompt do python:

Na pasta do projeto, rodar os seguintes comandos:

Para uma imagem específica:
```
python script.py -i [PATH para a imagem]
```
Exemplo:
```
python script.py -i ./cnhs/cnhfake.jpg
```

Para várias imagens contidas em uma pasta:
```
python script.py -f [PATH para a pasta]
```
Exemplo:
```
python script.py -f ./cnhs/
```
