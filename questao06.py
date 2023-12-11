m =0 
q = 0
# repete  a  ação 6 vezes
for i in range(6):
    #solicita o usuario numero para ser armazenado
    n = float(input(f'Digite o {i+1}° número: '))
    # nesta parte o programa pegarar a m e somarar ao n
    if n > 0:
     m = m + n
     #Se o num for maior que 0 adicionar 1 na variável positivo
     q = q + 1

#Mostra a q de valores positivos
print(f"{q} valores positivos")
#Mostra a média da lista "numeros"com o PRINT
print(f"{m/q :0.1f}")