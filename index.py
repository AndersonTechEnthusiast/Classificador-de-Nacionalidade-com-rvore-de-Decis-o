# -*- coding: utf-8 -*-
from sklearn.tree import DecisionTreeClassifier # DecisionTreeClassifier | Arvore de Decisão Classificada
import time
from colorama import init
from colorama import Fore
# Variáveis Independentes  
# Tabela  
#  
#      - OLHOS -         |       - CABELO -        |           - ALTURA -            |         - COR -        |  
#  
# Olhos Verdes    = [0]  | Cabelos Castanhos = [0] |  Alta (+170cm)           = [0]  |   Amarela = [0]        |  
# Olhos Azuis     = [1]  | Cabelos Loiros    = [1] |  Média (150cm a 160cm)   = [1]  |   Branco  = [1]        |  
# Olhos Castanhos = [2]  | Cabelos Ruivos    = [2] |  Baixa (-150cm)          = [2]  |   Negro   = [2]        |  
#  
# Nacionalidade  
#              [PN]                             [PB]                            [Pb]                           [A]  
#      - PAÍSES NÓRDICOS -       |      - PAÍSES BÁLTICOS -       |      - PAÍSES BAIXOS -         |      - ALEMANHA -       |  
#           [1,1,0,1]            |           [1,1,0,1]            |           [1,1,0,1]            |         [1,1,0,1]       |  
#           [0,1,0,1]            |           [0,1,1,1]            |           [0,1,0,1]            |         [0,0,0,1]       |  
#           [0,1,1,1]            |           [0,1,0,1]            |           [1,1,1,1]            |         [0,0,1,1]       |  
#           [1,1,1,1]            |           [1,1,1,1]            |           [2,1,0,1]            |         [2,0,1,1]       |  
#                                                                                                  |         [2,1,0,1]       |  
#           [E]                                [B]                              [Í]                             [C]
#      - ESPANHA -               |         - BRASIL -             |         - ÍNDIA -             |         - CHINA -       |  
#           [0,0,1,1]            |          [0,0,1,1]             |          [2,0,2,0]            |          [2,0,2,0]      |  
#           [2,0,1,1]            |          [2,1,1,1]             |          [2,0,2,0]            |          [2,0,2,0]      |  
#           [2,1,0,1]            |          [2,0,1,1]             |          [2,0,2,0]            |          [2,0,2,0]      |  
#           [2,1,1,1]            |          [1,1,1,1]             |                               |                         |  
#                                                                                                 |                         | 
#               [ÁS] 
#      - ÁFRICA SUBSAARIANA -    |  
#           [2,0,2,2]            |  
#           [2,0,2,2]            |  
#           [2,0,2,2]            |  
#           [2,0,2,2]            |  

X_ = [
    [1,1,0,1],[1,1,0,1],[1,1,0,1],[1,1,0,1],[0,0,1,1],[0,0,1,1],[2,0,2,0],[2,0,2,0],[2,0,2,2],
    [0,1,0,1],[0,1,1,1],[0,1,0,1],[0,0,0,1],[2,0,1,1],[2,1,1,1],[2,0,2,0],[2,0,2,0],[2,0,2,2],
    [0,1,1,1],[0,1,0,1],[1,1,1,1],[0,0,1,1],[2,1,0,1],[2,0,1,1],[2,0,2,0],[2,0,2,0],[2,0,2,2],
    [1,1,1,1],[1,1,1,1],[2,1,0,1],[2,0,1,1],[2,1,1,1],[1,1,1,1],[2,0,2,2],
    [2,1,0,1],
] 
#  Variaveis Dependentes
Y_ = [
    "PAÍSES NÓRDICOS","PAÍSES BÁLTICOS","PAÍSES BAIXOS","ALEMANHA","ESPANHA","BRASIL","ÍNDIA","CHINA","ÁFRICA SUBSAARIANA",
    "PAÍSES NÓRDICOS","PAÍSES BÁLTICOS","PAÍSES BAIXOS","ALEMANHA","ESPANHA","BRASIL","ÍNDIA","CHINA","ÁFRICA SUBSAARIANA",
    "PAÍSES NÓRDICOS","PAÍSES BÁLTICOS","PAÍSES BAIXOS","ALEMANHA","ESPANHA","BRASIL","ÍNDIA","CHINA","ÁFRICA SUBSAARIANA",
    "PAÍSES NÓRDICOS","PAÍSES BÁLTICOS","PAÍSES BAIXOS","ALEMANHA","ESPANHA","BRASIL","ÁFRICA SUBSAARIANA",
    "ALEMANHA"
] 
PN = [f'{Fore.WHITE}Você Pode Ter Descêndentes em sua Árvore Genealogica no País:{Fore.GREEN} Dinamarca',f'{Fore.WHITE}Você Pode Ter Descêndentes em sua Árvore Genealogica no País:{Fore.GREEN} Noruega',f'{Fore.WHITE}Você Pode Ter Descêndentes em sua Árvore Genealogica no País:{Fore.GREEN} Suécia',f'{Fore.WHITE}Você Pode Ter Descêndentes em sua Árvore Genealogica no País:{Fore.GREEN} Filândia',f'{Fore.WHITE}Você Pode Ter Descêndentes em sua Árvore Genealogica no País:{Fore.GREEN} Islândia']
PB = [f'{Fore.WHITE}Você Pode Ter Descêndentes em sua Árvore Genealogica no País:{Fore.GREEN} Estônia',f'{Fore.WHITE}Você Pode Ter Descêndentes em sua Árvore Genealogica no País:{Fore.GREEN} Letônia',f'{Fore.WHITE}Você Pode Ter Descêndentes em sua Árvore Genealogica no País:{Fore.GREEN} Lituânia']
Pb = [f'{Fore.WHITE}Você Pode Ter Descêndentes em sua Árvore Genealogica no País:{Fore.GREEN} Amsterdã',f'{Fore.WHITE}Você Pode Ter Descêndentes em sua Árvore Genealogica no País:{Fore.GREEN} Roterdã']
AS = [f'{Fore.WHITE}Você Pode Ter Descêndentes em sua Árvore Genealogica no País:{Fore.GREEN} Nigéria',f'{Fore.WHITE}Você Pode Ter Descêndentes em sua Árvore Genealogica no País:{Fore.GREEN} Gana',f'{Fore.WHITE}Você Pode Ter Descêndentes em sua Árvore Genealogica no País:{Fore.GREEN} Senegal',f'{Fore.WHITE}Você Pode Ter Descêndentes em sua Árvore Genealogica no País:{Fore.GREEN} República Democrática do Congo',f'{Fore.WHITE}Você Pode Ter Descêndentes em sua Árvore Genealogica no País:{Fore.GREEN} Angola',f'{Fore.WHITE}Você Pode Ter Descêndentes em sua Árvore Genealogica no País:{Fore.GREEN} Camarões',f'{Fore.WHITE}Você Pode Ter Descêndentes em sua Árvore Genealogica no País:{Fore.GREEN} Quênia',f'{Fore.WHITE}Você Pode Ter Descêndentes em sua Árvore Genealogica no País:{Fore.GREEN} Tanzânia',f'{Fore.WHITE}Você Pode Ter Descêndentes em sua Árvore Genealogica no País:{Fore.GREEN} Etiópia África do Sul',f'{Fore.WHITE}Você Pode Ter Descêndentes em sua Árvore Genealogica no País:{Fore.GREEN} Moçambique',f'{Fore.WHITE}Você Pode Ter Descêndentes em sua Árvore Genealogica no País:{Fore.GREEN} Namíbia']

# cria um Modelo e usa diretamente o .fit direto na instância da Classe DecisionTreeClassifier()
# .fit() = "Ajustar"/"Treinar"
Modelo = DecisionTreeClassifier().fit(X=X_,y=Y_)

def ReturnsAlerts(param):
    if isinstance(param , int):
        if param == 0:
            ALERT_ = f"{Fore.YELLOW} ⚠️  Valor Inválido  ⚠️"
            return ALERT_
        elif param == 1:
            ERROR_ = f"❌  {Fore.RED}ERROR  ❌ {Fore.WHITE}"
            return ERROR_
    else:
        print("Error de Parametros")
        exit
        
def Eyes(eye):
    if isinstance(eye , str):
        table_eyes = ['verdes','azuis','castanhos']
        table_nums = {'verdes':0,'azuis':1,'castanhos':2}
        
        while eye.strip().lower() not in table_eyes:
            print("\n")
            for i in str(ReturnsAlerts(0)):
                time.sleep(.01)
                print(f"{i}",end="",flush=True)
                time.sleep(.01)
            print("\n")
            for i in str(ReturnsAlerts(1)):
                time.sleep(.01)
                print(f"{i}",end="",flush=True)
                time.sleep(.01)
            print("\n")
            eye = input("🔹  Qual a Cor dos seus Olhos ?")
        _RESULT = None
        for i in table_eyes:
            if str(i) == str(eye).strip().lower():
                _RESULT = int(table_nums[str(i)])
                break
        return _RESULT
    else:
        STOP_ = "NOT_STRING"
        return STOP_
def Hairs(hair):
    if isinstance(hair , str):
        table_hairs = ['castanhos','loiros','ruivos']
        table_nums = {'castanhos':0,'loiros':1,'ruivos':2}
        while str(hair).strip().lower() not in table_hairs:
            print("\n")
            for i in str(ReturnsAlerts(0)):
                time.sleep(.01)
                print(f"{i}",end="",flush=True)
                time.sleep(.01)
            print("\n")
            for i in str(ReturnsAlerts(1)):
                time.sleep(.01)
                print(f"{i}",end="",flush=True)
                time.sleep(.01)
            print("\n")
            hair = input("🔹  Qual a cor dos seus Cabelos ?")
        _RESULT = None
        for i in table_hairs:
            if str(i).strip().lower() == str(hair).strip().lower():
                _RESULT = int(table_nums[str(i)])
                break
        return _RESULT
    else:
        STOP_ = "NOT_STRING"
        return STOP_
def Heights(height):
    Tall = 180
    Medium_min,Medium_max = [150,170]
    HEIGHT_ = None
    _RESULT = None
    table_num = {'alta':0,'média':1,'baixa':2}
    if '.' in height:
        height = float(height)
    else:
        height = int(height)
    if isinstance(height, int):
        if height < Medium_min:
            HEIGHT_ = "BAIXA_"
        elif height >= Medium_min and height <= Medium_max:
            HEIGHT_ = "MÉDIA_"
        elif height >= Tall:
            HEIGHT_ = "ALTA_"
        _RESULT = int(table_num[str(HEIGHT_).lower().replace('_','')])
        return _RESULT
    if isinstance(height , float):
        height_m = round(height,2)
        # [KM-HM-HAM-M-DM-CM-MM] * x10 -> de KM para grandezas menores multiplica por x10 para cada grandeza multiplica-se por x10
        # [KM-HM-HAM-M-DM-CM-MM] * /10 <- de M para grandezas maiores dividi-se por /10 para cada grandeza dividi-se por x10
        height_dm = round(height_m,2) * 10
        height_cm = round(height_dm,2) * 10
        height_cm = int(height_cm)
        if height_cm < Medium_min:
            HEIGHT_ = "BAIXA_"
        elif height_cm >= Medium_min and height_cm <= Medium_max:
            HEIGHT_ = "MÉDIA_"
        elif height_cm >= Tall:
            HEIGHT_ = "ALTA_"
        _RESULT = table_num[str(HEIGHT_).lower().replace('_','')]
        return _RESULT
    else:
        STOP_ = "NOT_INT"
        return STOP_
def Colors(color):
    if isinstance(color , str):
        COLOR_ = None
        table_color = ['branca','amarela','negra']
        table_nums = {'amarela':0,'branca':1,'negra':2}
        while str(color).strip().lower() not in table_color:
            for i in str(ReturnsAlerts(0)):
                time.sleep(.01)
                print(f"{i}",end="",flush=True)
                time.sleep(.01)
            print("\n")
            for i in str(ReturnsAlerts(1)):
                time.sleep(.01)
                print(f"{i}",end="",flush=True)
                time.sleep(.01)
            print("\n")
            color = input("🔹  Qual a Cor de Sua Pele ?")
        for i in table_nums:
            if str(i).strip().lower() == str(color).strip().lower():
                COLOR_ = int(table_nums[str(i).strip().lower()])
                break
        return COLOR_
    else:
        STOP_ = "NOT_STRING"
        return STOP_
# cria uma array para salvar aos dados
dados = []
# pergunta ao usuário
eyes = input("🔹  Qual a Cor dos Seus Olhos ?")
_EYES = Eyes(eyes)
while _EYES == "NOT_STRING":
    print("\n")
    for i in str(ReturnsAlerts(0)):
        time.sleep(.01)
        print(f"{i}",end="",flush=True)
        time.sleep(.01)
    print("\n")
    for i in str(ReturnsAlerts(1)):
        time.sleep(.01)
        print(f"{i}",end="",flush=True)
        time.sleep(.01)
    print("\n")
    eyes = input("🔹  Qual a Cor dos seus Olhos ?")
    _EYES = Eyes(eyes)
hairs = input("🔹  Qual a Cor dos seus Cabelos ?")
_HAIRS = Hairs(hairs)
while _HAIRS == "NOT_STRING":
    print("\n")
    for i in str(ReturnsAlerts(0)):
        time.sleep(.01)
        print(f"{i}",end="",flush=True)
        time.sleep(.01)
    print("\n")
    for i in str(ReturnsAlerts(1)):
        time.sleep(.01)
        print(f"{i}",end="",flush=True)
        time.sleep(.01)
    print("\n")
    hairs = input("🔹  Qual a cor dos seus Cabelos ?")
    _HAIRS = Hairs(hairs)
heights = input("🔹  Qual é a sua Altura ?")
_HEIGHT = Heights(heights)
while _HEIGHT == "NOT_INT":
    print("\n")
    for i in str(ReturnsAlerts(0)):
        time.sleep(.01)
        print(f"{i}",end="",flush=True)
        time.sleep(.01)
    print("\n")
    for i in str(ReturnsAlerts(1)):
        time.sleep(.01)
        print(f"{i}",end="",flush=True)
        time.sleep(.01)
    print("\n")
    heights = input("🔹  Qual é a sua Altura ?")
    _HEIGHT = Heights(heights)
colors = input("🔹  Qual é a Cor de Sua Pele ?")
_COLORS = Colors(colors)
while _COLORS == "NOT_STRING":
    print("\n")
    for i in str(ReturnsAlerts(0)):
        time.sleep(.01)
        print(f"{i}",end="",flush=True)
        time.sleep(.01)
    print("\n")
    for i in str(ReturnsAlerts(1)):
        time.sleep(.01)
        print(f"{i}",end="",flush=True)
        time.sleep(.01)
    print("\n")
    colors = input("🔹  Qual a Cor de sua Pele ?")
    _COLORS = Colors(colors)
dados.append([_EYES,_HAIRS,_HEIGHT,_COLORS])
# resposta
# .predict_prob = "Prever Probabilidade"
response = Modelo.predict_proba(dados)
# print(response)
# print(f"VOCÊ PROVAVELMENTE É OU TEM RAÍZES DO PÁIS: {response.item()}")
print("\n")
for j in response:
    for i,probabilidade in enumerate(j):
        if probabilidade != 0:
            mostrar = f"📍  {Fore.WHITE}Existe uma Probabilidade de {Fore.GREEN}{int(probabilidade * 100)}% {Fore.WHITE}de Você ser/ter Descendência do País:{Fore.GREEN} {Fore.GREEN}{Y_[i]}{Fore.WHITE}"
            for j in mostrar:
                time.sleep(.01)
                print(f"{j}",end="",flush=True)
                time.sleep(.01)
            print("\n")
            if str(Y_[i]) == "PAÍSES NÓRDICOS":
                 for i in PN:
                    print("\t 🔹 ",end="")
                    for j in i:
                        time.sleep(.01)
                        print(f"{j}",end="",flush=True)
                        time.sleep(.01)
                    print("\n")
            
            elif str(Y_[i]) == "PAÍSES BÁLTICOS":
                for i in PB:
                    print("\t 🔹 ",end="")
                    for j in i:
                        time.sleep(.01)
                        print(f"{j}",end="",flush=True)
                        time.sleep(.01)
                    print("\n")
            
            elif str(Y_[i]) == "PAÍSES BAIXOS":
                 for i in Pb:
                    print("\t 🔹 ",end="")
                    for j in i:
                        time.sleep(.01)
                        print(f"{j}",end="",flush=True)
                        time.sleep(.01)
                    print("\n")
            
            elif str(Y_[i]) == "ÁFRICA SUBSAARIANA":
                 for i in AS:
                    print("\t 🔹 ",end="")
                    for j in i:
                        time.sleep(.01)
                        print(f"{j}",end="",flush=True)
                        time.sleep(.01)
                    print("\n")