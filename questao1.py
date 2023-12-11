
#Pedir o salário
s = float(input("Digite seu salário: "))
#Verificar se o valor está entre 0R$ e 2000R$ .
if s <= 2000:
    print('Insento')#resultado do imposto
#Verificar se o valor está entre 2000R$ e 3000R$.
elif s > 2000 and s < 3000.01: 
    print(f"voçê  deve paga um imposto de  R$ {s*(8/100):.2f}")#resultado do imposto
#Verificar se o valor está entre 3000R$ e 4500R$.
elif s > 3000 and s < 4500.01:
    print(f"voçê  deve paga um imposto de  R$ {s*(18/100):.2f}")#resultado do imposto
#Verificar se o valor é maior que 4500R$.
else:
    print(f"voçê  deve paga um imposto de   R$ {s*(28/100):.2f}")#resultado do imposto