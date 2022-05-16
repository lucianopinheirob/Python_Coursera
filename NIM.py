def computador_escolhe_jogada(n,m):
    peças_retiradas = 0
    while (n%(m+1)!=0):
        peças_retiradas = peças_retiradas + 1
        n = n-1
    return peças_retiradas

def usuario_escolhe_jogada(n,m):
    i = True
    while i:
        peças_retiradas = int(input("Quantas peças você vai tirar? "))
        if peças_retiradas <= m and peças_retiradas <= n and peças_retiradas >= 1:
            return peças_retiradas
        else:
            print("\nOops! Jogada inválida! Tente de novo.\n")
        
def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    peças_atual = n
    conta_jogadas = 0
    if n%(m+1) != 0:
        print("\nComputador começa!\n")
        while peças_atual != 0:
            if conta_jogadas % 2 == 0:
                peças_retiradas = computador_escolhe_jogada(peças_atual,m)
                peças_atual = peças_atual - peças_retiradas
                print("O computador tirou", peças_retiradas,"peças.")
                print("Agora restam",peças_atual,"peças no tabuleiro.\n")    
            else:
                peças_retiradas = usuario_escolhe_jogada(peças_atual,m)
                peças_atual = peças_atual - peças_retiradas
                print("\nVocê tirou", peças_retiradas,"peças.")
                print("Agora restam",peças_atual,"peças no tabuleiro.\n")     
            conta_jogadas = conta_jogadas + 1
        if(conta_jogadas % 2 != 0):
            print("Fim do jogo! O computador ganhou!")
        else:
            print("Fim do jogo! Você ganhou!")
    else:
        print("\nVocê começa!\n")
        while peças_atual != 0:
            if conta_jogadas % 2 != 0:
                peças_retiradas = computador_escolhe_jogada(peças_atual,m)
                peças_atual = peças_atual - peças_retiradas
                print("O computador tirou", peças_retiradas,"peças.")
                print("Agora restam",peças_atual,"peças no tabuleiro.\n")    
            else:
                peças_retiradas = usuario_escolhe_jogada(peças_atual,m)
                peças_atual = peças_atual - peças_retiradas
                print("\nVocê tirou", peças_retiradas,"peças.")
                print("Agora restam",peças_atual,"peças no tabuleiro.\n")     
            conta_jogadas = conta_jogadas + 1
        if(conta_jogadas % 2 == 0):
            print("Fim do jogo! O computador ganhou!")
        else:
            print("Fim do jogo! Você ganhou!")

def campeonato():
    print("Bem-vindo ao jogo do NIM! Escolha:\n")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato\n")

    escolha = int(input())

    if escolha == 1:
        print("Você escolheu uma partida isolada!\n")
        partida()
    elif escolha == 2:
        print("Você escolheu um campeonato!\n")
        rodada = 1
        while(rodada <= 3):
            print("**** Rodada",rodada,"****\n")
            partida()
            rodada = rodada + 1
        print("\n**** Final do campeonato! ****\n")
        print("Placar: Você 0 X 3 Computador")

campeonato()


















        
