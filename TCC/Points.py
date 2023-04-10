import numpy as np

#-----------------------------#-----------------------------#------------------------------------#---------------------------------------#----------------------------#
#Variáveis e listas utilizadas
joints = [] #Juntas que serão usadas pela aplicação
global all_clicks
all_clicks = [] #Id de todas as posições identificadas após o click do mouse
global clicks
clicks = np.zeros((3,2), int) #Matriz de 3 linhas e 2 colunas que corresponde as coordenadas das 3 juntas selecionadas
joints_number = 0 #Limita o número de juntas selecionadas
#-----------------------------#-----------------------------#------------------------------------#---------------------------------------#----------------------------#
#Dicionário contendo o número da junta reconhecida pelo mediapipe e suas coordenadas na imagem utilizada
points = [{"id":23, "coordinates":[231, 231]}, {"id":11, "coordinates":[251, 117]}, {"id":13, "coordinates":[300, 160]}, {"id":15, "coordinates":[340, 140]}, {"id":21, "coordinates":[342, 119]}, {"id":19, "coordinates":[364, 110]}, {"id":17, "coordinates":[377, 140]}, {"id":24, "coordinates":[150, 231]}, {"id":12, "coordinates":[128, 117]}, {"id":14, "coordinates":[86, 160]}, {"id":16, "coordinates":[43, 140]}, {"id":22, "coordinates":[43, 119]}, {"id":20, "coordinates":[22, 110]}, {"id":18, "coordinates":[8, 140]}, {"id":25, "coordinates":[257, 312]}, {"id":27, "coordinates":[235, 398]}, {"id":29, "coordinates":[222, 419]}, {"id":31, "coordinates":[266, 423]}, {"id":26, "coordinates":[128, 312]}, {"id":28, "coordinates":[151, 398]}, {"id":30, "coordinates":[163, 419]}, {"id":32, "coordinates":[120, 423]}]
#MAPA COORDENADAS DAS JUNTAS NA IMAGEM
#(231, 231) #23
#(251, 117) #11
#(300, 160) #13
#(340, 140) #15
#(342, 119) #21
#(364, 110) #19
#(377, 140) #17
#(150, 231) #24
#(128, 117) #12
#(86, 160) #14
#(43, 140) #16
#(43, 119) #22
#(22, 110) #20
#(8, 140) #18
#(257, 312) #25
#(235, 398) #27
#(222, 419) #29
#(266, 423) #31
#(128, 312) #26
#(151, 398) #28
#(163, 419) #30
#(120, 423) #32
#-----------------------------#-----------------------------#------------------------------------#---------------------------------------#----------------------------#
#Define cada junta reconhecida pelo Mediapipe em forma de coordenada na imagem para seleção de juntas
def isInside(x, y):
    for point in points:
        if ((x - point["coordinates"][0]) * (x - point["coordinates"][0]) +
            (y - point["coordinates"][1]) * (y - point["coordinates"][1]) <= 10 * 10):
            return point["id"]
