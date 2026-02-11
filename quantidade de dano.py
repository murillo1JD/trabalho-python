def calcular_dano(base, nivel, bonus_valor, exposto=False):
    MULTIPLICADOR_EXPOSTO = 1.5
    NIVEL_MIN_BONUS = 50

    bonus_aplicado = bonus_valor if nivel >= NIVEL_MIN_BONUS else 0
    multiplicador = MULTIPLICADOR_EXPOSTO if exposto else 1.0
    
    return (base + bonus_applied) * multiplicador

dano_base = 100
nivel_player = 60
dano_bonus = 20
inimigo_exposto = False

dano_final = calcular_dano(dano_base, nivel_player, dano_bonus, inimigo_exposto)

print(f"Você causou {dano_final:.1f} de dano.")

if nivel_player < 50:
    print(f"Dica: Alcance o nível 50 para desbloquear +{dano_bonus} de bônus!")
elif inimigo_exposto:
    print("O inimigo estava exposto! Dano crítico aplicado.")
else:
    print("O inimigo resistiu bem (não estava exposto).")