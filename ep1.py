# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Beatriz Muniz de Castro e Silva, biamcs2000@al.edu.insper.com / biamcs2000@gmail.com
# - aluno B: Gustavo Pazemeckas, gustavorp3@al.insper.edu.br / gustavo.pazemeckas@gmail.com

import random
import json

##as funcões ok e algumas funções escolha são vazias para receber um input qualquer do usuário e agir como um "ok" -> próxima cena

#dados dos monstros
monstros = {
    "insperboys" : {
                "nome": "InsperBoys",
                "start" : "Os Insper Boys estão chocados com a sua audácia! Eles também entram na briga.",
                "ataques" : {
                        "Ostentação":10,
                        "Processo":20,
                        "Ameaça":10,
                        "Baforada na sua cara":15,
                        "Trap Music":15,
                        "Sertanejo":20
                        },
                "hp" : 30,
                "drop" : {"Vape Pen":20},
                "money": random.randint(20,100),
                "ok" : "\n\nCom a sua dignidade reinstaurada, você resolve voltar para o saguão e continuar a busca pelo Raul.\n\n",
                "volta" : "saguao"
                },
    "humberto" : {
                "nome": "Humberto e os Ninjas",
                "start" : "O Humberto está chocado que você desafiou ele, mas ele não foge da luta. Atrás dele, os ninjas também se juntam à luta.",
                "ataques" : {
                        "Dicionários":30,
                        "Exemplos complicados":20,
                        "Splash":10,
                        "Shuriken":15,
                        "Provas passadas":15
                        },
                "hp" : 120,
                "money": random.randint(20,100),
                "ok" : "\n\nPercebendo que agora é horário de atendimento em outra sala, Humberto e os Ninjas vão embora com pressa.",
                "volta" : "sair da sala"
                },
    "fernando" : {
                "nome": "Fernando",
                "start" : "O Fernando está chocado que você desafiou ele, mas ele não foge da luta. Atrás dele, os ninjas também se juntam à luta.",
                "ataques" : {
                        "Paradigma":30,
                        "APS":40,
                        "Capital Científico":10,
                        "Humanas":15,
                        "Prova sem consulta":15,
                        "Case": 15
                        },
                "hp" : 60,
                "money": random.randint(20,100),
                "ok" : "\n\nO Fernando está bem alterado devido à algo que ele fumou no fumódromo com os Insper Boys, e não pode te ajudar mais. Ele vai pro fumódromo fumar mais.",
                "drop": {"Óculos do Fernando":10},
                "volta" : "sair da sala"
                }
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


#coisas que o usuário começa com:
inventario = {"armas": {"guarda chuva": 15}, "armaduras":{}}
dinheiro = 120
hp = 50
maxhp = 50
armor = 0
capacidade = 5
    

cenarios, nome_cenario_atual = carregar_cenarios()      #permite que o usuário escolha a sala que vai voltar quando renascer
    

#função principal
def main(hp,maxhp,inventario,dinheiro,armor,capacidade,cenarios,nome_cenario_atual):
    
    tamanho_inv = len(inventario)+len(inventario["armas"])+len(inventario["armaduras"])-2
    hp=maxhp        #permite que o jogador tenha vida após voltar da morte
    
    
    #    função de combate
    def combate(monstro,hp,dinheiro,armor):
        hp_monstro = monstro["hp"]      #transforma o hp do monstro em uma variável para que possa ser calculada
        monstro_money = monstro["money"]
        
        
        #dados do insperboys que precisam ser adicionados dentro da funcão
        monstros["insperboys"]["end"]= "Parabéns! Você derrotou os Insperboys!\n\n\nNa correria para pedir um Uber para fugir, eles acabaram deixando cair a vape pen deles e {0} reais. Bem, achado não é roubado.". format(monstro_money)
        monstros["insperboys"]["vida"]=("\n\nHP InsperBoys: {0}". format(hp_monstro))
        monstros["insperboys"]["atplayer"]=("{0} atacou os Insper Boys com seu guarda chuva de {1}!". format(nome,tema_umb))
        monstros["insperboys"]["dano"]=("\n\nInsper Boys sofreram {0} de dano.\n\n". format(inventario["armas"]["guarda chuva"]))
        
        #dados do humberto e ninjas que precisam ser adicionados dentro da função
        monstros["humberto"]["end"]= "Você conseguiu derrotar o Humberto e os Ninjas de DesSoft!\n\n\nO Humberto não sabe exatamente onde está o Raul, mas ele mencionou algo sobre o Techlab. Talvez valha a pena checar.\n\nAlém da pista, eles também deixaram cair {0} reais enquanto saiam da sala.\n\n". format(monstro_money)
        monstros["humberto"]["vida"]=("\n\nHP do Humberto e dos Ninjas: {0}". format(hp_monstro))
        monstros["humberto"]["atplayer"]=("{0} atacou o Humberto e os Ninjas com seu guarda chuva de {1}!". format(nome,tema_umb))
        monstros["humberto"]["dano"]=("\n\nHumberto e os Ninjas sofreram {0} de dano.\n\n". format(inventario["armas"]["guarda chuva"]))
        
        #dados do humberto e ninjas que precisam ser adicionados dentro da função
        monstros["fernando"]["end"]= "Você conseguiu derrotar o Fernando!\n\n\nEle lhe dá os óculos dele em reconhecimento do seu Capital de Luta superior. Esse item aumenta a sua armadura em 10. Além disso ele te dá {0} pelo esforço.". format(monstro_money)
        monstros["fernando"]["vida"]=("\n\nHP do Fernando: {0}". format(hp_monstro))
        monstros["fernando"]["atplayer"]=("{0} atacou o Fernando com seu guarda chuva de {1}!". format(nome,tema_umb))
        monstros["fernando"]["dano"]=("\n\nFernando sofreu {0} de dano.\n\n". format(inventario["armas"]["guarda chuva"]))
        
        print("\n\n____________\n\n")
        print (monstro["start"])
        
        fight = True
        while fight:
            print (monstro["vida"])
            print ("HP de {0}: {1}". format(nome,hp))
            print("\n\n[ATACAR]")
            print("[FUGIR]")
            if hp<=0:
                if dinheiro>=20:
                    dinheiro-=20
                else:
                    dinheiro = 0
                print("\n\nVocê não aguentou a briga, e acabou morrendo.\n\n")
                fight=False
                escolha=""
                return escolha,dinheiro,hp
            escolha = arruma(input(": "))
            if escolha=="desistir":
                print("Você desistiu da sua procura. Uma pena, vai pegar DP em DesSoft")
                fight = False
                return escolha, dinheiro, hp
                
            elif escolha == "atacar":
                 print("\n\n____________\n\n")
                 print(monstro["atplayer"])
                 print(monstro["dano"])
                 hp_monstro-= inventario["armas"]["guarda chuva"]
                 if hp_monstro>0:
                    ataque = random.choice(list(monstro["ataques"]))
                    
                    #frase de contra-ataque baseada no ataque escolhido
                    monstros["insperboys"]["back"]=("Os Insper Boys atacaram de volta com {0}.". format(ataque))
                    monstros["humberto"]["back"]=("Humberto e os Ninjas atacaram de volta com {0}.". format(ataque))
                    monstros["fernando"]["back"]=("Fernando atacou de volta com {0}.". format(ataque))
                    
                    print(monstro["back"], "\n\n")
                    print("{0} sofreu {1} de dano.". format(nome,int(monstro["ataques"][ataque]*(1-armor/100))))      #quanto de dano o jogador recebeu
                    hp-=int(monstro["ataques"][ataque]*(1-armor/100))
                    monstro["vida"]=("\n\nHP {0}: {1}". format(monstro["nome"],hp_monstro))
                    monstro["hp"] = hp_monstro
                    
                 else:
                    print(monstro["end"])
                    if "drop" in monstro: 
                        for k in monstro["drop"]:
                            print("\n\n{0} ADICIONADA AO INVENTÁRIO". format(k.upper()))
                            inventario.update(monstro["drop"])
                    dinheiro += monstro_money
                    print("BALANÇO DA CARTEIRA: {0} REAIS". format(dinheiro))
                    monstro["hp"] = hp_monstro
                    print(monstro["ok"])
                    print("[OK]")
                    escolha = monstro["volta"]
                    cenarios[cenario_atual["add"]]["descricao"]= cenarios[cenario_atual["add"]]["segunda"]
                    cenarios[cenario_atual["add"]]["contador"]=1
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
                
    #    função do sistema de compras
    def compra(dinheiro, inventario,armor,capacidade,hp,maxhp,cenario_atual,cenarios):
        produtos={
                    "casaco":(20,"armor"),
                    "sacochila":(3,"capacidade"),
                    "canecao":"vazio"
                    }
        for k,v in produtos.items():
            if k in escolha:
                if k not in inventario:
                    if dinheiro>=cenario_atual["produtos"][k][1]:
                        print("\n\n{0}\n\n". format("_"*(len(escolha)+3)))
                        print("Você comprou um(a) {0}. Uma pena que não é de {1}.". format(k, tema_umb))
                        ok=input(": ")
                        dinheiro -= cenario_atual["produtos"][k][1]
                        inventario[k]=v
                        
                    else:
                        print("\n\n{0}\n\n". format("_"*(len(escolha)+3)))
                        print("Você não tem dinheiro suficiente para comprar um(a) {0}. Nem todo mundo pode ser Bettina nessa vida.". format (k))
                        ok=input(": ")
                else:
                    print("\n\n{0}\n\n". format("_"*(len(escolha)+3)))
                    print("Você já tem esse item.")
                    ok=input(": ")
        for k,v in produtos.items():
            if "armor" in v:
                armor+=v[0]
            elif "capacidade" in v:
                capacidade+=v[0]
            elif "hp" in v:
                hp+=v[0]
            elif "maxhp" in v:
                maxhp+=v[0]
            
        return dinheiro, inventario,armor,capacidade,hp,maxhp
    
    def heal(hp,maxhp,inventario):
        if hp<maxhp:
            hp+=20
            if hp>maxhp:
                hp = maxhp
            print("Você bebeu água e restaurou 20 HP\n")
            print ("HP de {0}: {1}\n\n[OK]". format(nome,hp))
            ok = input(": ")
        else:
            print("\n\n____________\n\n\nA sua vida já está no máximo\n\n\n[OK]")
            ok=input(": ")
        return hp, maxhp, inventario
    
    def heal_caneca(hp,maxhp,inventario):
        if "canecao" in inventario: 
            for k,v in inventario.items():
                if k=="canecao":
                    if "cheio" in v:
                        inventario["canecao"] = "vazio"
                        print("Você bebeu água e restaurou 20 HP\n\n[OK]")
                        ok=input(": ")
                        if hp<maxhp:
                            hp+=20
                            if hp>maxhp:
                                hp = maxhp
                            print("\n\n____________\n\n\nVocê bebeu água e restaurou 20 HP") 
                            print ("HP de {0}: {1}". format(nome,hp))
                    else:
                        
                        print("\n\n____________\n\n\nO seu canecão está vazio\n\n[OK]")
                        ok=input(": ")
        else:
            print("\n\n____________\n\n\nVocê não tem um canecão\n\n[OK]")
            ok=input(": ")
#        print ("HP de {0}: {1}". format(nome,hp))
        return hp, maxhp, inventario
    
    
    def encher(inventario):
        if "canecao" in inventario:
            for k,v in inventario.items():
                if k=="canecao":
                    if "vazio" in v:
                        inventario["canecao"] = "cheio"
                        print("\n\n____________\n\n\nVocê encheu o seu Canecão.\n\n\n[OK]")
                        ok=input(": ")
                    else:
                        print("\n\n____________\n\n\nO seu Canecão já está cheio.\n\n\n[OK]")
                        ok=input(": ")
        else: 
            print("n\n____________\n\n\nVocê não tem um Canecão.\n\n\n[OK]")
            ok=input(": ")
        return inventario
    

    game_over = False
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]
        if "titulo" in cenario_atual:
            print("\n\n{0}\n\n". format("_"*len(cenario_atual["titulo"]))) #eu acho que fica melhor colocar a linha em cima do titulo, entre ações, apenas - Bilbia
            print(cenario_atual["titulo"])
            print("\n\n")
            print(cenario_atual["descricao"])
            print("\n\n")
        else:    
          
            print("\n\n{0}". format("_"*20))
            print("\n\n")
            print(cenario_atual["descricao"])
            print("\n\n")
        
        if "óculos do fernando" in inventario:
            inventario["armaduras"]["oculos do fernando"]=inventario["óculos do fernando"]
            del inventario["óculos do fernando"]
            armor+=10
        
        if monstros["humberto"]["hp"]<=0:
            cenarios["elevadores"]["opcoes"]["1 subsolo"]="[1 SUBSOLO]"
        
        if "Vape Pen" in inventario: 
            inventario["armaduras"]["vape pen"]=inventario["Vape Pen"]
            armor+=20
            
            


        opcoes = cenario_atual['opcoes']
        
        #display dos cenarios caso vc já tenha visitado a sala
        if cenario_atual["contador"]==1:
            print("[OK]")
            escolha = arruma(input(": "))
            if escolha == "desistir":
                print("Você desistiu da sua procura. Uma pena, vai pegar DP em DesSoft")
                game_over=True
                return hp,maxhp,inventario,dinheiro,armor,capacidade,cenarios,nome_cenario_atual
            else:
                nome_cenario_atual = cenario_atual["volta"]
               
                

                
                
        #pede escolha e faz display no resto dos tipos de sala
        else:
            if cenario_atual["contador"]==2:
                for k,v in cenario_atual["produtos"].items():
                    print("{0}: {1}". format(k,v[0]))
                    print("Preço: R${0}\n". format(v[1]))
                print("\nBALANÇO DA CARTEIRA: {0} REAIS\n\n\n". format(dinheiro))
            for k,v in opcoes.items():
                print(v)   
            if len(opcoes) == 0:
                print("Acabaram-se suas opções! Perdeu playboy...")
                game_over = True
            else:
                escolha = arruma(input(": "))
                if escolha=="desistir":
                    print("\n\nVocê desistiu da sua procura. Uma pena, vai pegar DP em DesSoft\n\n")
                    game_over=True
                    return hp,maxhp,inventario,dinheiro,armor,capacidade,cenarios,nome_cenario_atual,escolha
                elif escolha=="usar canecao":
                    hp, maxhp, inventario = heal_caneca(hp, maxhp, inventario)
                    
                elif escolha in opcoes:
                    if escolha in cenarios: 
                        nome_cenario_atual = escolha
                        
                    elif cenario_atual["contador"]==0:
                        if escolha == "batalhar":
                            print (cenario_atual["titulo"])
                            if cenario_atual["monstro"] in monstros:
                                monstro=monstros[cenario_atual["monstro"]]
                                escolha, dinheiro, hp =combate(monstro,hp,dinheiro,armor)
                            if escolha=="desistir":
                                game_over=True
                                return hp,maxhp,inventario,dinheiro,armor,capacidade,cenarios,nome_cenario_atual,escolha
                            elif hp<=0:
                                return hp,maxhp,inventario,dinheiro,armor,capacidade,cenarios,nome_cenario_atual,escolha
                                game_over=True
                            else:
                                nome_cenario_atual = escolha
                        elif escolha == "gritar":
                            print("\n\n{0}\n\n". format("_"*(len(escolha)+3)))
                            print("Você saiu gritando para saber se alguém viu o Raul mas acabou sendo expulso da biblioteca. Honestamente, você nunca foi numa biblioteca?")
                            print("\n\n[OK]")
                            ok = input(": ")
                            cenario_atual["contador"]=1
                            cenario_atual["descricao"]=cenario_atual["segunda"]
                            if escolha=="desistir":
                                game_over=True
                                hp,maxhp,inventario,dinheiro,armor,capacidade,cenarios,nome_cenario_atual
                            else:
                                nome_cenario_atual = cenario_atual["volta"]
                                
                                
                                
                                
                        #prototipo
                        elif escolha=="ver prototipo":
                            print("\n\n{0}\n\n". format("_"*(len(escolha)+3)))
                            print("Você se aproxima do protótipo lentamente.\n\nPuts! Você tropeça numa peça no chão e começa a cair na direção do protótipo!\n\n*CRASH*\n\n\n[OK]")
                            ok=input(": ")
                            print("\n\n{0}\n\n". format("_"*(len(escolha)+3)))
                            print("Você cai direto no chão. Ué, você não estava caindo de cara no protótipo?\n\n\nVocê olha em volta. Você não está no Techlab! À sua volta, carros estão estacionados no estacionamento, nehuma máquina a vista. No seu lado, o protótipo se mescla ao resto das máquinas, mas quando vc toca nele, nada acontece. \n\n\n[ONDE ESTOU?]")
                            ok=input(": ")
                            while True:
                                print("\n\n{0}\n\n". format("_"*(len(escolha)+3)))
                                print("Você sobe até o térreo e vê o que parece o Insper, mas quase 10 anos atrás! O que deseja fazer?\n\n\n[SURTAR]\n[CHECAR O 4 ANDAR]")
                                escolha=arruma(input(": "))
                                if escolha=="surtar":
                                     print("\n\n{0}\n\n". format("_"*(len(escolha)+3)))
                                     print("Você entrou em pânico e soltou um grito de desespero no meio da entrada. Os alunos já estão acostumados. Ninguém sequer vira pra você.\n\n\n[OK]")
                                     ok=input(": ")
                                if escolha=="checar o 4 andar":
                                    print("\n\n{0}\n\n". format("_"*(len(escolha)+3)))
                                    print("Você resolve subir pra checar o 4 andar. Cadê os contâineres? Foram todos trocados por salas de aula como nos outros andares!\n\n\nVocê olha num jornal em cima de um pequeno stand e lê a data:\n\n\n22 de abril de 2006!\n\n\n[OK]")
                                    ok=input(": ")
                                    print("\n\n{0}\n\n". format("_"*(len(escolha)+3)))
                                    print("Enquanto você está suave surtando num canto, você sente alguém trombando em você.\n\n\n'Me desculpe! não estava prestando atenção!'\n\n\n[OK]")
                                    ok=input(": ")
                                    while True:
                                        print("\n\n{0}\n\n". format("_"*(len(escolha)+3)))
                                        print("Você olha com surpresa: o Raul é cabeludo!\n\n\n'Posso lhe ajudar?' ele pergunta.\n\n\n[SURTAR]\n[LAVAGEM CEREBRAL]")
                                        escolha=arruma(input(": "))
                                        if escolha=="surtar":
                                            print("\n\n{0}\n\n". format("_"*(len(escolha)+3)))
                                            print("Você começa a surtar e falar muito rápido, mas o Raul não entende nada e pede para você se acalmar.\n\n\n[OK]")
                                            ok=input(": ")
                                        if escolha=="lavagem cerebral":
                                            print("\n\n{0}\n\n". format("_"*(len(escolha)+3)))
                                            print("Você se aproxima da Raul e sussurra:\n\n\n'Se liga aqui Raul. No futuro, essa universidade vai ter um departamento de engenharia, e você vai ser professor de programação pro 1 semestre. Algum dia, uma pessoa chamada {0} vai lhe pedir pra você adiar a EP dela, e caso você não fizer isso, eu vou achar você e vou te matricular no curso de InstruMed. Acredite, você não quer isso'". format(nome))
                                            print("\n\nRaul olha pra você com medo. Ele acena a cabeça e sai de fininho\n\n\n[OK]")
                                            ok=input(": ")
                                            print("\n\n{0}\n\n". format("_"*(len(escolha)+3)))
                                            print("Depois de falar com o Raul, você volta para o estacionamento e encontra o protótipo brilhando novamente, iluminando o lugar. Sem pensar duas vezes, você corre em direção à ele e estende a sua mão.\n\n\n. . .\n\n\n[OK]")
                                            ok=input(": ")
                                            break
                                        else:
                                            print("\n\nComando inválido\n")
                                    break
                                else:
                                    print("\n\nComando inválido\n")
                                
                            nome_cenario_atual = "techlab"
                            cenarios["techlab"]["descricao"]= cenarios["techlab"]["segunda"]
                            del cenarios["techlab"]["opcoes"]["ver prototipo"]
                            cenarios["elevadores"]["opcoes"]["6 andar"]="[6 ANDAR]"
                            
                        elif escolha=="6 andar":
                            print("\n\n{0}\n\n". format("_"*(len(escolha)+3)))
                            print("Você se encontra no 6 andar. Numa mesa perto de você, o Raul está programando no seu laptop.\n\n\n[FALAR COM ELE]\n\n\n")
                            ok=input(": ")
                            print("\n\n{0}\n\n". format("_"*(len(escolha)+3)))
                            print("Você chega perto o suficiente do Raul para que ele possa lhe ouvir.\n\n\n'Boa tarde Raul, posso falar com você? Eu preciso de um adiamento da EP' \n\n\nO Raul levanta os olhos do computador, e quando ele vê que é você falando, seus olhos brilham com reconhecimento e medo\n\n\n'Mas é claro, {0}. Pode me entregar no final da semana.'\n\n\nVocê vai embora, comemorando a sua vitória e o tempo extra de procastinação.\n\n\n[FIM]")
                            ok=input(": ")
                            print("\n\n{0}\n\n". format("_"*(len(escolha)+3)))
                            print("PARABÉNS, VOCÊ CONSEGUIU ADIAR A SUA EP E GANHOU O JOGO! AGORA VAI LÁ FAZER O TRABALHO DE MODSIM")
                            game_over= True
                            
                            
                            
                                    
                                    
                                    
                                    
        
                                
                      
                            
                            
                        elif escolha=="beber":
                            print("\n\n{0}\n\n". format("_"*(len(escolha)+3)))
                            hp, maxhp, inventario = heal(hp, maxhp, inventario)
                            print ("HP de {0}: {1}". format(nome,hp))
                        elif escolha=="encher canecao":
                            inventario = encher(inventario)
                        elif escolha=="voltar":
                            nome_cenario_atual=cenario_atual["volta"]
                            
                            
                        elif escolha=="livro de python":
                            if tamanho_inv<capacidade:
                                print("\n\n{0}\n\n". format("_"*(len(escolha)+3)))
                                print("Você alugou o livro de Python. Isso lhe promove um aumento no seu dano de 20%.\n\n[OK]")
                                inventario["livro de python"]=0.2
                                inventario["armas"]["guarda chuva"]=int(inventario["armas"]["guarda chuva"]*(1+inventario["livro de python"]))
                                ok=input(": ")
                                cenarios["alugar livro"]["contador"]=1
                                nome_cenario_atual=cenario_atual["volta"]
                                cenarios["alugar livro"]["descricao"]=cenarios["alugar livro"]["segunda"]
                            else:
                                print("\n\n{0}\n\n". format("_"*(len(escolha)+3)))
                                print("Você não tem espaço no seu inventário. Deseja retirar algo?")
                                escolha=arruma(input(": "))
                                if escolha=="sim":
                                    while True:
                                        print("\n\n{0}\n\n". format("_"*(len(escolha)+3)))
                                        print("Escolha um item para retirar:\n\n")
                                        for k in inventario:
                                            if k not in ("armas", "armaduras"):
                                                print (k.upper())
                                            if k in ("armas", "armaduras"):
                                                for a in inventario[k]:
                                                    print (a.upper())
                                        escolha=arruma(input("\n\n: "))
                                        if escolha in inventario:
                                            if escolha in inventario["armas"] or escolha in inventario["armaduras"]:
                                                print("\n\n{0}\n\n". format("_"*(len(escolha)+3)))
                                                print("Você não pode remover esse item.\n\n\n[OK]")
                                                ok=input(": ")
                                            else: 
                                                print("\n\n{0}\n\n". format("_"*(len(escolha)+3)))
                                                print("Você retirou {0} do seu inventário e pegou o livro de Python. Isso lhe promove um aumento no seu dano de 20%\n\n\n[OK]". format(escolha))
                                                del inventario["{0}". format(escolha)]
                                                inventario["livro de python"]=0.2
                                                ok=input(": ")
                                                cenarios["alugar livro"]["contador"]==1
                                                nome_cenario_atual=cenario_atual["volta"]
                                                break
                                else:
                                    print("\n\n{0}\n\n". format("_"*(len(escolha)+3)))
                                    print("Você resolveu não alugar nenhum livro.\n\n\n[OK]")
                                    ok = input(": ")
                                    nome_cenario_atual=cenario_atual["volta"]
                                    
                                    
                        elif escolha=="livro do golem":
                            if tamanho_inv<capacidade:
                                print("\n\n{0}\n\n". format("_"*(len(escolha)+3)))
                                print("Você alugou o livro do Golem. Isso permite que você cancele a APS do Fernando.\n\n[OK]")
                                inventario["livro do golem"]="sem aps"
                                del monstros["fernando"]["ataques"]["APS"]
                                ok=input(": ")
                                cenarios["alugar livro"]["contador"]=1
                                nome_cenario_atual=cenario_atual["volta"]
                                cenarios["alugar livro"]["descricao"]=cenarios["alugar livro"]["segunda"]
                            else:
                                print("\n\n{0}\n\n". format("_"*(len(escolha)+3)))
                                print("Você não tem espaço no seu inventário. Deseja retirar algo?")
                                escolha=arruma(input(": "))
                                if escolha=="sim":
                                    while True:
                                        print("\n\n{0}\n\n". format("_"*(len(escolha)+3)))
                                        print("Escolha um item para retirar:\n\n")
                                        for k in inventario:
                                            if k not in ("armas", "armaduras"):
                                                print (k.upper())
                                            if k in ("armas", "armaduras"):
                                                for a in inventario[k]:
                                                    print (a.upper())
                                        escolha=arruma(input("\n\n: "))
                                        if escolha in inventario:
                                            if escolha in inventario["armas"] or escolha in inventario["armaduras"]:
                                                print("\n\n{0}\n\n". format("_"*(len(escolha)+3)))
                                                print("Você não pode remover esse item.\n\n\n[OK]")
                                                ok=input(": ")
                                            else: 
                                                print("\n\n{0}\n\n". format("_"*(len(escolha)+3)))
                                                print("Você retirou {0} do seu inventário e pegou o livro do Golem. Isse livro cancela a APS do Fernando.". format(escolha))
                                                del inventario["{0}". format(escolha)]
                                                del monstros["fernando"]["ataques"]["APS"]
                                                inventario["livro do golem"]="sem aps"
                                                ok=input(": ")
                                                cenarios["alugar livro"]["contador"]==1
                                                nome_cenario_atual=cenario_atual["volta"]
                                                break
                                else:
                                    print("\n\n{0}\n\n". format("_"*(len(escolha)+3)))
                                    print("Você resolveu não alugar nenhum livro.\n\n\n[OK]")
                                    ok = input(": ")
                                    nome_cenario_atual=cenario_atual["volta"]
                                    
                                    
                        elif escolha=="livro de engineering design":
                            if tamanho_inv<capacidade:
                                print("\n\n{0}\n\n". format("_"*(len(escolha)+3)))
                                print("Você alugou o livro de Engineering Design. Com esses novos conhecimentos, você é capaz de fazer um upgrade no seu Guarda Chuva, aumentando o seu dano em 8.\n\n\n[OK]")
                                inventario["livro de engineering design"]=8
                                inventario["armas"]["guarda chuva"]=int(inventario["armas"]["guarda chuva"]+8)
                                ok=input(": ")
                                cenarios["alugar livro"]["contador"]=1
                                nome_cenario_atual=cenario_atual["volta"]
                                cenarios["alugar livro"]["descricao"]=cenarios["alugar livro"]["segunda"]
                            else:
                                print("\n\n{0}\n\n". format("_"*(len(escolha)+3)))
                                print("Você não tem espaço no seu inventário. Deseja retirar algo?")
                                escolha=arruma(input(": "))
                                if escolha=="sim":
                                    while True:
                                        print("\n\n{0}\n\n". format("_"*(len(escolha)+3)))
                                        print("Escolha um item para retirar:\n\n")
                                        for k in inventario:
                                            if k not in ("armas", "armaduras"):
                                                print (k.upper())
                                            if k in ("armas", "armaduras"):
                                                for a in inventario[k]:
                                                    print (a.upper())
                                        escolha=arruma(input("\n\n: "))
                                        if escolha in inventario:
                                            if escolha in inventario["armas"] or escolha in inventario["armaduras"]:
                                                print("\n\n{0}\n\n". format("_"*(len(escolha)+3)))
                                                print("Você não pode remover esse item.\n\n\n[OK]")
                                                ok=input(": ")
                                            else: 
                                                print("\n\n{0}\n\n". format("_"*(len(escolha)+3)))
                                                print("Você retirou {0} do seu inventário e pegou o livro de Engineering Design. Com esses novos conhecimentos, você é capaz de fazer um upgrade no seu Guarda Chuva, aumentando o seu dano em 8.". format(escolha))
                                                del inventario["{0}". format(escolha)]
                                                inventario["armas"]["guarda chuva"]=int(inventario["armas"]["guarda chuva"]+8)
                                                inventario["livro de engineering design"]=8
                                                ok=input(": ")
                                                cenarios["alugar livro"]["contador"]==1
                                                nome_cenario_atual=cenario_atual["volta"]
                                                break
                                else:
                                    print("\n\n{0}\n\n". format("_"*(len(escolha)+3)))
                                    print("Você resolveu não alugar nenhum livro.\n\n\n[OK]")
                                    ok = input(": ")
                                    nome_cenario_atual=cenario_atual["volta"]
                                    
                                            
                        elif escolha=="jogar mario kart":
                            print("\n\n{0}\n\n". format("_"*(len(escolha)+3)))
                            print("Você resolveu jogar Mario Kart com uns veteranos. Não vejo como isso te ajuda, você tá só perdendo tempo da sua busca\n\n\n[OK]")
                            ok=input(": ")
                            
                                                
                                    
                    
                            
                        else:
                            print("\n\nComando inválido\n")
                    elif cenario_atual["contador"]==2:
                        dinheiro,inventario,armor,capacidade,hp,maxhp = compra(dinheiro, inventario,armor,capacidade,hp,maxhp,cenario_atual,cenarios)
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
    hp,maxhp,inventario,dinheiro,armor,capacidade,cenarios,nome_cenario_atual,escolha = main(hp,maxhp,inventario,dinheiro,armor,capacidade,cenarios,nome_cenario_atual)
    while hp<=0 and escolha=="desistir":
        with open('Binha_Noza.txt','r') as arquivo:
           conteudo = arquivo.read()
           print (conteudo)
           while hp<=0:
               print("\n\nCaso você se lembre do nome de uma sala, você pode se teleportar pra ela para voltar ao jogo\n\n")
               escolha=arruma(input(": "))
               if escolha in cenarios:
                   nome_cenario_atual = escolha
                   main(hp,maxhp,inventario,dinheiro,armor,capacidade,cenarios,nome_cenario_atual)
               else:
                    break