#primeiro passo é pedir valores de compra e de pagamento
preco = float(input('Digite o valor da compra (R$): '))
din = float(input('Digite a quantia de dinheiro entregue(R$): '))
print('')

#uma condicional para ver se o valor pago é suficiente ou se há troco;
#se tiver troco, apresentar o valor
if din == preco:
  print('Valor pago igual ao valor do preço. Não há troco.')
elif din < preco:
  falta = float(preco - din)
  print(f'Valor insuficiente. Faltam R$ {falta}.')
else:
  troco = float(din-preco)
  print(f'O valor do troco será de R$ {troco:.2f}.')

#agora a parte da especificação do troco; usando várias condicionais e um loop
ced = 100
totced = 0
while True:
  if troco >= ced:
    troco -= ced
    totced +=1
  else:
    if totced > 0:
       print(f'Total de {totced} cédulas de R$ {ced}.')
    if ced == 100:
       ced = 50
    elif ced == 50:
       ced = 20
    elif ced == 20:
       ced = 10
    elif ced == 10:
       ced = 5
    elif ced == 5:
       ced = 2
    elif ced == 2:
       ced = 1 
    totced = 0
    if troco < 1:
        break

#aqui separei a parte dos centavos do troco e fiz o mesmo procedimento das cédulas
resto_troco = float(troco - int(troco))
moeda = 1
totmoe = 0
while True:
  if resto_troco >= moeda:
    resto_troco -= moeda
    totmoe +=1
  else:
    if totmoe > 0:
       print(f'Total de {totmoe} moedas de R$ {moeda} centavos.')
    if moeda == 1:
       moeda = 0.50
    elif moeda == 0.50:
       moeda = 0.25
    elif moeda == 0.25:
       moeda = 0.10
    elif moeda == 0.10:
       moeda = 0.05
    elif moeda == 0.05:
       moeda = 0.01
    totmoe = 0
    if resto_troco == 0:
        break



