salario_por_hora = float(input("Quanto você ganha por hora? R$: "))
horas_trabalhadas = float(input("Quantas horas você trabalhou no mês? "))

salario_mensal = salario_por_hora * horas_trabalhadas

print(f"O total do seu salário no mês é: R$ {salario_mensal:.2f}")
