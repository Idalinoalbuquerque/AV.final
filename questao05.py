
num = []
p=0
#cria um loop para ler 5 numeros
for i in range(0,5):
#Pede que o usuário coloque um número
    numero = int(input(f'Digite o {i+1}° número: '))
#Se o número for par adicionar 1 a variável "p"
    if numero % 2 == 0:
        p = p+1
#disponibiliza o numero de numeros  que possui na lista
print(f"{p} são pares")