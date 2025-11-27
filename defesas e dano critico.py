import random
dano_base = 150
houve_critico = random.random() < 0.3
bonus_critico = 50
defesa = 0.85
defesa_santa = 0
defesa_reflexiva = 0.45
defesas = ["Fortificada", "Santa", "Nenhuma", "Reflexiva"]
tipo_defesa_inimigo = random.choice(defesas)
dano_temporario = dano_base

print(f"O inimigo escolheu a defesa: {tipo_defesa_inimigo}")

print(f'houve_critico? {houve_critico}')
if houve_critico:
    dano_base += bonus_critico
else:
    dano_base

if tipo_defesa_inimigo == 'Fortificada':
   dano_temporario = dano_temporario * defesa
elif tipo_defesa_inimigo == 'Santa':
    dano_temporario = dano_temporario * defesa_santa
elif tipo_defesa_inimigo == 'Reflexiva':
    dano_temporario = dano_temporario * defesa_reflexiva
else:
   dano_temporario = dano_base

if dano_temporario == defesa_santa:
    defesa_santa = 'voce nao causou nenhum dano.'
    
if tipo_defesa_inimigo == 'Fortificada':
    print(f'voce causou {dano_temporario}')
    print(f'o inimigo estava usando defesa {tipo_defesa_inimigo}, diminuindo seu dano em 15%') 
elif tipo_defesa_inimigo == 'Santa':
    print(f'voce causou {defesa_santa} o inimigo usou a defesa {tipo_defesa_inimigo}')
elif tipo_defesa_inimigo == 'Nenhuma':
    print(f'voce causou {dano_temporario} de dano.')
    print(f'o inimigo estava usando defesa {tipo_defesa_inimigo}')
elif tipo_defesa_inimigo == 'Reflexiva':
    print(f'voce causou {dano_temporario} de dano.')
    print(f'O inimigo usou {tipo_defesa_inimigo} e você recebeu {dano_temporario} de volta.')
