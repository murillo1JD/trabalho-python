import random
import os

os.system('clear') # Limpar terminal


dano_base = 150
houve_critico = random.random() < 0.3
bonus_critico = 50
defesas = ["Fortificada", "Santa", "Nenhuma", "Reflexiva"]
tipo_defesa_inimigo = random.choice(defesas)

# critico
dano_total = dano_base + (bonus_critico if houve_critico else 0)

# Multiplicador dano
multiplicadores = {
    "Fortificada": 0.85,
    "Santa": 0.0,
    "Reflexiva": 0.45,
    "Nenhuma": 1.0
}

dano_final = dano_total * multiplicadores[tipo_defesa_inimigo]

# saida
status_critico = "SIM! 💥" if houve_critico else "Não."
resumo = (
    f"\n{'='*30}\n"
    f"⚔️ RELATÓRIO DE COMBATE\n"
    f"{'='*30}\n"
    f"Inimigo usou: {tipo_defesa_inimigo}\n"
    f"Ataque Crítico? {status_critico}\n"
    f"Dano causado: {dano_final:.2f}\n"
)

# defesas
if tipo_defesa_inimigo == "Santa":
    resumo += "🚫 O dano foi totalmente bloqueado!"
elif tipo_defesa_inimigo == "Reflexiva":
    resumo += f"⚠️ Você recebeu {dano_final:.2f} de dano de volta!"
elif tipo_defesa_inimigo == "Fortificada":
    resumo += "🛡️ Dano reduzido em 15%."

print(resumo)
print('='*30)