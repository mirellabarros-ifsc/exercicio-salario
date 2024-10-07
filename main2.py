#coding: utf-8

def ComissaoSalario():  
    Nome = input("Entre com o nome do vendedor: ")
    SalarioFixo = float(input("Informe o salário: "))
    Vendas = float(input("Informe o total de vendas: "))
    Comissao = 0.15*Vendas 
    PagamentoEsperado=SalarioFixo+Comissao
    return Nome, Comissao, PagamentoEsperado



if __name__=="__main__": 
    Nome, Comissao, PagamentoEsperado= ComissaoSalario()
    strg = "{0} obteve R$ {1:.2f} de comissão e vai receber {2:.2f}".format(Nome,Comissao, PagamentoEsperado)
    print(strg) 