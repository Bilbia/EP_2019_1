# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Beatriz Muniz de Castro e Silva, biamcs2000@al.edu.insper.com / biamcs2000@gmail.com
# - aluno B: Gustavo Pazemeckas, gustavorp3@al.insper.edu.br / gustavo.pazemeckas@gmail.com
import random

##as funcões ok e algumas funções escolha são vazias para receber um input qualquer do usuário e agir como um "ok" -> próxima cena

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
humberto = {
            "nome": "Humberto e os Ninjas",
            "start" : "O Humberto está chocado que você desafiou ele, mas ele não foge da luta. Atrás dele, os ninjas também se juntam à luta.",
            "ataques" : {
                    "Dicionários":30,
                    "Exemplos complicados":20,
                    "Splash":10,
                    "Shuriken":15,
                    "Provas passadas":15
                    },
            "dano" : ("\n\nHumberto e os ninjas sofreram {0} de dano.\n\n". format(inventario["Armas"]["Guarda Chuva"])),
            "hp" : 50,
            "money": random.randint(20,100),
            "ok" : "\n\nVocê conseguiu derrotar o Humberto e os Ninjas de DesSoft!\n\nO Humberto não sabe exatamente onde está o Raul, mas mencionou o Techlab. Talvez você devesse ir lá checar.",
            "volta" : "sair da sala"
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
    with open('cenarios.txt','r') as arquivo:
       conteudo = arquivo.read()
       cenarios= json.loads(conteudo)
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
    
    
    #    função de combate
    def combate(monstro,hp,dinheiro,armor):
        hp_monstro = monstro["hp"]      #transforma o hp do monstro em uma variável para que possa ser calculada
        
        #dados do insperboys que precisam ser adicionados dentro da funcão
        insb_money = random.randint(20,100)
        insperboys["end"]= "Parabéns! Você derrotou os Insperboys!\n\n\nNa correria para pedir um Uber para fugir, eles acabaram deixando cair a vape pen deles e {0} reais. Bem, achado não é roubado.". format(insb_money)
        insperboys["vida"]=("\n\nHP InsperBoys: {0}". format(hp_monstro))
        insperboys["atplayer"]=("{0} atacou os Insper Boys com seu guarda chuva de {1}!". format(nome,tema_umb))
        
        print("\n\n____________\n\n")
        print (monstro["start"])
        
        fight = True
        while fight:
            print (monstro["vida"])
            print ("HP de {0}: {1}". format(nome,hp))
            print("\n\n[ATACAR]")
            print("[FUGIR]")
            escolha = arruma(input(": "))
            if escolha=="desistir":
                print("Você desistiu da sua procura. Uma pena, vai pegar DP em DesSoft")
                fight = False
                return escolha, dinheiro, hp
                
            elif escolha == "atacar":
                 print("\n\n____________\n\n")
                 print(monstro["atplayer"])
                 print(monstro["dano"])
                 hp_monstro-= inventario["Armas"]["Guarda Chuva"]
                 if hp_monstro>0:
                    ataque = random.choice(list(monstro["ataques"]))
                    
                    #frase de contra-ataque baseada no ataque escolhido
                    insperboys["back"]=("Os Insper Boys atacaram de volta com {0}.". format(ataque))
                    
                    print(monstro["back"], "\n\n")
                    print("{0} sofreu {1} de dano.". format(nome,int(monstro["ataques"][ataque]*(1-armor/100))))      #quanto de dano o jogador recebeu
                    hp-=int(monstro["ataques"][ataque]*(1-armor/100))
                    monstro["vida"]=("\n\nHP {0}: {1}". format(monstro["nome"],hp_monstro))
                    monstro["hp"] = hp_monstro
                    
                 else:
                    print(monstro["end"])
                    for k in monstro["drop"]:
                        print("\n\n{0} ADICIONADA AO INVENTÁRIO". format(k.upper()))
                    dinheiro += insb_money
                    print("BALANÇO DA CARTEIRA: {0} REAIS". format(dinheiro))
                    inventario.update(monstro["drop"])
                    insperboys["hp"] = hp_monstro
                    print(monstro["ok"])
                    print("[OK]")
                    escolha = monstro["volta"]
                    cenario_atual["descricao"]= cenario_atual["segunda"]
                    cenario_atual["contador"]=1
                    ok = input(": ")
                    fight = False
                    return escolha, dinheiro, hp
            elif escolha == "fugir":
                print("\n\n____________\n\n")
                print("Você não aguentou a briga e resolveu fugir de volta para o saguão!\n\n")
                print("[OK]")
                escolha = monstro["volta"]
                ok = input(": ")
                fight = False
                return escolha, dinheiro, hp
            else:
                print("\n\nComando inválido")
                print("\n\n____________")
            

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
        
        #display dos cenarios caso vc já tenha visitado a sala
        if cenario_atual["contador"]==1:
            print("[OK]")
            escolha = arruma(input(": "))
            if escolha == "desistir":
                print("Você desistiu da sua procura. Uma pena, vai pegar DP em DesSoft")
                game_over=True
            else:
                nome_cenario_atual = cenario_atual["volta"]
                
                
        #display dos cenarios normais ou de combate
        else:
            for k,v in opcoes.items():
                print(v)   
            if len(opcoes) == 0:
                print("Acabaram-se suas opções! Perdeu playboy...")
                game_over = True
            else:
                escolha = arruma(input(": "))
                if escolha=="desistir":
                    print("\n\nVocê desistiu da sua procura. Uma pena, vai pegar DP em DesSoft")
                    game_over=True       
                elif escolha in opcoes:
                    if escolha in cenarios: 
                        nome_cenario_atual = escolha
                    elif cenario_atual["contador"]==0:
                        if escolha == "brigar":
                            escolha, dinheiro, hp =combate(insperboys,hp,dinheiro,armor)
                            if escolha=="desistir":
                                game_over=True
                            else:
                                nome_cenario_atual = escolha
                        
                       
                            
                        else:
                            print("\n\nComando inválido\n")
                    elif cenario_atual["contador"]==1:
                        ok = input(": ")
                        escolha = cenario_atual["volta"]
                    else:
                        print("\n\nComando inválido\n")
                        escolha = arruma(input(": "))
                   
                else:
                    print("\n\nComando inválido")


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
