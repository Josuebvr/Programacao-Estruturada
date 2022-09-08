# Data:
massa = float(input('Massa corporal: '))
idade = int(input('Idade: '))

if idade < 18 and idade > 15:
    documentos_de_autorizacao = str(
        input('Tem documento de autorização? (s/n): ')).upper()
else:
    documentos_de_autorizacao = False

sintomas = str(
    input('Teve febre ou sintomas gripais nos últimos 14 dias? (s/n): ')).upper()
viajou = str(input('Viajou ao exterior nos últimos 30 dias? (s/n): ')).upper()
teve_contato = str(
    input('Teve contato com caso suspeito ou confimado de Covid-19? (s/n): ')).upper()
primeira_doacao = str(input('É sua primeira doação? (s/n): ')).upper()

if primeira_doacao == 'N':
    quantidade_de_doacoes = int(
        input('Teve quantas doações nos últimos 12 meses?: '))
else:
    quantidade_de_doacoes = False
if quantidade_de_doacoes > 0:
    ultima_doacao = int(
        input('Faz quantos meses desde a sua última doação?: '))
else:
    ultima_doacao = False

sexo = str(input('Qual seu sexo biológico? (f/m): ')).upper()

if sexo == 'F':
    gravida = str(input('Está grávida ou amamentando? (s/n): ')).upper()
else:
    gravida = False


# Entrada:
print('\nMassa corporal: ', massa)
print('Idade: ', idade)

if idade < 18:
    print('Autorização do responsável: ', documentos_de_autorizacao)
else:
    documentos_de_autorizacao = False

print('Febre ou sintomas gripais: ', sintomas)
print('Viagem ao exterior: ', viajou)
print('Contato com caso de Covid-19: ', teve_contato)
print('Primeira doação: ', primeira_doacao)

if primeira_doacao == 'N':
    print('Doações nos últimos 12 meses: ', quantidade_de_doacoes)
else:
    qdoaquantidade_de_doacoescoes = False
if quantidade_de_doacoes > 0:
    print('Meses desde a última doação: ', ultima_doacao)
else:
    ultima_doacao = False

print('Sexo biológico: ', sexo)

if sexo == 'F':
    print('Grávida ou amamentando: ', gravida)
else:
    gravida = False

# Pode fazer agendamento
agendamento = True


# Impedimentos:
if massa < 50:
    print('Impedimento: Está abaixo da massa corporal mínima')
    agendamento = False

if idade < 16:
    print('Impedimento: É menor de 16 anos')
    agendamento = False

if documentos_de_autorizacao == 'N':
    print('Impedimento: É menor de 18 anos e não possui consentimento do responsável')
    agendamento = False

if idade > 60 and primeira_doacao == 'S':
    print('Impedimento: É maior de 60 anos e é sua primeira doação')
    agendamento = False

if idade > 69:
    print('Impedimento: É maior de 69 anos')
    agendamento = False

if sintomas == 'S':
    print('Impedimento: Tem febre ou sintomas gripais')
    agendamento = False

if viajou == 'S':
    print('Impedimento: Realizou uma viagem recente ao exterior')
    agendamento = False

if teve_contato == 'S':
    print('Impedimento: Teve contato com caso suspeito ou confimado de COVID-19')
    agendamento = False

if sexo == 'M':
    if quantidade_de_doacoes >= 4:
        print('Impedimento: Teve o número máximo de doações anuais atingido')
        agendamento = False
    if ultima_doacao < 2 and ultima_doacao != False:
        print('Impedimento: O intervalo mínimo entre as doações não foi respeitado')
        agendamento = False

if sexo == 'F':
    if quantidade_de_doacoes >= 3:
        print('Impedimento: Teve o número máximo de doações anuais atingido')
        agendamento = False
    if ultima_doacao < 3 and ultima_doacao != False:
        print('Impedimento: O intervalo mínimo entre as doações não foi respeitado')
        agendamento = False

if gravida == 'S':
    print('Impedimento: Está grávida ou amamentando')
    agendamento = False


# Agendamento
if agendamento == True:
    print('\nAgende um horário para triagem completa')
