print('''\nBem-vindo, amigo(a)!
Nesse programa, você irá digitar o \033[1mNOME, IDADE e SEXO de\033[m 4 pessoas diferentes.
No final irei mostrar:\033[36m
- Média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos.\033[m
\033[31mATENÇÃO: No "sexo", digite apenas: [HOMEM] ou [MULHER]\033[m''')

list_homem = []
list_nome_homem = []
count_idade = 0
count_mm = 0
for c in range(1, 5):
    nome = str(input(f"\nDigite o nome da {c}º pessoa: "))
    idade = int(input(f"Digite a idade da {c}º pessoa: "))
    sexo = str(input(f"Digite se é \033[4mHOMEM\033[m ou \033[4mMULHER\033[m: ")).strip().lower()
    count_idade += idade
    if sexo == "homem":
        list_homem.append(idade)
        if idade is max(list_homem):
            list_nome_homem.insert(0, nome)
    elif sexo == "mulher":
        if idade < 20:
            count_mm += 1
    elif sexo != "homem" or "mulher":
        print("\033[31mPor favor, reinicie o programa e digite [HOMEM] ou [MULHER]\033[m")

media_idade = count_idade/4  # Média de idade do grupo
# list_nome_homem[0] : Homem mais velho do grupo
# count_mm : Quantas mulheres têm menos de 20 anos

print(f"\nMédia de idade do grupo: \033[1m{int(media_idade)}\033[m!")
if len(list_nome_homem) >= 1:
    print(f"Homem mais velho do grupo: \033[1m{list_nome_homem[0].title()}\033[m!")
else:
    print(f"Não tem homens no grupo!")
if count_mm >= 1:
    print(f"Mulheres com menos de 20 anos: \033[1m{count_mm}\033[m!")
else:
    print(f"Nenhuma mulher com menos de 20 anos!")
