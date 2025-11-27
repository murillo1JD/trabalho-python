dano_base = 150
houve_critico = True
bonus_critico = 50
tipo_defesa_inimigo = 'Fortificada'
dano_temporario = dano_base

if houve_critico:
    dano_base += bonus_critico
else:
    dano_base
    
dano_temporario = dano_base

if tipo_defesa_inimigo == 'Fortificada':
   dano_temporario = dano_temporario * 0.85
else:
   dano_temporario = dano_base

if tipo_defesa_inimigo == 'Fortificada':
    print(f'voce causou {dano_temporario}')
    print(f'o inimigo estava usando defesa {tipo_defesa_inimigo}, diminuindo seu dano em 15%')
    
elif tipo_defesa_inimigo == 'Santa':
    print(f'voce nao causou nenhum dano. o inimigo usou a defesa {tipo_defesa_inimigo}')

elif tipo_defesa_inimigo == 'Nenhuma':
    print(f'voce causou {dano_temporario} de dano.')
    print(f'o inimigo estava usando defesa {tipo_defesa_inimigo}')
    
