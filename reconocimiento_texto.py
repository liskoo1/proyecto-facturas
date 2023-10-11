import cv2 
import numpy as np
import matplotlib.pyplot as plt
import pytesseract as ts
import pandas as pd
#path de tesseract
ts.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'
def print_imagenes(img):
    '''muestra las imagenes'''
    try:
        # Realizar el recorte y mostrar la imagen recortada
        cv2.imshow("Imagen", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except:
        print("No se pudo cargar la imagen.")

def read_and_resize(img: str):
    '''Lee y le da un nuevo tamaño a la imagen'''
    try:
        #imagen a mostrar
        imagen = cv2.imread(img)
        imagen_bn = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        #redimension de imagen
        img_resize = cv2.resize(imagen_bn,[714,1024],interpolation = cv2.INTER_CUBIC)
        return img_resize
    except:
        print("Imagen no encontrada o archivo dañado.")
    


#dimensiones donde se encuentran los datos que queremos del documento
def get_descripcion(img_re, x1:int, y1:int, x2:int, y2:int):
    '''
    Esta funcioón extrae los datos de una parte de la imagen.
    (x1, y1) es la esquina superior izquierda y (x2, y2) es la esquina inferior derecha
    '''
    img_redi = cv2.resize(img_re,[1500,2151],interpolation = cv2.INTER_CUBIC)
    #recortamos la imagen el la zona donde queremos
    descripcion_art = img_redi[y1:y2, x1:x2]
    #redimensionamos la imagen para una mejor lerctura de los datos
    print_imagenes(descripcion_art)
    #extraemos los datos de la imagen en string
    texto = ts.image_to_string(descripcion_art)
    #separamos los articulos en la lista por los saltos de linea
    texto = texto.split("\n")
    #como no salen partes del texto en un string vacio pues los quitamos
    list_art = []
    for tex in texto:
        if not tex == "":
            list_art.append(tex)
    print("descripcion ",list_art)
    return list_art

def get_precio_importe(img_re, x1:int, y1:int, x2:int, y2:int):
    '''
    Esta función extrae los datos numericos de la imagen.
    (x1, y1) es la esquina superior izquierda y (x2, y2) es la esquina inferior derecha
    '''
    img_resize = cv2.resize(img_re,[1500,2151],interpolation = cv2.INTER_CUBIC)
    #recortamos la imagen el la zona donde queremos
    descripcion_art = img_resize[y1:y2, x1:x2]
    print_imagenes(descripcion_art)
    #extraemos los datos de la imagen en string
    texto = ts.image_to_string(descripcion_art)
    #separamos los articulos en la lista por los saltos de linea
    texto = texto.split("\n")
    #como no salen partes del texto en un string vacio pues los quitamos
    precio_importe = []
    for tex in texto:
        if not tex == "":
            #cambiamos las comas por puntos para poder hacer los numeros float
            nuevo_tex = float(tex.replace(",","."))
            #los guardamos en una lista
            precio_importe.append(nuevo_tex)
    print("importe ",precio_importe)
    return precio_importe

def get_units(img_re, x1:int, y1:int, x2:int, y2:int, imp_total: list = [],precio: list = []):
    '''Esta función extrae los datos numericos de la imagen.
    (x1, y1) es la esquina superior izquierda y (x2, y2) es la esquina inferior derecha
    '''
    
    img_resize = cv2.resize(img_re,[1500,2151],interpolation = cv2.INTER_CUBIC)
    #recortamos la imagen el la zona donde queremos
    descripcion_art = img_resize[y1:y2, x1:x2]
    print_imagenes(descripcion_art)
    #extraemos los datos de la imagen en string
    texto = ts.image_to_string(descripcion_art)
    print("Texto", texto)

    try:
        
        #separamos los articulos en la lista por los saltos de linea
        texto = texto.split("\n")
        #como no salen partes del texto en un string vacio pues los quitamos
        units = []
        for tex in texto:
            if not tex == "":
                #cambiamos las comas por puntos para poder hacer los numeros float
                nuevo_tex = float(tex.replace(",","."))
                #los guardamos en una lista
                units.append(nuevo_tex)
        print("unidaes",units)
        if len(imp_total) == len(units):
            return  units
        else:
            raise Exception("Error en la data")
    except Exception:
        '''Calcula las unidades que hay de cada productoe en la factura'''
        units = []
        for i in range(len(imp_total)):
            units.append(round(imp_total[i] / precio[i])) 
        return units

def get_iva(img_re,lista_articulos, x1:int, y1:int, x2:int, y2:int):
    '''
    Esta función extrae los datos numericos de la imagen.
    (x1, y1) es la esquina superior izquierda y (x2, y2) es la esquina inferior derecha
    '''
    img_resize = cv2.resize(img_re,[1500,2151],interpolation = cv2.INTER_CUBIC)
    #recortamos la imagen el la zona donde queremos
    descripcion_art = img_resize[y1:y2, x1:x2]
    print_imagenes(descripcion_art)
    #extraemos los datos de la imagen en string
    texto = ts.image_to_string(descripcion_art)
    print("Texto", texto)
    #separamos los articulos en la lista por los saltos de linea
    texto = texto.split("\n")
    #como no salen partes del texto en un string vacio pues los quitamos
    iva = []
    for tex in texto:
        if not tex == "":
            #cambiamos las comas por puntos para poder hacer los numeros float
            nuevo_tex = float(tex.replace(",","."))
            #los guardamos en una lista
            iva.append(nuevo_tex)
    print("IVA",iva)
    if iva == []:
        for i in range(len(lista_articulos)):
            iva.append(0)
        print("iva",iva)
    return  iva
    
def mostrar_tablas(articulos: list, iva: list, unidades: list, precio: list,precio_total: list):
    data = {
        "Descripcion":articulos,
        "iva": iva,
        "unidades": unidades,
        "lista_precio": precio,
        "lista_imp_total": precio_total 
    }
    df = pd.DataFrame(data)
    print(df)
    return df



'''img = read_and_resize("img/albaran1.jpg")
units = get_descripcion(img,434,738,1107,1575)
lista_precio = get_precio_importe(img,1164,739,1250,1629)
lista_imp_total = get_precio_importe(img,1377,742,1462,1626)
unidades = get_units(lista_imp_total,lista_precio)
mostrar_tablas(units,unidades,lista_precio,lista_imp_total)
print_imagenes(img)
print_imagenes(img2)
print_imagenes(img3)
print_imagenes(img4)
'''

