import random
from os import system, name

#funcao para limpar a tela a cada execucao do programa
def limpa_tela():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

banco_de_palavras = ["gato", "cachorro", "elefante", "computador", "banana", "abacaxi"]

def selecionar_palavra_aleatoria(banco_de_palavras):
    return random.choice(banco_de_palavras)

def exibir_palavra_mascarada(palavra_secreta, letras_descobertas):
    palavra_mascarada = ""
    for letra in palavra_secreta:
        if letra in letras_descobertas:
            palavra_mascarada += letra
        else:
            palavra_mascarada += ' _ '
    return palavra_mascarada

def adivinhar_letra():
    letra = input('Digite uma letra: ')
    return letra

def verificar_palpite(letra, palavra_secreta):
    if letra in palavra_secreta:
        return True
    else:
        return False



def forca():
    limpa_tela()
    print('JOGO DA FORCA\n')
    palavra_secreta = selecionar_palavra_aleatoria(banco_de_palavras)

    letras_erradas = []
    letras_descobertas = []
    chances = 6
    while chances > 0:
        letra = adivinhar_letra()
        

        if verificar_palpite(letra, palavra_secreta):
            letras_descobertas.append(letra)
            
            
            
        else:
            letras_erradas.append(letra)
            print('letras erradas')
            print(letras_erradas)
            chances -= 1

        palavra_mascarada = exibir_palavra_mascarada(palavra_secreta, letras_descobertas)
        print(palavra_mascarada)
        if '_' not in palavra_mascarada:
                print('Você venceu!')
                break
        
        
        print('chances restantes', chances)



    
    


forca()

