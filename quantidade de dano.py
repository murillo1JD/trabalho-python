dano_base = 100
nivel_player = 60
dano_bonus = 20

dano_total = dano_base + dano_bonus

if nivel_player >= 50:
   print(f'voce atualmente dá {dano_total} de dano, pois recebeu {dano_bonus} de bonus dmg ')
else:
    print(f'voce dá atualmente {dano_base} de dano, evolua ate o 50 ou mais para receber um bonus de {dano_bonus}.')
