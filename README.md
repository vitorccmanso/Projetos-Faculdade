# Projetos realizados durante a faculdade

## Carrinho acessível:
Projeto voltado para ajudar pessoas com algum grau de deficiência visual a realizar comprar no mercado. Essas pessoas teriam acesso a um carrinho especial que seria controlado por voz e calcularia a rota mais rápida pelo supermercado com base nos produtos citados.
 - Para o reconhecimento de voz, a biblioteca SpeechRecognition foi utilizada, em conjunto com a API do google, e para a conversão de texto para audio, a biblioteca pyttsx3 foi utilizada. Os comandos e respostas foram implementados a mão, visando apenas uma demonstração do que o projeto consegue fazer.
 - Para calcular a rota, foi utilizado o algorítimo A*, que utiliza uma função heurística e os vizinhos da posição para ir calculando qual o caminho mais rápido.
 - O mapa do supermercado é uma matriz numpy composta por 3 números: 0 representa a área que o carrinho pode andar livremente, 1 representa a margem de segurança para prateleiras e paredes e o 8 representas as prateleiras e paredes do supermercado.
 - Ao executar o arquivo main.py, o programa já irá calcular a melhor rota para os 5 produtos disponíveis. Para ativar o reconhecimento de voz, basta comentar a linha onde a variável 'produtos' é a lista de produtos e descomentar as linhas acima dela.