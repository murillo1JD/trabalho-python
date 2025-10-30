# divida
salario = int(input('digite o salario: '))
divida = int(input('digite a divida: '))
sobra = salario - divida 
print(f"o resultado e: {sobra}")

# aposentadoria
porcentagem = float(input('digite a porcentagem da aposentadoria: '))
aposentadoria = sobra * porcentagem / 100
print(f"o valor da aposentadoria e: {aposentadoria}")
rentaMensal = aposentadoria * 0.12
print(f"A rentabilidade mensal (12%) é: {rentaMensal}")

# sobra total
sobraTotal = sobra - aposentadoria
print(f'o salario restante, retirando a aposentadoria e a divida, e: {sobraTotal}')

# divisão entre eles
divisao = sobraTotal / 2
print(f'a divisao entre voces resultara em: {divisao}')
