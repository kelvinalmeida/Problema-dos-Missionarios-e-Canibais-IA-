# Situação Inicia
# Posição 0 -> 3 missionários do lado esquerdo 
# Posição 1 -> 3 Canibais do lado esquerdo 
# Posição 2 -> 0 Canibais do lado esquerdo 
# Posição 3 -> 0 missionários do lado esquerdo 
# Posição 4 -> Lado da canoa 0 - Esquerdo - 1 - Direito

estadoInicial=[3,3,0,0,0]

# Operadores - Situações possíveis para atravessia do barco.
# (1,0) - atravessar um missionario no barco
# (2,0) - atravessar dois missionario no barco
# (1,1) - atravessar um canabis e um missionario no barco
# (0,2) - atravessar dois canibais no barco
# (1,0) - atravessar um  canibal no barco
operadores = [(1,0), (0,1), (1,1), (2,0), (0,2)]
# operadores = [(1,0), (1,1), (2,0), (0,2)]

borda = []
visitados = []


#  deslocarCanoa() Me retorna o próximo passo possíel de acordo com os operadores

def deslocarCanoa(estado, quantMissionarios = 0, quantCanibais = 0): 
    # Pequeno controle
    if quantMissionarios + quantCanibais > 2:
        return
    
    # Onde está a canoa? Se está a esquerda a viagem será para a direita e vice-versa;
    # 0 - esquerda
    # 1 - direita
    if estado[-1] == 0:
        missonariosOrigem = 0
        canabisOrigem = 1
        missionariosDestinos = 2
        canabisDestino = 3
    else:
        missonariosOrigem = 2
        canabisOrigem = 3
        missionariosDestinos = 0
        canabisDestino = 1

    # Se não há o que transportar
    if estado[missonariosOrigem] == 0 and estado[canabisOrigem] == 0:
        return
    
    # Atualizando a posição da canoa
    estado[-1] = 1 - estado[-1]

    # transportando os missionários.
    for i in range(min(quantMissionarios, estado[missonariosOrigem])):
        estado[missonariosOrigem] -= 1
        estado[missionariosDestinos] += 1
    
    for i in range(min(quantCanibais, estado[canabisOrigem])):
        estado[canabisOrigem] -= 1
        estado[canabisDestino] += 1

    return estado

# Retorna os proximos estados (se houver) 
def sucessores(estado):
    sucessores = []
    for (i,j) in operadores:
        est = deslocarCanoa(estado[:], i, j)
        if est == None: continue
        if ((est[0] < est[1] and est[0] > 0) or (est[2] < est[3] and est[2] > 0)): continue
        if est in visitados: continue
        sucessores.append(est)
    
    return sucessores


def obtemAdjacenteNaoVisitado(elementoAnalisar):
    estadosPossiveis = sucessores(elementoAnalisar)
    if len(estadosPossiveis) > 0:
        return estadosPossiveis[0]
    else:
        return -1
    

def testeMeta(estado):
    if estado[2] >= 3 and estado[3] >= 3:
        return True
    else:
        return False

# Buscando em Profundidade...

def dfs(estadoInicial):
    
    borda.append(estadoInicial)
    
    while len(borda) != 0:
        # print(borda)
        
        elementoAnalisar = borda[len(borda) - 1]
        
        # Encontrou a solução e termina o loop.
        if testeMeta(elementoAnalisar):break 
        
        estadoPossivel = obtemAdjacenteNaoVisitado(elementoAnalisar)

        if estadoPossivel == -1:
            borda.pop()
        else:
            visitados.append(estadoPossivel)
            borda.append(estadoPossivel)
    else:
        print("Caminho não encontrado!")

    return borda


# Executando a busca...
print(dfs(estadoInicial))
