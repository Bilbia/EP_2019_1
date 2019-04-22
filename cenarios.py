# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 10:36:42 2019

@author: biamc
"""


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
            "batalhar": "[BATALHAR]"
        },
        "segunda":"Você entra no fumódromo. Os Insper Boys não estão em nenhum lugar à vista. Devem ter ido para a Villa Mix.",
        "opcoes2": {
                "saguao": "[SAGUÃO]",
                },
        "volta":"saguao",
        "contador":0,
        "monstro": "insperboys",
        "add":"sair"
    },
    "stand do da": {
        "titulo": "Stand do DA",
        "descricao": "Você se aproxima do stand do DA. Eles estão vendendo uma pletora de produtos temáticos da sua querida faculdade.",
        "opcoes": {
            "comprar casaco": "[COMPRAR CASACO]",
            "comprar sacochila":"[COMPRAR SACOCHILA]",
            "comprar canecao":"[COMPRAR CANECÃO]",
            "saguao":"[SAGUÃO]"
        },
        "volta":"saguao",
        "contador":2,
        "produtos":{
            "casaco":("aumenta armadura em 20 pontos",120),
            "sacochila":("aumenta capacidade do inventário em 3", 70),
            "canecao":("permite carregar água para recuperar vida. Não consumido depois do uso", 100)
            }
    },
    "catracas": {
        "titulo": "Dentro das catracas",
        "descricao": "Você passou pelas catracas e entrou no Insper. À sua frente se posiciona a bilbioteca, e nas suas laterais estão elevadores para os outros andares. Para onde deseja ir?",
        "opcoes": {
                "biblioteca": "[BIBLIOTECA]",
                "elevadores": "[ELEVADORES]",
                "saguao": "[SAGUAO]" 
                },
        "contador":0
    },
    "biblioteca":{
        "titulo":"Biblioteca",
        "descricao": "Você entra na biblioteca. O Raul parece não estar aqui também.",
        "opcoes": {
                "gritar":"[GRITAR]",
                "atendimento":"[ATENDIMENTO]",
                "catracas": "[CATRACAS]"
                },
        "contador": 0,
        "volta": "catracas",
        "segunda":"Você foi expulso da biblioteca, não deve ser uma boa ideia tentar entrar de novo"
            },
    "atendimento":{
        "descricao": "Você se aproxima do balcão de atendimento. Talvez o Raul tenha passado aqui mais cedo.",
        "opcoes": {
                "perguntar":"[PERGUNTAR]",
                "alugar livro":"[ALUGAR LIVRO]",
                "voltar": "[VOLTAR]"
                },
        "contador": 0,
        "volta": "terreo",
        "segunda":"Você foi expulso da biblioteca, não deve ser uma boa ideia tentar entrar de novo"
            },
    "elevadores":{
        "titulo": "Elevadores",
        "descricao": "Você está num elevador. Qual botão deseja apertar?",
        "opcoes": {
                "terreo": "[TERREO]",
                "1 subsolo": "[1 SUBSOLO]",
                "4 andar": "[4 ANDAR]",
                "5 andar": "[5 ANDAR]"
                },
        "contador": 0
            },
    "terreo": {
        "titulo": "Dentro das catracas",
        "descricao": "Você está dentro do Insper. À sua frente se posiciona a bilbioteca, e nas suas laterais estão elevadores para os outros andares. Para onde deseja ir?",
        "opcoes": {
                "biblioteca": "[BIBLIOTECA]",
                "elevadores": "[ELEVADORES]",
                "saguao": "[SAGUAO]" 
                },
        "contador":0
            },
    "1 subsolo":{
        "titulo": "Primeiro Subsolo",
        "descricao": "Você se encontra no primeiro subsolo. Não sei a probabilidade, mas talvez o Raul esteja no Techlab.",
        "opcoes": {
                "techlab": "[TECHLAB]",
                "elevadores": "[ELEVADORES]"
                },
        "contador":0
            },
    "4 andar":{
        "titulo": "Quarto Andar",
        "descricao": "Você se encontra no quarto andar",
        "opcoes": {
                "sala 405": "[SALA 405]",
                "jogar mario kart": "[JOGAR MARIO KART]",
                "bebedouro": "[BEBEDOURO]",
                "elevadores": "[ELEVADORES]",
                },
        "contador":0
            },
    "bebedouro":{
        "titulo": "Bebedouro",
        "descricao": "Você se aproxima do bebedouro.",
        "opcoes": {
                "beber": "[BEBER]",
                "encher canecao": "[ENCHER CANECÃO]",
                "4 andar": "[4 ANDAR]",
                },
        "contador":0
            },
    "sala 405": {
        "titulo": "Sala 405",
        "descricao": "Você entrou na sala de DesSoft. Curiosamente, o único professor que está na sala é o Humberto e os ninjas.",
        "opcoes": {
                "perguntar do raul": "[PERGUNTAR DO RAUL]",
                "sair da sala": "[SAIR DA SALA]"
                },
        "contador": 0,
        "segunda": "Você entrou na sala de DesSoft. Ela está vazia",
        "volta": "sair da sala"
        
            },
    "perguntar do raul": {
        "titulo" : "",
        "descricao": "Você perguntou sobre o Raul, mas o Humberto se recusa a responder até você entregar o EP. Aposto que você conseguiria batalhá-lo pela informação.",
        "opcoes": {
                "batalhar": "[BATALHAR]",
                "sair da sala": "[SAIR DA SALA]"
                },
        "add":"sala 405",
        "contador": 0,
        "monstro":"humberto",
        "segunda": "Você entra na sala 405. Ela está vazia"
            },
    "sair da sala": {
        "titulo": "Quarto Andar",
        "descricao": "Você está no quarto andar",
        "opcoes": {
                "sala 405": "[SALA 405]",
                "jogar mario kart": "[JOGAR MARIO KART]",
                "elevadores": "[ELEVADORES]"
                },
        "contador":0
            },
    "5 andar": {
        "titulo":"Quinto Andar",
        "descricao": "Você se encontra no quinto andar. O Raul pode estar comendo na cantina.",
        "opcoes": {
                "procurar raul": "[PROCURAR RAUL]",
                "bebedouro": "[BEBEDOURO]",
                "elevadores": "[ELEVADORES]"
                },
        "contador": 0
            },
    "techlab": {
        "titulo": "Techlab",
        "descricao": "Você entrou no techlab. Raul não está aqui, mas você vê um protótipo de um aluno brilhando no canto.",
        "opcoes": {
                "ver protótipo":"[VER PROTÓTIPO]",
                "elevadores": "[ELEVADORES]"
                },
        "contador": 0
            },
    "ver protótipo": {
        "descricao": "Você se aproxima do protótipo lentamente.\n\nPuts! Você tropeça numa peça no chão e começa a cair na direção do protótipo!\n\n*CRASH*",
        "opcoes": {
                "procurar raul": "[PROCURAR RAUL]"
                }
            }
  }
import json

arquivo_json= json.dumps(cenarios)

with open('cenarios.txt','w') as conteudo:
    conteudo.write(arquivo_json)
with open('cenarios.txt','r') as arquivo:
   conteudo = arquivo.read()
   cenarios= json.loads(conteudo)

