# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Beatriz Muniz de Castro e Silva, biamcs2000@al.edu.insper.com / biamcs2000@gmail.com
# - aluno B: Gustavo Pazemeckas, gustavorp3@al.insper.edu.br / gustavo.pazemeckas@gmail.com
#arruma o input do usuário pra ele poder escrever em qualquer formato (minúsculo ou maiúsculo) e com ou sem acentos
def arruma(string):     
    string = string.lower()     #faz todos os caracteres do input minúsculos
    s = list(string)     #faz uma lista da string para que possamos iterar sobre ela
    i = 0
    while i<len(s):
        if s[i]=="ã":
            s[i]="a"
        elif s[i]=="é":
            s[i]="e"
        elif s[i]=="ç":
            s[i]="c"
        i+=1
    string = str("".join(s))   
    return string   #junta todos os caracteres separados novamente em uma palavra só e transforma de novo em uma string


def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "Saguao do perigo",
            "descricao": "Voce esta no saguao de entrada do insper",
            "opcoes": {
                "andar professor": "Tomar o elevador para o andar do professor",
                "biblioteca": "Ir para a biblioteca"
            }
        },
        "andar professor": {
            "titulo": "Andar do desespero",
            "descricao": "Voce chegou ao andar da sala do seu professor",
            "opcoes": {
                "inicio": "Tomar o elevador para o saguao de entrada",
                "professor": "Falar com o professor"
            }
        },
        "professor": {
            "titulo": "O monstro do Python",
            "descricao": "Voce foi pedir para o professor adiar o EP. "
                         "O professor revelou que é um monstro disfarçado "
                         "e devorou sua alma.",
            "opcoes": {}
        },
        "biblioteca": {
            "titulo": "Caverna da tranquilidade",
            "descricao": "Voce esta na biblioteca",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada"
            }
        }
    }
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual


def main():
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    print()

    cenarios, nome_cenario_atual = carregar_cenarios()

    game_over = False
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]
        print("\n\n{0}\n\n". format("_"*len(cenario_atual["titulo"]))) #eu acho que fica melhor colocar a linha em cima do titulo, entre ações, apenas - Bilbia
        print(cenario_atual["titulo"])
        print("\n\n")
        print(cenario_atual["descricao"])
        print("\n\n")
        
    
        opcoes = cenario_atual['opcoes']
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:

            # Aluno B: substitua este comentário e a linha abaixo pelo código
            # para pedir a escolha do usuário.
            escolha = ""

            if escolha in opcoes:
                nome_cenario_atual = escolha
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True

    print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()
