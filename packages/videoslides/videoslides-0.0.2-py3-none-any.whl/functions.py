import os
import cv2
import json
import re
import stanza
import easyocr
import warnings
import numpy as np
import matplotlib.patches as patches
from pytube import YouTube
from pathlib import Path
from matplotlib import pyplot as plt
from math import sqrt 
from math import floor
from skimage import img_as_float
from skimage.metrics import structural_similarity as ssim

def addJ (name):
    return str(name)+".jpg"

def ls(ruta = Path.cwd()):
    """ Funcion que obtiene Lista de nombres de Frames casteado a entero
    -------------------------------------------------------
    Input:
        ruta (str): ruta de carpeta donde se encuentran los frames
    Output:
        (array(int)) Lista de nombres de Frames casteado a entero
    """
    return [int(arch.name.split(".")[0]) for arch in Path(ruta).iterdir() if (arch.is_file() and re.search(r'\.jpg$', arch.name))]

def download_video(url): 
    """ Descarga un video de youtube 
    -------------------------------------------------------
    Input:
        url (str): link del video de youtube
    Output:
        No aplica
    """
    ''' 
    CAMBIOS QUE REQUIERE EN CIPHER.PY (DOCUMENTOS DE LA LIBRERIA)
    lineas 272 y 273
    r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&\s*'
    r'\([a-z]\s*=\s*([a-zA-Z0-9$]{2,3})(\[\d+\])?\([a-z]\)'
    cambiar linea  288
    nfunc=re.escape(function_match.group(1))),
    '''
    try:
        video = YouTube(url)
        title = video.title
        video = video.streams.get_highest_resolution()
        video.download()
        return True, title
    except:
        return False, ""

def getqua(rute1, rute2, me = 1): 
    """ Funcion que compara dos frames con la metrica que indica el parametro "me"
    -------------------------------------------------------
    Input:
        f_ruta (str): ruta frames
        nombre (str): nombre de la extension de la carpeta de bloques
        me (int): metrica a usar para comparar los frames
    Output:
        Valor (float): valor de evaluacion obtenido con metrica elegida
    """
    # COlOR
    # im1 = cv2.imread(rute1)
    # im2 = cv2.imread(rute2)
    #BLANCO Y NEGRO
    if(isinstance(rute1, str)):
        im1 = cv2.imread(rute1, 0)
        im2 = cv2.imread(rute2, 0)
    else:
        im1 = rute1
        im2 = rute2
    im1F = img_as_float(im1)
    im2F = img_as_float(im2)

    # plt.subplot(1, 2, 1)
    # plt.imshow(im1)
    # plt.subplot(1, 2, 2)
    # plt.imshow(im2)
    # plt.show()

    height = im1.shape[0]
    width = im1.shape[1]
    pixT = height *  width

    if(me == 1 ):
        # Aplicando metrica SSIM TODO: elegir un tipo RGB o Blanco y negro, sino habra diferencia entre local y no local
        try:
            ssimV = ssim(im1F, im2F, multichannel=True, data_range=im2F.max() - im2F.min())
        except:
            ssimV = ssim(im1F, im2F, multichannel=False, data_range=im2F.max() - im2F.min())
        return ssimV
    elif(me == 2):
        dif = np.sum(im1 != im2)
        return dif/pixT

def getdata(f_ruta): 
    """ Funcion que usando getqua() en frames ordenados entrega un array con los valores evaluados de frames contiguos
    -------------------------------------------------------
    Input:
        f_ruta (str): ruta frames o (list): array de imagenes cv2
    Output:
        data (list): array ordenado con numeros enteros obtenidos evaluando frames contiguos
    """
    # data = list()
    data = np.array([])

    if(isinstance(f_ruta, list)):
        for index, frame in enumerate(f_ruta):
            if(index != 0):
                rute2 = frame
                qua =  getqua(rute1, rute2, 1) # SSIM
                data = np.append(data, qua) 
                rute1 = rute2
            else:
                rute1 = frame
    else:
        Frames = ls(ruta = f_ruta)
        Frames.sort()
        Frames = list(map(addJ ,Frames))

        # iteracion sobre Frames contiguos, comparando por cantidad de pixeles diferntes y por metric SSIM, para eliminar los con info repetida
        f_ruta = f_ruta+"/"
        for index, frame in enumerate(Frames):
            i = int(frame.split(".")[0]) 
            if(index != 0):
                rute1 = f_ruta+ str(anterior)+'.jpg'
                rute2 = f_ruta+ str(i)+'.jpg'
                qua =  getqua(rute1, rute2, 1) # SSIM
                # TODO anotar esto en documento
                # TEST grafico
                # qua =  getqua(rute1, rute2, 2) 
                # if (qua > 0.9):
                # 	qua = 1
                data = np.append(data, qua) 
            anterior = i
    return data

def localmin(data):
    """ Funcion que obtiene los minimos locales de la data entregada
    -------------------------------------------------------
    Input:
        data (list): array ordenado con numeros enteros 1D
    Output:
        counts[1] (int): numero de minimos locales encontrados
        pos (list): posiciones correspondiente a los minimos locales dentro del array data
    """
    coef = 0.98
    a_min =  np.r_[True, data[1:] < data[:-1]] & np.r_[data[:-1] < data[1:], True] & np.r_[data < coef]
    # a_max =  np.r_[True, data[1:] > data[:-1]] & np.r_[data[:-1] > data[1:], True]
    unique, counts = np.unique(a_min, return_counts=True)
    pos = []
    for index, i in enumerate(a_min):
        if(i):
            pos.append(index)
    return counts[1], pos

def dist_2p(pos1, pos2): 
    """ Obtienen la distancia euclidiana entre dos puntos
    -------------------------------------------------------
    Input:
        pos1 (tuple(int,int)): valores en eje x e y de punto 1
        pos2 (tuple(int,int)): valores en eje x e y de punto 2
    Output:
        distancia (float)
    """
    return sqrt( (pos2[0]-pos1[0])**2 + (pos2[1]-pos1[1])**2 )

def min_dis_sq(pos1, pos2):
    """ Funcion que entrega la distancia entre dos cuadrados, asumiendo diferentes casos reduciendo el calculo a distancia entre dos puntos 
    -------------------------------------------------------
    Input:
        pos1 (arrays(int,int)): valores en eje x e y de punto 1
        pos2 (arrays(int,int)): valores en eje x e y de punto 2
    Output:
        distancia (float)
    """
    a1,a2,a3,a4 = pos1
    b1,b2,b3,b4 = pos2
    dist = 0
    if (a3[0] < b1[0]): # B esta completamente a la derecha de A -> A<<B 
        if (a1[1] > b3[1]):            
            return(dist_2p(a2, b4))
        elif (b1[1] > a3[1]):
            return(dist_2p(a3, b1))
        else:
            return(b1[0] - a3[0])

    elif (b3[0] < a1[0]):
        if (a1[1] > b3[1]):
            return(dist_2p(a1, b3))
        elif (b1[1] > a3[1]):
            return(dist_2p(a4, b2))
        else:
            return(a1[0] - b3[0])

    elif ( b1[0] <= a1[0] <= b3[0] or  b1[0] <= a3[0] <= b3[0] or a1[0] <= b1[0] <= a3[0] or  a1[0] <= b3[0] <= a3[0]):
        if (a1[1] > b3[1]):
            return(a1[1] - b3[1])
        elif (b1[1] > a3[1]):
            return(b1[1] - a3[1])
        else:
            return(dist)
    else:
        # ("FALLO")
        raise Exception("Posicion fuera del rango considerado en min_dis_sq()")

def lemat(text):
    """ Funcion que lematiza el texto recibido
    -------------------------------------------------------
    Input:
        text (str): string con oración o parrafo a ser lematizado
    Output:
        ret (str): string con texto lematizado
    """
    # stanza.download('es')
    nlp = stanza.Pipeline('es', verbose= False,  use_gpu = False) # pos_batch_size=3000
    doc = nlp(text)
    ret = ""
    for sent in doc.sentences:
        for word in sent.words:
            ret = ret + " " + word.lemma    
    return ret

def easy(ruta, detail, debugg = False):
    """ Funcion que :
    - Obtiene una transcripcion de una imagen y las posiciones de cada bloque de texto
    - Dadas las posiciones calcula las distancias entre ellos
    - Con las distancias estructura las transcripciones en orden de lectura occidental (arriba hacia abajo e izquierda a derecha)
    -------------------------------------------------------
    Input:
        ruta (str): ruta frames o imagen (en numpy array)
        detail (str): nombre de la extension de la carpeta de bloques
        debugg (boolean): True -> grafica sobre la imagen los bloques de texto reconocidos
    Output:
        order (array): lista con la transcripcion estructurada 
    """
    
    reader = easyocr.Reader(['en'], gpu=False) # this needs to run only once to load the model into memory
    result = reader.readtext(ruta, detail = detail)
    if (detail == 1):
        trans = ""
        ref_pos = []
        trans_l = []
        c = 0
        if(debugg):
            if(isinstance(ruta, str)):
                im = cv2.imread(ruta, 0)
            else:
                im = ruta
            # Create figure and axes
            fig_dims = (5, 5)
            fig, ax = plt.subplots(figsize=fig_dims)
            # Display the image
            ax.imshow(im)
            ejex = 0
            ejey = 0
        for p, t, a in result :
            aux = []
            count = 0
            trans = trans + t + "\n"
            # -------------------- SE APLICA LA LEMATIZACION EN LAS TRANSCRIPCIONES --------------------
            trans_l.append(lemat(t))
            # ------------------------------------------------------------------------------------------
            # -------------------- SIN APLICARLA  --------------------
            # trans_l.append(t)
            # --------------------------------------------------------
            for  pos, text, accu in result :			
                if (c < count): 
                    dis = round(min_dis_sq(p, pos),2)
                    aux.append(dis)
                # -------------- Se calculan las dimensiones y se crea el poligono que engloba el texto encontrado --------------
                if(debugg):
                    if ( pos[2][0] > ejex): 
                        ejex = pos[2][0] 
                    if ( pos[2][1] > ejey): 
                        ejey = pos[2][1] 
                    x, y =  pos[0]
                    # Create a Rectangle patch
                    rect = patches.Polygon(pos, linewidth=1, edgecolor='r', facecolor='none')
                    plt.text(x, y,str(count))
                    # Add the patch to the Axes
                    ax.add_patch(rect)
                # ---------------------------------------------------------------------------------------------------------------
                count+= 1
            c += 1
            ref_pos.append(aux)

        if(debugg):
            ax.set_xlim(0, ejex+50)
            ax.set_ylim(0, ejey+50)
            ax.invert_yaxis()
        
        flatten = list(num for sublist in ref_pos for num in sublist)
        if(len(flatten) == 0 ):
            warnings.warn("Warning ........... [No hay texto encontrado en frame]")
            return []

        clusters = clustering(ref_pos)
        # -------------- En order_X se dejan los indices de las textos ordenados segun su posicion en el eje x --------------
        orden_l = sorted([item for sublist in clusters for item in sublist])
        pos_l = [p[0][0] for (p, t, a) in result]
        zip_list = list(zip(pos_l, orden_l))
        zip_sort = sorted(zip_list, key=lambda x: x[0])
        order_X = [i[1] for i in zip_sort ]
        # -------------------------------------------------------------------------------------------------------------------

        # -------------- En order_Y se dejan los indices segun eje y --------------
        order_Y = []
        for index, i in enumerate(clusters):
            if (len(i)> 1):
                clus = []
                aux = [k[0] for kinde, k in enumerate(result) if kinde in i]  # lista de pos in cluster i
                lis = [k[0] for k in aux] # lista de pos1 del cluster i
                lis3 =  [k[3] for k in aux] # lista de pos3 del cluster i
                list_H = [k[1] for k in lis] # lista de pos1.y
                list_h = [k[1] for k in lis3] # lista de pos3.y
                while(len(i) > len([item for sublist in clus for item in sublist])):
                    higher = min(list_H) # valor mas alto 
                    pos_H = list_H.index(higher)
                    high = list_h[pos_H] # valor mas alto 
                    list_H[pos_H] = float('inf')
                    # ----------RANGO--------------- ME FALTA TOMAR EL PUNTO 1 Y EL 3 O 4 PARA MEDIR LA ALTURA  (QUIZAS TENGA PROBLEMA CON LOS RECTANGULOS DIAGONALES)
                    rango =  (high- higher)/4
                    levels = []
                    levels.append(i[pos_H])
                    for jndex, j in enumerate(i): # set(range(tot)) - set([i])
                        if(higher+rango > list_H[jndex] ):
                            levels.append(i[jndex])
                            list_H[jndex] = float('inf')

                    clus.append(levels)
            else: # CASO EN QUE len(i) == 1
                clus = i
            order_Y.append(clus)
        # -------------------------------------------------------------------------

        # -------------- En order se dejan los indices segun eje "y" y usando order_X se ordenan los arrays internos --------------
        order = []
        order = order_Y
        for index, i in enumerate(order_Y):
            if(len(i) > 1):
                for jndex, j in enumerate(i):
                    if(len(j) > 1):
                        x_ord = [x for x in order_X if x in j]
                        order[index][jndex] = x_ord
        # -------------------------------------------------------------------------------------------------------------------------

        # -------------- Se crea un archivo json (e idealmente RTF) donde se estructura la transcripcion --------------
        for index, i in enumerate(order):
            if(len(i) > 1):
                for jndex, j in enumerate(i):
                    if(len(j) > 1):
                        for kndex, k in enumerate(j):
                            order[index][jndex][kndex] = trans_l[k]
                    else:
                        order[index][jndex][0] = trans_l[j[0]]
            else:
                order[index][0] = trans_l[i[0]]

        # --------------------- UNIENDO LOS TEXTOS QUE PERTENECEN AL MISMO PARRAFO ---------------------
        # for index, i in enumerate(order):
        #     if(len(i) > 1):
        #         for jndex, j in enumerate(i):
        #             if(len(j) > 1):
        #                 for kndex, k in enumerate(j):
        # ----------------------------------------------------------------------------------------------

        if(debugg):
            plt.show()
        return order        
    else:
        return (" ").join(result)

def deep_index(lst, w):
    """ Funcion que entrega los indices de puntos a los cuales corresponde la distancia indicada en w, dentro de la lista triangular lst (no flatten)
    -------------------------------------------------------
    Input:
        lst array2 (array(arrays(int))): lista de listas con distancias entre bloques de texto, (estructura triangular: [a disntacia con b, c, d, e] [b distancia con c, d, e] ...)
        w (str): palabra/numero a indexar en las lista lst
    Output:
        l[0] (tuple(int, int)): indices de puntos a los cuales corresponde la distancia indicada en w
    """
    l = list((i, sub.index(w)) for (i, sub) in enumerate(lst) if w in sub)
    return l[0]

def clustering(array2):
    """ Funcion forma grupos segun distancias entregadas
    -------------------------------------------------------
    Input:
        array2 (array(arrays(int))): lista de listas con distancias entre bloques de texto, (estructura triangular: [a disntacia con b, c, d, e] [b distancia con c, d, e] ...)
    Output:
        ret_array2 (array(array(int))): array de lista de grupos creados a partir de las distancias (no reundantes)
    """
    tot = len(array2)
    aux = [[None]]*tot
    ret_array2 = [[None]]*tot
    flatten = list(num for sublist in array2 for num in sublist)
    maxim = max(flatten) 
    tot_flat = len(flatten) 
    average = sum(flatten)/tot_flat  
    fla_sort = sorted(flatten)
    media = fla_sort[floor(tot_flat/2)]
    metrica = media# average o media
    while ( len(list(num for sublist in ret_array2 for num in sublist)) < tot*2): 
        minim = min(flatten)
        if (minim > metrica):
            # "existen aislados"
            # TODO(?) :Agregar solos los que no alcanzaron en ret_array2 
            break
        ind = flatten.index(minim) 
        indx, indy = deep_index(array2, minim)        

        flatten[ind] = maxim + 1
        array2[indx][indy] = maxim + 1
        ret_array2[indx] = ret_array2[indx] + [indy+indx+1]

    for j in range(tot):
        if(len(ret_array2[j]) > 1):
            ret_array2[j][0] = j
        elif(len(ret_array2[j]) == 1):
            ret_array2[j] = [j]

    for i in range(tot):
        if(len(ret_array2[i]) == 0):
            continue
        for j in  set(range(tot)) - set([i]):
            if(len([i for i in ret_array2[i] if i in ret_array2[j]]) > 0):
                ret_array2[i] = list(set(ret_array2[i] + ret_array2[j]))
                ret_array2[j] = []

    ret_array2 = [i for i in ret_array2 if len(i)>0]
    return(ret_array2)

def last_ones(array): 
    """ Obtiene los ultimos elementos de las listas dentro de array
    -------------------------------------------------------
    Input:
        array (list): array de arrays
    Output:
        retorno (array) 
    """
    largo = len(array)
    retorno =  []
    for i in range(largo):
        retorno.append(array[i][-1])
    return retorno

def write_json(data, filename= "default"): 
    """ Funcion que escribe data en un archivo formato json
    -------------------------------------------------------
    Input:
        data (array o dict): data estructurada en listas o diccionarios 
        filename (str): nombre del archivo incluyendo la extension
    Output:
        No aplica
    """
    filename = f"{filename}.json"
    with  open(filename, "w") as f:
        json.dump(data, f, indent=4)

def get_transcription(f_ruta, data = [], local = True, ocr = 1): 
    """ Funcion que itera sobre los frames/imagenes transcribiendolas usando algun OCR (easyOCR o teseract) 
    1 = easyOCR
    2 = teseract 
    -------------------------------------------------------
    Input:
        f_ruta (str): ruta frames
        data (list): array con posiciones, usadas como filtro en la seleccion de imagenes
        local (boolean):
    Output:
        transcription (str o list): texto recopilado de cada frame unido en una sola estuctura
    """
    if(isinstance(f_ruta, list)):
        Frames = f_ruta
    else:
        Frames = ls(ruta = f_ruta)
        Frames.sort()
        Frames = list(map(addJ ,Frames))
        f_ruta = f_ruta+"/"
    transcription = ""
    json = []
    # iteracion sobre Frames contiguos, comparando por cantidad de pixeles diferntes y por metric SSIM, para eliminar los con info repetida
    for index, frame in enumerate(Frames):
        if (len(data) != 0 and index in data):
            if(isinstance(frame, str)):
                i = int(frame.split(".")[0]) 
                rute = f_ruta+ str(i)+'.jpg'
            else:
                rute = frame
            if (ocr == 1):
                json.append(easy(rute, 1))
            # elif (ocr == 2):
            #     transcription = transcription + tese(rute, False) + "\n\n"

    if (ocr == 1):
        filename = "order"
        transcription = json
        if(not local):
            write_json(json, filename)
    return transcription

def isame(rute1, rute2, dbugg = False):  
    """ Compara dos frames usando el porcentaje de pixeles que difieren como tambien el valor para SSIM entre ellos
    -------------------------------------------------------
    Input:
        rute1 (str): ruta de primer frame
        rute2 (str): ruta de segundo frame
        dbugg (boolean): True en caso de querer visualizar los frames
    Output:
        state (boolean): indicador que indica si son considerados suficientemente similares 
    """
    # COlOR
    # im1 = cv2.imread(rute1)
    # im2 = cv2.imread(rute2)
    #BLANCO Y NEGRO
    if(isinstance(rute1, str)):
        im1 = cv2.imread(rute1, 0)
        im2 = cv2.imread(rute2, 0)
    else:
        im1 = rute1
        im2 = rute2
    im1F = img_as_float(im1)
    im2F = img_as_float(im2)
    
    # Aplicando metrica SSIM
    try:
        ssimV = ssim(im1F, im2F, multichannel=True, data_range=im2F.max() - im2F.min())
    except:
        ssimV = ssim(im1F, im2F, multichannel=False, data_range=im2F.max() - im2F.min())
    dif = np.sum(im1 != im2)

    # Dimensiones imagen
    height = im1.shape[0]
    width = im1.shape[1]
    # channels = im1.shape[2]
    pix_num = height * width * 3

    state = False
    if ( dif/pix_num < 0.001):
        #  Son escencial- la misma
        if (dbugg):
            print(" ----------------- dif %f ----------------- " % float(dif/pix_num))		
        state  = True
    elif(ssimV>0.999):	
        # Son escencial- la misma
        if (dbugg):
            print(" ----------------- ssimV %f ----------------- " % ssimV)		
        state  = True

    if (dbugg):
        f = plt.figure()
        f.add_subplot(1,2, 1)
        plt.imshow(im1)
        f.add_subplot(1,2, 2)
        plt.imshow(im2)
        plt.title("SAME ? :" + str(state) )
        plt.show(block=True)
    return state

def clean(f_ruta): 
    """ Funcion que usando isame() filtra las imagenes que son consideradas iguales (dejando solo una de ellas)
    para el caso de no estar local : se elimina el frame de la ruta 
    caso local: se crea una nueva lista con los frames correspondientes y se retorna   
    -------------------------------------------------------
    Input:
        f_ruta (str): ruta frames
    Output:
        Frames (lista): local-> lista con los frames (array(numpy.array)) y no-local-> lista con los nombre de los frames en la carpeta
    """
    if(isinstance(f_ruta, list)):
        Frames = f_ruta.copy()
    else:
        Frames = ls(ruta = f_ruta)
        Frames.sort()
        Frames = list(map(addJ ,Frames))
        f_ruta = f_ruta+"/"

    # iteracion sobre Frames contiguos, comparando por cantidad de pixeles diferntes y por metric SSIM, para eliminar los con info repetida
    # j = 0 
    if(isinstance(f_ruta, list)):
        Frames_R = []
        for a, frame in enumerate(Frames):
            if(a != 0):
                rute2 = frame
                if(not isame(rute1, rute2)): # si son iguales no se hace nada, si son distintos se guarda el primero
                    Frames_R.append(rute1)
                rute1 = rute2
            else :
                rute1 = frame
        Frames_R.append(rute2)
        Frames = Frames_R
            
    else: 
        for a, frame in enumerate(Frames):
            i = int(frame.split(".")[0]) 
            if(a != 0):
                rute1 = f_ruta+ str(anterior)+'.jpg'
                rute2 = f_ruta+ str(i)+'.jpg'
                if(isame(rute1, rute2)):  # si son iguales se elimina el primero, si son distintos no se hace nada
                    os.remove(rute1)
            anterior = i
    return Frames

def ploteo(nombre, data): 
    """ Funcion que grafica data 1D, y en caso de no entregarla la obtiene usando getdata(f_ruta)
    -------------------------------------------------------
    Input:
        f_ruta (str): ruta frames
        nombre (str): nombre de la data (video)
    Output:
        "OK" (str)
    """
    print(f" -------- {nombre} -------- ")
    # min, minl = localmin(data)
    classic(data, nombre)
    return "OK"

def classic(data, nombre): 
    """ Grafica data 1D, indicando el nombre, minimo y maximo de la data
    -------------------------------------------------------
    Input:
        data (list):  array ordenado con numeros enteros 1D
        nombre (str): nombre de la data (video)
    Output:
        no aplica
    """
    minim = np.amin(data)
    maxim = np.amax(data)
    plt.plot(data, label='data', color='b')
    plt.legend(bbox_to_anchor=(1.05, 1),loc='upper left', borderaxespad=0.)
    plt.xlabel("Par de frames")
    plt.ylabel("SIMM par de frames")
    number_of_diapos, pos = localmin(data)
    plt.title(f"{nombre} ({number_of_diapos})")
    plt.show()

