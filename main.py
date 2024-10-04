# Função recebe o salário fixo e o valor em vendas 
# Retorna o valor da comissão e o pagamento total
def calcula_pagamento(salario, vendas):
  comissao = vendas * 0.15
  pagamento = salario + comissao
  return comissao, pagamento

# Obtém o nome do vendedor, salário fixo e o valor em vendas
nome = input("Entre com o nome do vendedor: ")
salario = float(input("Informe o salário: "))
vendas = float(input("Informe o valor em vendas: "))

# Chama a função calcula_pagamento para obter o valor da comissão e o pagamento total
comissao, pagamento = calcula_pagamento(salario, vendas)

# Escreve o resultado na tela
print("{0} obteve R$ {1:.2f} de comissao e vai receber R$ {2:.2f}".format(nome, comissao, pagamento))