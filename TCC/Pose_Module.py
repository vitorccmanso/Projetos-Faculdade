import cv2
from matplotlib.pyplot import angle_spectrum
import mediapipe as mp
import numpy as np
import time

#Classe para automatizar todo o código de avaliação e detecção das juntas
global angles
angles = []
class poseDetector():
    #Parametros iguais ao da função "Pose" do mediapipe
    def __init__(self, mode=False, upBody=False, smooth=True, detectionConf=0.5, trackConf=0.5):
        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth
        self.detectionConf = detectionConf
        self.trackConf = trackConf

        self.mp_drawing = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode, self.upBody, self.smooth, self.detectionConf, self.trackConf)

    #Detecção
    def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #Coloca a imagem em cores formato rgb pois a opencv utiliza imagens em bga
        self.results = self.pose.process(imgRGB) #Processa a imagem que foi detectada
        #Detecta as partes do corpo e as coordenadas de cada ponto detectado na imagem, caso alguma imagem seja pós-processada
        if self.results.pose_landmarks:
            if draw:
                #Desenha no img as linhas e pontos das juntas do corpo humano
                self.mp_drawing.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
        return img
 
    def findPostion(self, img, draw=True):
        self.lmList = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark): #Indica o número e as coordenadas de cada junta detectada 
                h, w, c = img.shape #Altura, comprimento e canal da imagem
                cx, cy = int(lm.x*w), int(lm.y*h) #Multiplica a altura e comprimento da junta pela resolução da imagem, dando o valor real de localização
                self.lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED) #Coloca no video os pontos com as coordenadas verdadeira, para caso alguma junta não estiver sendo bem rastreada
        return self.lmList

    def findAngle(self, img, p1, p2, p3, draw=True):
        #Pega as coordenadas dos 3 pontos selecionados na lista
        x1, y1 = self.lmList[p1][1:]
        x2, y2 = self.lmList[p2][1:]
        x3, y3 = self.lmList[p3][1:]

        #Calculo do ângulo
        radians = np.arctan2(y3-y2, x3-x2) - np.arctan2(y1-y2, x1-x2)
        angle = np.abs(radians*180.0/np.pi)

        if angle > 180.0:
            angle = 360 - angle
            #angle.append(angle)

        #Desenha círculos em cima dos pontos selecionados para uma melhor visualização
        if draw:
            cv2.line(img, (x1,y1), (x2,y2), (255,255,255), 3)
            cv2.line(img, (x2,y2), (x3,y3), (255,255,255), 3)
            cv2.circle(img, (x1, y1), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x1, y1), 15, (0, 0, 255), 2)
            cv2.circle(img, (x2, y2), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (0, 0, 255), 2)
            cv2.circle(img, (x3, y3), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x3, y3), 15, (0, 0, 255), 2)
            cv2.putText(img, str(int(angle)), (x2,y2), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
        if angle not in angles:
            angles.append(int(angle))

def main():
    #Captura de video
    cap = cv2.VideoCapture(0)
    pTime = 0
    detector = poseDetector()
    while True:
        success, img = cap.read()
        img = detector.findPose(img)
        lmList = detector.findPostion(img, draw=False)
        #if len(lmList) != 0:
            #print(lmList[14])
            #cv2.circle(img, (lmList[14][1], lmList[14][2]), 15, (0, 0, 250), cv2.FILLED)
        #Calcula o fps do video e escreve na tela
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (70, 50),
                   cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
 
        cv2.imshow("Video", img)
 
        if cv2.waitKey(24) == ord("q"):
            break

if __name__ == '__main__':
    main()

cv2.destroyAllWindows()