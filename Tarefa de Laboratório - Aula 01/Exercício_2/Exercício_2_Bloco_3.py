# Multa: 2% do valor da fatura
valor = 999.90
multa = 20.00
juros = 0.33
valor_total = valor + multa + juros
valor_negociacao = valor_total * 0.1

print("Valor: R$", format(valor, '.2f'))
print("Multa: R$", format(multa, '.2f'))
print("Juros: R$", format(juros, '.2f'))
print("Valor Total: R$", format(valor_total, '.2f'))
print("Valor mínimo para negociação: R$", format(valor_negociacao, '.2f'))


