#Programa para calcular nota UEA

np1 = float(input("Victor,digite sua nota tirada na NP1:"))
np2 = float(input("Victor,digite sua nota tirada na NP2:"))
media = (np1+np2)/2
print("sua media nesse periodo foi:",media)

if media >= 8:
    print("Parabéns victor,você foi aprovado,agora é so correr para o abraço,e comemorar com os amigos")

if media <8:
    print("infelizmente não foi dessa vez victor,estude mais e recupere sua nota.")

