
#armazena a senha
s = 2000
t = int(input("Digite a senha: "))
#verifica a senha que o usuario colocou esta correta
while t != s:
    print("Senha incoreta")
    t= int(input("digite senha: "))
#se a senha digitada pelo usuario for correta  o programa vai digita "acesso permitido"
print("Acesso permitido")
