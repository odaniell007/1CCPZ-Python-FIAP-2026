from operator import truediv

idade = 20

maior_idade = idade >= 18
print(maior_idade, type(maior_idade))





print()

verifica_email = True
verifica_senha = True

login = verifica_email and verifica_senha
print(login)

if not login:
    print("OU... Seja mais inteligente, loga aí")



nota_final = 10

if nota_final < 4:
    print("Reprovado")

elif nota_final < 6:
    print("Recuperação")

else:
    print("Aprovado")

print("FIM")


