# Projetos realizados durante a faculdade

## Carrinho acessível:
Projeto voltado para ajudar pessoas com algum grau de deficiência visual a realizar comprar no mercado. Essas pessoas teriam acesso a um carrinho especial que seria controlado por voz e calcularia a rota mais rápida pelo supermercado com base nos produtos citados.
 - Para o reconhecimento de voz, a biblioteca SpeechRecognition foi utilizada, em conjunto com a API do google, e para a conversão de texto para audio, a biblioteca pyttsx3 foi utilizada. Os comandos e respostas foram implementados a mão, visando apenas uma demonstração do que o projeto consegue fazer.
 - Para calcular a rota, foi utilizado o algorítimo A*, que utiliza uma função heurística e os vizinhos da posição para ir calculando qual o caminho mais rápido.
 - O mapa do supermercado é uma matriz numpy composta por 3 números: 0 representa a área que o carrinho pode andar livremente, 1 representa a margem de segurança para prateleiras e paredes e o 8 representas as prateleiras e paredes do supermercado.
 - Ao executar o arquivo main.py, o programa já irá calcular a melhor rota para os 5 produtos disponíveis. Para ativar o reconhecimento de voz, basta comentar a linha onde a variável 'produtos' é a lista de produtos e descomentar as linhas acima dela.

## TCC
Com a vinda da pandemia, muitos médicos tiveram que utilizar várias camadas de máscaras e aparelhos para se proteger durante o atendimento, prinicipalmente quando o atendimento requeria o uso do goniômetro, para medir o ângulo de amplitude de algum membro superior do paciente. Por conta disso, foi feito um programa para auxiliar médicos e fisioterapeutas nos exames e diagnósticos de doenças que afetam a mobilidade dos membros superiores dos pacientes, assim como no acompanhamento desses pacientes, possibilitando que mesmo a distância, os médicos possam realizar esse tipo de exame com um alto grau de confiabilidade.
 - No projeto foram utilizadas bibliotecas de realidade aumentada (OpenCV), de interface (TKinter) para que o uso do programa seja facilitado, e a biblioteca MediaPipe, que contém o modelo de rastreamento de pose humana BlazePose.
 - O blazePose consegue rastrear até 33 pontos do corpo humano, sendo uma ótima escolha para o projeto.
 - Ao executar o arquivo main.py, a pasta 'Imagem_juntas' e os outros arquivos do projeto devem estar no mesmo diretório.
 - O usuário tem a opção de escolher manualmente as juntas desejadas ou ele pode simplesmente selecionar uma das quatro opções já feitas na interface.
 - O programa necessita de uma câmera para funcionar, e isso pode ser a câmera do celular conectada via wifi com o computador, uma webcam conectada via usb ou a webcam nativa do computador. 