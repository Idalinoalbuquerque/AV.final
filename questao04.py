#Pede o número de telefone 
nu = int(input("Digite seu número de telefone : "))
#Salva os dois primeiros dígitos do número de telefone
nu = int(str(nu)[:2])
#Compara os dois primeiros dígitos do número de telefone 
if nu == 61:
    print("seu DDD é de Brasília")
elif nu == 71:
    print("seu DDD é de Salvador")
elif nu == 11:
    print("seu DDD é de São Paulo")
elif nu == 21:
    print("seu DDD é de Rio de Janeiro")
elif nu == 32:
    print("seu DDD é de Juiz de Fora")
elif nu == 19:
    print(" seu DDD é de Campinas")
elif nu == 27:
    print(" seu DDD é de Vitória")
elif nu == 31:
    print("seu DDD é de Belo Horizonte")
else:
    print("DDD não encontrado")