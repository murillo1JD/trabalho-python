salario = float(input('Digite o salário: '))
divida = float(input('Digite o valor da dívida: '))

sobra = salario - divida 
print(f"Saldo após pagar a dívida: R$ {sobra:.2f}")

porcentagem = float(input('Digite a porcentagem para aposentadoria (ex: 10): '))
valor_aposentadoria = sobra * (porcentagem / 100)
rentabilidade_mensal = valor_aposentadoria * 0.12  # 12% de rendimento

print(f"Valor reservado para aposentadoria: R$ {valor_aposentadoria:.2f}")
print(f"Estimativa de rendimento mensal (12%): R$ {rentabilidade_mensal:.2f}")

sobra_total = sobra - valor_aposentadoria
divisao_entre_parceiros = sobra_total / 2

print("-" * 30)
print(f"Salário líquido restante: R$ {sobra_total:.2f}")
print(f"Cada pessoa receberá: R$ {divisao_entre_parceiros:.2f}")