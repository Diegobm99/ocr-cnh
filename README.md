# ocr-cnh

## Como testar o código
O código foi feito no <b>Windows</b> com <b>Python 3.7</b>.

Clonar o git e instalar os requirements. Para testar o código, foram utilizadas CNHs de tamanhos e qualidades diferentes, contidas na pasta './cnhs/'.

 - É possível rodar o código pelo Jupyter Notebook. Um exemplo foi feito em <a href="https://github.com/Diegobm99/ocr-cnh/blob/master/ocr-cnh.ipynb">ocr-cnh.ipynb</a>;


 - Ou pelo próprio prompt:

Na pasta do projeto, rodar os seguintes comandos:

#### Para uma imagem específica:
```
python script.py -i [PATH para a imagem]
```
#### Exemplo:
```
python script.py -i ./cnhs/cnhfake.jpg
```

#### Para várias imagens contidas em uma pasta:
```
python script.py -f [PATH para a pasta]
```
#### Exemplo:
```
python script.py -f ./cnhs/
```
