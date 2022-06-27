import json


# 2 - Fibonacci
def fib(num):

    if num in [0, 1]:
        return num

    return fib(num - 1) + fib(num - 2)


# 3 - Arquivo dados.json
def faturamento():
    file = open('dados.json')

    menorV, maiorV, totalV, diaMaiorM = 9990, 0, 0, 0;

    dados = json.load(file)

    file.close()

    dados = [i for i in dados if i['valor'] != 0]

    numDias = len(dados)

    for i in dados:
        if i['valor'] <= menorV:
            menorV = i['valor']

        if maiorV < i['valor']:
            maiorV = i['valor']

        totalV += i['valor']

    totalV /= numDias

    for i in dados:
        if i['valor'] > totalV:
            diaMaiorM += 1

    return menorV, maiorV, diaMaiorM


# 4 - Percentual de representação
def percentual():
    dados = [{'ST': 'SP', 'valor': 67836.43}, {'ST': 'RJ', 'valor': 36678.66}, {'ST': 'MG', 'valor': 29229.88}, {'ST': 'ES', 'valor': 27165.48}, {'ST': 'OUTROS', 'valor': 19849.53}]

    valorT = 0

    for i in dados:
        valorT += i['valor']

    for i in dados:
        i.update({'porcentagem' : round(i['valor'] / valorT * 100, 2)})

    return dados


# 5 - inverter
def inverter(string):
    return string[::-1]


#for n in range(5):
 #   print(fib(n))

#faturamento()

#percentual()

