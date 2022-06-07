import time

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
    print('''\nParabéns! Seus familires conseguiram pagar um bom cursinho e você conseguiu passar de primeira!''')

print('='*30)
print('   UNIVERSIDADE PÚBLICA')
print('='*30)

#Depois
cidade = str(input('Você mora na mesma cidade que sua universidade?'))
if cidade.capitalize().strip()[0] == 'S':
    print('Que bom! Só vai precisar da condução.')
    facilidade+=1
else:
    print('Ah, voçê terá de morar em outra cidade, muitas vezes sozinho e sem seus familiares e amigos...')
    dificuldade+=1
    moradia = str(input('Você tem lugar pra ficar?(casa de parentes, república)'))
    if moradia.capitalize().strip()[0] == 'S':
        casa = str(input('Essa moradia é uma república?'))
        if casa.capitalize().strip()[0] =='S':
            print('''\nParabéns, voçê entrou em uma república!
    Vantagens: Menor valor de aluguel e contas
    Desvantagens: Você divide a casa com mais 30 pessoas.''')
            time.sleep(2)
            print('='*30)
            print('   República Humilhação')
            print('='*30)
            print('''\nVocê já conseguiu arrumar seu canto na república e está ansioso para as aulas.
    Você se decepsiona um pouco com a maneira que seus colegues te tratam,
    eles te humilham constantemente e te forçam a carregar "placas" de papelão
    com ofensas durante a aula.''')
    else:
        print('''\nVocê terá de arrumar um lugar pra ficar...
Infelizmente, as vagas de moradia para alunes estão em falta.
    ''')
        dificuldade +=1
        if int(dificuldade) >= 3 or int(facilidade) == 0:
            print('Com muito esforço, seus familiares conseguem pagar um pequeno aluguel pra você.')
        else:
            print('Seus familiares conseguem pagar sua moradia.')