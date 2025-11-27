def calcular_dano(dano_base, houve_critico, bonus_critico, tipo_defesa_inimigo):
    if houve_critico:
        dano_base += bonus_critico
    
    dano_temporario = dano_base
    
    if tipo_defesa_inimigo == 'Fortificada':
        dano_temporario *= 0.85
        print(f'Você causou {dano_temporario}')
        print(f'O inimigo estava usando defesa {tipo_defesa_inimigo}, diminuindo seu dano em 15%')
    elif tipo_defesa_inimigo == 'Santa':
        print(f'Você não causou nenhum dano. O inimigo usou a defesa {tipo_defesa_inimigo}')
    elif tipo_defesa_inimigo == 'Nenhuma':
        print(f'Você causou {dano_temporario} de dano.')
        print(f'O inimigo estava usando defesa {tipo_defesa_inimigo}')
    else:
        print(f'Você causou {dano_temporario} de dano.')
        print(f'O inimigo estava usando defesa desconhecida: {tipo_defesa_inimigo}')

# Exemplo de uso
calcular_dano(150, True, 50, 'Fortificada')
