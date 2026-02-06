dano_base = 100
nivel_player = 60
dano_bonus = 20
is_exposto = False
multiplicador_exposto = 1.5

bonus_aplicado = dano_bonus if nivel_player >= 50 else 0

multiplicador = multiplicador_exposto if is_exposto else 1.0

dano_total = (dano_base + bonus_aplicado) * multiplicador

print(f"Você deu {dano_total} de dano.")

if nivel_player < 50:
    print(f"Evolua até nível 50 para receber bônus de {dano_bonus}.")
elif is_exposto:
    print(f"O inimigo estava exposto, recebendo {multiplicador_exposto}x de dano!")
else:
    print("O inimigo não estava exposto.")