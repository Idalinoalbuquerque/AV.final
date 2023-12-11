#peça ao usuario o salario dele
l = float(input("digite o seu salario "))

#se o salario for menor que 400 ele recebera um aumento de 15%
if l <= 400 :
    print("em porcentage seu salario aumentou 15%")
    r=l*15/100  #formula para calcular o reajuste
    s1=l+r # formula para calcular o salario com o reajuste
    print(f"seu reajuste é de { r }")
    print(f"seu salario atual é de {s1}")
#se o salario for menor que 400 ele recebera um aumento de 12%
elif l <=800.00:
    print("em porcentage seu salario aumentou 12%")
    r1=l*12/100#formula para calcular o reajuste
    s2=l+r1 # formula para calcular o salario com o reajuste
    print(f"seu reajuste é de: {r1}")
    print(f"seu salario atual é de {s2}")
#se o salario for maior que 400 é menor que 800 ele recebera um aumento de 10%
elif l <=1200.00 :
    print("em porcentage seu salario aumentou 10%")
    r2 =l*10/100 #formula para calcular o reajuste
    s3=l+r2 # formula para calcular o salario com o reajuste
    print(f"seu reajuste é de: {r2}")
    print(f"seu salario atual é de {s3}")
#se o salario for menor que 2000 é maior que 1200 ele recebera um aumento de 7%
elif l <=2000.00 :
    print("em porcentage seu salario aumentou 7%")
    r3=l*7/100 #formula para calcular o reajuste
    s4=l+r3 # formula para calcular o salario com o reajuste
    print(f"seu reajuste é de: {r3}")
    print(f"seu salario atual é de {s4}")
#se o salario for maior que 2000 ele recebera um aumento de 4%
else:
    r4=l*4/100 #formula para calcular o reajuste
    s5=l+r4 # formula para calcular o salario com o reajuste
    print(f"seu reajuste é de: {r4}")
    print(f"seu salario atual é de {s5} ")
    print("em porcentage seu salario aumentou 4%")
