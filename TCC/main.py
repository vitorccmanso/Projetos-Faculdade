from tkinter import *
from PIL import Image
from PIL import ImageTk
import cv2
import imutils
from numpy import angle
from Pose_Module import *
from Points import *
import time
#-----------------------------#-----------------------------#------------------------------------#---------------------------------------#----------------------------#
#Identifica os clicks do mouse na imagem para a seleção manual das juntas
def mouseClicks(event, x, y, flags, params):
    global joints_number
    global clicks
    if event == cv2.EVENT_LBUTTONDOWN:
        clicks[joints_number] = x, y #Adiciona os pontos x e y na matriz clicks
        if len(joints) < 3:      
            all_clicks.append(isInside(x, y)) #Checa se as coordenadas x e y correspondem a alguma junta ou não
            for i in all_clicks:
                if i != None:
                    if i not in joints:
                        joints.append(i)
                        joints_number += 1 #Confirma que os pontos x e y representam um ponto de junta e avança para a próxima linha da matriz
#-----------------------------#-----------------------------#------------------------------------#---------------------------------------#----------------------------#
#Funções dos botões iniciar, parar e selecionar
#Inicio da gravação
def start():
    angles.clear()
    global cap
    global detector
    cap = cv2.VideoCapture(camera.get())
    #detector = module.poseDetector()
    detector = poseDetector()
    visualize()

#Finaliza a gravação
def stop():
    global cap
    global joints
    global joints_number
    global clicks
    joints.clear()
    clicks = np.zeros((3,2), int)
    joints_number = 0
    all_clicks.clear()
    cap.release()

#Seleciona as juntas na imagem
def select():
    joints_img = cv2.imread("Imagem_juntas/Juntas_Detectaveis.png")
    joints.clear()
    while True:
        for point in points:
                cv2.circle(joints_img, (point["coordinates"][0], point["coordinates"][1]), 10, (0, 0, 255), cv2.FILLED)
                for joint in joints:
                    if joint == point["id"]:
                        cv2.circle(joints_img, (point["coordinates"][0], point["coordinates"][1]), 10, (0, 255, 0), cv2.FILLED)
        cv2.imshow("Selecione as juntas", joints_img)
        cv2.setMouseCallback("Selecione as juntas", mouseClicks)
        print(joints)
        if len(joints) == 3:
            cv2.destroyAllWindows()
            break
        elif cv2.waitKey(1) == ord("q"):
            cv2.destroyAllWindows()
            break
#-----------------------------#-----------------------------#------------------------------------#---------------------------------------#----------------------------#
#Funções dos botões para selecionar conjuntos de juntas frequentemente examinadas
#Define os pontos para ângulo do cotovelo esquerdo
def LeftElb():
    global joints
    joints.clear()
    joints = [11, 13, 15]
#Define os pontos para ângulo do cotovelo direito
def RightElb():
    global joints
    joints.clear()
    joints = [12, 14, 16]
#Define os pontos para ângulo do ombro esquerdo
def LeftShldr():
    global joints
    joints.clear()
    joints = [23, 11, 13]
#Define os pontos para ângulo do ombro direito
def RightShldr():
    global joints
    joints.clear()
    joints = [24, 12, 14]
#-----------------------------#-----------------------------#------------------------------------#---------------------------------------#----------------------------#
#Função de visualização da camera
def visualize():
    success, img = cap.read()
    if success:
        img = detector.findPose(img, False) #Analisa a pose mas não desenha as conexões entre as juntas
        lmList = detector.findPostion(img, False) #Acha a posição de cada junta mas não desenha nada
        if len(lmList) != 0: #Faz com que o desenho só apareça quando os pontos forem identificados
            #Pontos para o cotovelo esquerdo
            detector.findAngle(img, joints[0], joints[1], joints[2]) #Desenha as juntas e suas ligações escolhidas, junto com o ângulo
            if len(angles) > 0:
                MaxAngle.set(max(angles))
                MinAngle.set(min(angles))
        img = imutils.resize(img, width=800)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(image=img)
        lblVideo.configure(image=img)
        lblVideo.image = img
        lblVideo.after(10, visualize)
    else:
        lblVideo.image = ""
        cap.release()
#-----------------------------#-----------------------------#------------------------------------#---------------------------------------#----------------------------#
window = Tk() #Cria a janela
#Configurações da janela
window.title("Teste")
width_window = 1280
height_window = 720
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_window/2)
y_coordinate = (screen_height/2)-(height_window/2)
window.geometry("%dx%d+%d+%d" % (width_window, height_window, x_coordinate, y_coordinate)) #Centraliza a janela
window.resizable(width=False, height=False) #Não deixa mudar a resolução da janela
#-----------------------------#-----------------------------#------------------------------------#---------------------------------------#----------------------------#
#Botões
#Inicia a gravação
btnStart = Button(window, text="Iniciar", width=25, height=5, command=start)
btnStart.place(x=(width_window-1260), y=(height_window-710))
#Parar a gravação
btnStop = Button(window, text="Parar / Limpar juntas sel.", width=25, height=5, command=stop)
btnStop.place(x=(width_window-1050), y=(height_window-711))
#Seleciona manualmente as juntas
btnSelect = Button(window, text="Sel. Juntas", width=25, height=5, command=select)
btnSelect.place(x=(width_window-1050), y=(height_window-600))
#Cotovelo esquerdo
btnLeftElb = Button(window, text="Cotovelo Esquerdo", width=25, height=10, command=LeftElb)
btnLeftElb.place(x=(width_window-1260), y=(height_window-440))
#Cotovelo direito
btnRightElb = Button(window, text="Cotovelo Direito", width=25, height=10, command=RightElb)
btnRightElb.place(x=(width_window-1050), y=(height_window-441))
#Ombro esquerdo
btnLeftShldr = Button(window, text="Ombro Esquerdo", width=25, height=10, command=LeftShldr)
btnLeftShldr.place(x=(width_window-1260), y=(height_window-270))
#Ombro direito
btnRightShldr = Button(window, text="Ombro Direito", width=25, height=10, command=RightShldr)
btnRightShldr.place(x=(width_window-1050), y=(height_window-271))
#-----------------------------#-----------------------------#------------------------------------#---------------------------------------#----------------------------#
#Video em forma de legenda para aparecer na mesma janela
lblVideo = Label(window)
lblVideo.pack(side = RIGHT, padx=30)
#-----------------------------#-----------------------------#------------------------------------#---------------------------------------#----------------------------#
#Legendas com números
#Selecionar a camera que será utilizada
camera = IntVar()
lblCamera = Label(window, text="Camera:", width=25)
lblCamera.place(x=(width_window-1327), y=(height_window-600))

txtCamera = Entry(window, width=5, textvariable=camera)
txtCamera.place(x=(width_window-1200), y=(height_window-600))

#Exibir maior ângulo medido
MaxAngle = StringVar()
lblMaxAngle = Label(window, text="Ângulo Máximo:", width=25)
lblMaxAngle.place(x=(width_window-1320), y=(height_window-550))

txtMaxAngle = Entry(window, width=5, textvariable=MaxAngle, state=DISABLED)
txtMaxAngle.place(x=(width_window-1180), y=(height_window-550))

#Exibir menor ângulo medido
MinAngle = StringVar()
lblMinAngle = Label(window, text="Ângulo Mínimo:", width=25)
lblMinAngle.place(x=(width_window-1320), y=(height_window-500))

txtMinAngle = Entry(window, width=5, textvariable=MinAngle, state=DISABLED)
txtMinAngle.place(x=(width_window-1180), y=(height_window-500))
#-----------------------------#-----------------------------#------------------------------------#---------------------------------------#----------------------------#

window.mainloop()