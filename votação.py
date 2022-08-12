import os

Votos_Candidato_X = 0
Votos_Candidato_Y = 0
Votos_Candidato_Z = 0
Votos_Branco = 0
while True:
    print('*'*30)
    print('Total Candidato X:{}''\nTotal Candidato Y:{}''\nTotal Candidato Z:{}''\nVotos Nulos ou Brancos:{}'.format(Votos_Candidato_X, Votos_Candidato_Y, Votos_Candidato_Z, Votos_Branco))
    print('*'*30)

    try:
        voto = int(input('Para quem você gostaria de votar?''\n889 - Candidato X''\n847 - Candidato Y''\n515 - Candidato Z''\nSeu voto: '))
        if voto == 889:
            Votos_Candidato_X += 1
        elif voto == 847:
            Votos_Candidato_Y += 1
        elif voto == 515:
            Votos_Candidato_Z += 1
        else:
            Votos_Branco += 1
    except:
        print('Digite apenas números, vote novamente!')
    os.system('cls')
