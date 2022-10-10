n1 = int(input('Nota 1: '))
n2 = int(input('Nota 2: '))
n3 = int(input('Nota 3: '))

media = ((n1+n2+n3)/3)

if media < 6:
    print("Aluno reprovado")
if media >= 6:
    print("Aluno aprovado")