dano_base = 100
nivel_player = 60
dano_bonus = 20
is_exposto = True
dano_exposto = 1.5

# dano baseado na exposição
if is_exposto:
    dano_total = (dano_base + dano_bonus) * dano_exposto
elif not is_exposto:
    dano_total = dano_base + dano_bonus
else:
    dano_total = dano_base

# Mensagem baseada no nível
if nivel_player >= 50:
    if is_exposto:
        print(f'Você deu {dano_total} de dano, o inimigo estava exposto. recebendo {dano_exposto}x.')
    else: # se nao estiver exposto
        print(f'Você deu {dano_total} de dano, o inimigo não estava exposto.')
else:
    print(f'Você deu {dano_base} de dano. Evolua até nível 50 para receber bônus de {dano_bonus}.')
