#Slicite o preço da mercadoria e o percentual de desconto.Exiba o valor de desconto e o preço a pagar

price = int(input("Digite o preço da mercadoria: "))
discount = float(input("Digite o percentual de desconto: "))
discount2 = (discount * price)/(100) 
price_discount = price - discount2
print("Valor de desconto: ","R$",discount2)
print("preço a pagar: ","R$",price_discount)

