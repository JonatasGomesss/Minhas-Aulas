# 1) soma(a, b):  Retorna a soma de dois n ́umeros inteiros.
def soma(a, b):
    return a + b
resultado = soma(3, 5)
print(resultado)  

#Teste de soma de números positivos:
#Neste teste, você pode verificar se a função retorna corretamente a soma de dois números positivos. 
#assert soma(3, 5) == 8
#Teste de soma de números negativos:
#Este teste verifica se a função lida corretamente com números negativos.
#assert soma(-3, -5) == -8
#Teste de soma de um número positivo e um número negativo:
#Este teste garante que a função seja capaz de lidar com a soma de um número positivo e um número negativo.
#assert soma(3, -5) == -2


# 2) subtracao(a, b):  Retorna a diferen ̧ca entre dois n ́umeros inteiros.

def subtracao(a, b):
    return a - b
resultado = subtracao(5, 3)
print(resultado) 
#Teste de subtração de números positivos:
#Neste teste, você pode verificar se a função retorna corretamente a diferença de dois números positivos.
#assert subtracao(5, 3) == 2
#Teste de subtração de números negativos:
#Este teste verifica se a função lida corretamente com números negativos.
#assert subtracao(-5, -3) == -2
#Teste de subtração de um número positivo e um número negativo:
#Este teste garante que a função seja capaz de lidar com a subtração de um número positivo e um número negativo.
#assert subtracao(5, -3) == 8

# 3) multiplicacao(a, b):  Retorna o produto de dois n ́umeros inteiros.

def multiplicacao(a, b):
    return a * b

resultado = multiplicacao(5, 3)
print(resultado) 

#Teste de multiplicação de números positivos:
#Verifica se a função retorna corretamente o produto de dois números positivos.
#assert multiplicacao(5, 3) == 15
#Teste de multiplicação de números positivo e negativo:
#Verifica se a função lida corretamente com a multiplicação de um número positivo por um número negativo.
#assert multiplicacao(-5, 3) == -15
#Teste de multiplicação de números negativos:
#Verifica se a função retorna corretamente o produto de dois números negativos.
#assert multiplicacao(-5, -3) == 15

#4) divisao(a, b):  Retorna o resultado da divis ̃ao de dois n ́umeros inteiros(arredondado para 2 casas decimais).

def divisao(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return round(a / b, 2)

resultado = divisao(5, 3)
print(resultado)

#Teste de divisão de números inteiros positivos:
#Verifica se a função retorna corretamente o resultado da divisão de dois números inteiros positivos.
#assert divisao(5, 3) == 1.67
#Teste de divisão de um número positivo por um número negativo:
#Verifica se a função lida corretamente com a divisão de um número positivo por um número negativo.
#assert divisao(10, -2) == -5.0
#Teste de divisão de um número negativo por um número positivo:
#Verifica se a função retorna corretamente o resultado da divisão de um número negativo por um número positivo.
#assert divisao(-8, 4) == -2.0

# 5) media(lista):  Retorna a m ́edia dos valores em uma lista de n ́umeros.

def media(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)

valores = [10, 15, 20, 25]
resultado = media(valores)
print(resultado) 

#Teste com uma lista de números inteiros:
#Verifica se a função retorna corretamente a média de uma lista de números inteiros.
#assert media([10, 20, 30, 40]) == 25.0
#Teste com uma lista de números decimais:
#Verifica se a função retorna corretamente a média de uma lista de números decimais.
#assert media([2.5, 3.5, 4.5, 5.5]) == 4.0
#Teste com uma lista vazia:
#Verifica se a função retorna zero quando a lista está vazia.
#assert media([]) == 0

#6) maiorvalor(lista):  Retorna o maior valor em uma lista de n ́umeros.

def maior_valor(lista):
    if len(lista) == 0:
        return None
    return max(lista)


valores = [10, 15, 20, 25]
resultado = maior_valor(valores)
print(resultado)  

#Teste com uma lista de números inteiros positivos:
#Verifica se a função retorna corretamente o maior valor em uma lista de números inteiros positivos.
#assert maior_valor([10, 20, 30, 40]) == 40
#Teste com uma lista de números inteiros negativos:
#Verifica se a função retorna corretamente o maior valor em uma lista de números inteiros negativos.
#assert maior_valor([-10, -20, -30, -5]) == -5
#Teste com uma lista mista de números inteiros positivos e negativos:
#Verifica se a função retorna corretamente o maior valor em uma lista mista de números inteiros positivos e negativos.
#assert maior_valor([-10, 20, -30, 40]) == 40

#7) menorvalor(lista):  Retorna o menor valor em uma lista de n ́umeros.
def menor_valor(lista):
    if len(lista) == 0:
        return None
    return min(lista)

valores = [10, 15, 20, 25]
resultado = menor_valor(valores)
print(resultado)  

#Teste com uma lista de números inteiros positivos:
#Verifica se a função retorna corretamente o menor valor em uma lista de números inteiros positivos.
#assert menor_valor([10, 20, 30, 40]) == 10
#Teste com uma lista de números inteiros negativos:
#Verifica se a função retorna corretamente o menor valor em uma lista de números inteiros negativos.
#assert menor_valor([-10, -20, -30, -5]) == -30

#8) numeroprimo(numero): RetornaTruese o n ́umero for primo,Falsecasocontr ́ario.
def numero_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


resultado = numero_primo(17)
print(resultado)  

#Teste com um número primo:
#Verifica se a função retorna corretamente True para um número que é primo.
#assert numero_primo(17) == True
#Teste com um número não primo:
#Verifica se a função retorna corretamente False para um número que não é primo.
#assert numero_primo(16) == False

#9.fibonacci(n):  Retorna os primeirosnn ́umeros na s ́erie de Fibonacci.
def fibonacci_recursive(n, fib_sequence=[0, 1]):
    if n <= len(fib_sequence):
        return fib_sequence[:n]
    fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fibonacci_recursive(n, fib_sequence)

n = 10
#Teste para Entrada Negativa:
#Este teste verifica o comportamento das funções quando uma entrada negativa é fornecida. Na série de Fibonacci, não há números negativos, então as funções devem lidar com isso adequadamente.
#def test_negative_input(self):
    #self.assertEqual(fibonacci(-1), [])
    #self.assertEqual(fibonacci_recursive(-5), [])

#Teste para Entrada Zero:
#Este teste verifica o comportamento das funções quando zero é fornecido como entrada. Como a série de Fibonacci começa com 0 e 1, isso é importante verificar.
#def test_zero_input(self):
 #   self.assertEqual(fibonacci(0), [])
 #  self.assertEqual(fibonacci_recursive(0), [])

#parouimpar(numero):  Retorna ”Par” se o n ́umero for par e ” ́Impar” sefor  ́ımpar.
def parOuImpar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

print(parOuImpar(10))  
print(parOuImpar(7))   
#Teste para Entrada de Número Inteiro Negativo:
#Este teste verifica o comportamento da função quando um número inteiro negativo é fornecido como entrada.

def verificarNumero(numero):
    if numero > 0:
        return "Positivo"
    elif numero < 0:
        return "Negativo"
    else:
        return "Zero"

# Testes
def test_verificarNumero(self):
    self.assertEqual(verificarNumero(5), "Positivo")
    self.assertEqual(verificarNumero(-3), "Negativo")
    self.assertEqual(verificarNumero(0), "Zero")

#Calcular fatorial de um número
#Essa função, chamada fatorial(numero), retorna o fatorial de um número inteiro não negativo.
def fatorial(numero):
    if numero < 0:
        return None
    elif numero == 0:
        return 1
    else:
        result = 1
        for i in range(1, numero + 1):
            result *= i
        return result

# Testes
def test_fatorial(self):
    self.assertEqual(fatorial(0), 1)
    self.assertEqual(fatorial(1), 1)
    self.assertEqual(fatorial(5), 120)
    self.assertIsNone(fatorial(-3))



