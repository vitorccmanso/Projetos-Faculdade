import speech_recognition as sr
import pyttsx3

#Define a função reconhecimento para o reconhecimento de voz
def reconhecimento():
    speak = pyttsx3.init('sapi5')

    r = sr.Recognizer()

    with sr.Microphone() as fonte:
        r.adjust_for_ambient_noise(fonte)

        #Enquanto o codigo estiver rodando, o programa sempre irá responder o usuário e tentará fazer o reconhecimento de voz
        while True:
            try:
                audio = r.listen(fonte)

                speech = r.recognize_google(audio, language='pt')
                print('Você disse: ', speech)

                frase = "Você disse " + speech + "?"
                print("Resposta: ", frase)
            
                speak.say(frase)
                speak.runAndWait()

                audio = r.listen(fonte)

                speech2 = r.recognize_google(audio, language='pt')
                print('Você disse: ', speech2)

                #IF / ELSE criado para o programa saber o que responder dependendo da resposta do usuário
                if speech2 == "sim":
                    frase = "Ok, calculando róta até esses produtos."
                    print("Resposta: ", frase)
            
                    speak.say(frase)
                    speak.runAndWait()

                    return speech
                    #break
            
                elif speech2 == "não":
                    frase = "Por favor, repita os produtos que deseja comprar."
                    print("Resposta: ", frase)

                    speak.say(frase)
                    speak.runAndWait()
                else:
                    frase = "Não tive uma confirmação do seu pedido, por favor, repita-o."
                    print("Resposta: ", frase)
            
                    speak.say(frase)
                    speak.runAndWait()
            except:
                print("Algum erro ocorreu.")

#Define a função sem_produtos, para ser usada caso o usuário fale apenas produtos que estão em falta
def sem_produtos():
    speak = pyttsx3.init('sapi5')

    r = sr.Recognizer()

    with sr.Microphone() as fonte:
        r.adjust_for_ambient_noise(fonte)
        
        SemProdutos = "Esses produtos não estão disponiveis no momento. Deseja tentar outros produtos?"
        print("Resposta: ", SemProdutos)
            
        speak.say(SemProdutos)
        speak.runAndWait()

        while True:
            try:
                audio = r.listen(fonte)

                resposta = r.recognize_google(audio, language='pt')
                print('Você disse: ', resposta)

                if resposta == "sim":
                    frase = "Ok. Por favor, diga os novos produtos."
                    print("Resposta: ", frase)
            
                    speak.say(frase)
                    speak.runAndWait()

                    break
                elif resposta == "não":
                    frase = "Ok. Obrigado por nos visitar."
                    print("Resposta: ", frase)

                    speak.say(frase)
                    speak.runAndWait()
                    return False
                    
                else:
                    frase = "Não tive uma confirmação da sua escolha, por favor, repita-a."
                    print("Resposta: ", frase)
            
                    speak.say(frase)
                    speak.runAndWait()
            except:
                print("Algum erro ocorreu.")

def intro():
    speak = pyttsx3.init('sapi5')

    r = sr.Recognizer()

    with sr.Microphone() as fonte:
        r.adjust_for_ambient_noise(fonte)

        Intro = "Bem vindo, por favor, diga os produtos que deseja comprar."
        print("Resposta: ", Intro)
            
        speak.say(Intro)
        speak.runAndWait()

        return Intro


