datas = []
valores = []
variac = []

with open('dados_financeiros.txt', 'r') as dadosfinanc:
  for data in dadosfinanc.readlines()[1:]:
    dados = data.split(',')
    datas.append(dados[0])
    valores.append(int(dados[1]))
   

i = 1
variacao = 0
while i < (len(datas)):
  var = valores[i] - valores[i-1]
  variacao += var
  variac.append(var)
  i+=1


maiorvar = max(variac)
maiorvar_index = variac.index(maiorvar)

menorvar = min(variac)
menorvar_index = variac.index(menorvar)


with open('relatorio.txt', 'w') as relatorio:
  relatorio.write('Análise Financeira\n')
  relatorio.write(('-'*28) + '\n')
  relatorio.writelines(f'Total de meses: {len(datas)}\n')
  relatorio.writelines(f'Total: $ {sum(valores)}\n')
  relatorio.writelines(f'Média: $ {sum(valores)/len(datas):.2f}\n')
  relatorio.writelines(f'Variação da média: ${(variacao/(len(datas) - 1)):.2f}\n')
  relatorio.writelines(f'Maior aumento nos lucros: {datas[(maiorvar_index) + 1]} ($ {max(variac)})\n')
  relatorio.writelines(f'Maior reducao nos lucros: {datas[(menorvar_index) + 1]} ($ {min(variac)})\n')