print('=' *30)
print('\n   Simulador De Universidade\n')
print('=' *30)
print('''Imagine que você é um jovem
e quer entrar em uma universidade pública.
A cada opção menos favorável sua dificldade aumenta e a cada
opção mais favorável, sua facilidade aumenta.
\nBoa sorte!''')

dificuldade = 0
facilidade = 0

cor = str(input('Você é branco?'))
if cor.capitalize().strip()[0] == 'S':
    print('Parabéns! Ficou um pouco mais fácil pra você...')
    facilidade += 1
else:
    print('Sinto muito, ficou um pouco mais díficil pra você...')
    dificuldade += 1

renda = str(input('Sua renda per capita familiar é mais que um salário mínimo?'))
if renda.capitalize().strip()[0] == 'S':
    print('Legal, mais um avanço!')
    facilidade += 1
else:
    print('Sinto muito, mas temos mais chances, não se preocupe!')
    dificuldade += 1

if  int(dificuldade) >= 2:
    print('''Parabéns!! Depois de muito esforço e ajuda dos seu familiares e 
professores do cursinho municipal, você finalmente passou na Universidade,
depois de dois anos!''')
elif int(dificuldade) == 1:
    print('''Parabéns! Depois de muito esforço, você conseguiu passar
na Universidade!''')
else:
    print('''Parabéns! Seus familires conseguiram pagar um bom cursinho e você conseguiu passar de primeira!''')