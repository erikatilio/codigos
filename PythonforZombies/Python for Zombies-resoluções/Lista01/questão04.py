#Faça um programa que calcule o aumente de um salário.Ele deve solicitar o valor do salário e a porcentagem de aumento.Exiba o valor de aumento e o novo salário

salary = float(input("digite o  valor do seu salário: "))
percentage = int(input("Digite a porcentagem do aumento: "))
calc_percentage = (percentage*salary/100)
received = salary + calc_percentage

print("Seu aumento será de","%", calc_percentage)
print("O valor total recebido será de: ","R$", received)
