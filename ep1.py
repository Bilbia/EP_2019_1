# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Beatriz Muniz de Castro e Silva, biamcs2000@al.edu.insper.com / biamcs2000@gmail.com
# - aluno B: Gustavo Pazemeckas, gustavorp3@al.insper.edu.br / gustavo.pazemeckas@gmail.com
import random

#dados dos monstros
insperboys = {
            "nome": "InsperBoys",
            "start" : "Os Insper Boys estão chocados com a sua audácia! Eles também entram na briga.",
            "ataques" : {
                    "Ostentação":10,
                    "Processo":20,
                    "Ameaça":10,
                    "Baforada na sua cara":15
                    },
            "dano" : ("\n\nInsper Boys sofreram {0} de dano.\n\n". format(inventario["Armas"]["Guarda Chuva"])),
            "hp" : 30,
            "drop" : {"Vape Pen":20},
            "money": random.randint(20,100),
            "ok" : "\n\nCom a sua dignidade reinstaurada, você resolve voltar para o saguão e continuar a busca pelo Raul.\n\n",
            "volta" : "saguao"
            }

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

#carrega os cenarios
def carregar_cenarios():
    cenarios = {
        "saguao": {
                "titulo": "Saguão do Insper",
                "descricao": "Você está no saguão do Insper. À sua frente, as catracas se colocam entre você e o Insper em si. À sua esquerda, integrantes do DA estão vendendo diversos objetos temáticos da facool. Atrás de você, as portas levam para o fumódromo.",
                "opcoes": {
                    "catracas" : "[CATRACAS]",
                    "stand do da": "[STAND DO DA]",
                    "sair": "[SAIR]"
                },
                "contador":0
            },
            "sair": {
                "titulo": "Fumódromo",
                "descricao": "Você entra no fumódromo. À sua volta, deveros Insper Boys fumam seus vapes e cigarros, mas você não vê o Raul em lugar nenhum.\n\nComo assim?! Os Insper Boys estão zuando o seu guarda chuva de {0}! Você pode atacá-los para defender sua dignidade ou voltar para o saguão e continuar procurando o Raul.". format(tema_umb),
                "opcoes": {
                    "saguao": "[SAGUÃO]",
                    "brigar": "[BRIGAR]"
                },
                "segunda":"Você entra no fumódromo. Os Insper Boys não estão em nenhum lugar à vista. Devem ter ido para a Villa Mix.",
                "opcoes2": {
                        "saguao": "[SAGUÃO]",
                        },
                "volta":"saguao",
                "contador":0
            },
            "stand do da": {
                "titulo": "Stand do DA",
                "descricao": "Você se aproxima do stand do DA. Eles estão vendendo uma pletora de produtos temáticos da sua querida faculdade.",
                "opcoes": {
                    "comprar casaco": "[COMPRAR CASACO]",
                    "comprar sacochila":"[COMPRAR SACOCHILA]",
                    "comprar canecao":"[COMPRAR CANECÃO]",
                    "saguao":"[SAGUÃO]"
                    }
            }
        }
    nome_cenario_atual = "saguao"
    return cenarios, nome_cenario_atual


def main():
     #coisas que o usuário começa com:
    inventario = {"Armas": {"Guarda Chuva": 15}, "Armaduras":{}}
    dinheiro = 120
    hp = 50
    maxhp = 50
    armor = 0
    capacidade = 5

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
    comeco = True
    while comeco:
        print("\n\n____________________\n\n")
        print("DIGITE 1 PARA COMEÇAR OU 2 PARA LIGAR PARA O ATENDIMENTO AO CONSUMIDOR")
        start = input (": ")
        if start == "2":
            print("\n\nBEM VINDO AO ATENDIMENTO AO CONSUMIDOR. QUAL A SUA QUEIXA?")
            ok = input(": ") #variável vazia que não será usada, apenas para requisitar um "ok" do jogador ou outras perguntas/inputs que não mudam nada no jogo
            print("\n\nÉ UMA PENA, SUA RECLAMAÇÃO SÓ PODERÁ SER ATENDIDA APÓS A ENTREGA DO SEU EP. POR FAVOR, PROCURE O RAUL PARA RETIFICAR ESSE PROBLEMA.")
            print("\n\n[OK]")
            ok = input(": ")
            comeco = False
        elif start == "1":
            print("\n\nVamos direto ao ponto então, se é assim.\n\n")
            print("[OK]")
            ok = input(": ")
            comeco = False
        else:
            print("\n\nVocê acha que você é o bichão mesmo né? Engraçadão você. Vamos tentar de novo")
    print("\n\n____________\n\n")   
    print("Oh não! É o dia da entrega da sua EP de DesSoft e você ainda não terminou a sua!\n\n")
    print("Se você não entregar essa EP, você vai ficar de DP em DesSoft. Precisamos achar o Raul para ver se conseguimos adiar a entrega!\n\n")
    print("Primeiramente, qual o seu nome?")
    nome = input(": ")
    print("\n\nÓtimo. E qual o seu jogo/anime/cartoon favorito?")
    tema_umb = input(": ")
    print("\n\nMassa. Mas voltando agora pra todo aquele negócio de ter que encontrar o Raul:\n\n")
    print("[OK]")
    ok = input(": ")
    main()
