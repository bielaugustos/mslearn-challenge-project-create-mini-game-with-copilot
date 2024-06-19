

import random


opcoes = ['rock', 'paper', 'scissors']
pontuacao = 0

while True:
    escolha_jogador = input('Escolha rock, paper ou scissors: ').lower()
    if escolha_jogador not in opcoes:
        print('Opção inválida. Tente novamente.')
        continue

    escolha_computador = random.choice(opcoes)

    if escolha_jogador == escolha_computador:
        print(f'Empate! Ambos escolheram {escolha_jogador}.')
    elif (escolha_jogador == 'rock' and escolha_computador == 'scissors') or \
         (escolha_jogador == 'paper' and escolha_computador == 'rock') or \
         (escolha_jogador == 'scissors' and escolha_computador == 'paper'):
        print(f'Você venceu! {escolha_jogador} vence {escolha_computador}.')
        pontuacao += 1
    else:
        print(f'Você perdeu! {escolha_computador} vence {escolha_jogador}.')

    jogar_novamente = input('Você quer jogar novamente? (s/n): ').lower()
    if jogar_novamente != 's':
        break

print(f'Sua pontuação final é {pontuacao}.')