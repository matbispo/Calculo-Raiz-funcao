# -*- coding: utf-8 -*-

from math import log10

class RootBiss(object):


    def __init__(self, fx0):

        self.__fx = fx0 # atributo privado que recebe o objeto do tipo Function como argumetno

        #margens de erro utilizados nos testes
        #self.erro = 0.0001
        self.erro = 0.0000001
        #self.erro = 0.00000000000001
        #self.erro = 0.00000000000000000000000000001
        #self.erro = 0.00000000000000000000000000000000000000000000000000000001  # menor numero possivel do tipo float

    def findRoot(self):

        self.pontoA = float(input("informe o valor do ponto A para calcular a raiz da funcao: "))

        self.pontoB = float(input("informe o valor do ponto B para calcular a raiz da funcao: "))

        self.x0 = 0.0 # variavel para armazenar o resultado do metodo de bisseccao
        validar = self.__fx.function(self.pontoA) * self.__fx.function(self.pontoB) #se o resultado for menor que 0 existe pelo menos uma raiz na funcao

        index = 0  # contador de iteracoes

        if validar < 0:

            try:
                while True:
                    index = index + 1

                    self.x0 = (self.pontoA + self.pontoB) /2.0 # calculando a media entre o ponto A e B

                    sinal = self.__fx.function(self.pontoA) * self.__fx.function(self.x0) # calculo feito para identificar qual ponto recebera o novo valor para continuar o metodo dependendo do sinal do valor
                    fx0 = self.__fx.function(self.x0) #calcular o valor da função no ponto x0

                    if fx0 ==0: # se f(x0) == 0, x0 e a raiz
                        print("fx0 = 0")
                        break
                    elif sinal < 0: # trocar o lado do calculo da raiz
                        self.pontoB = self.x0 # o ponto B recebeo valor de x0 calculado para dar continuidade
                    else:
                        self.pontoA = self.x0 # o ponto A recebeo valor de x0 calculado para dar continuidade

                    precisao = abs((self.pontoB - self.pontoA)) # calcula a predisao do resultado do metodo
                    if precisao < self.erro: # quando a precisao calculada for menor que o erro estipulado o metodo foi concluido
                        break

                print("Com a margem de erro: {0}, ocorreram {1} iteracoes para calcular a raiz da funcao.".format(
                    self.erro, index))

            except Exception as motivoErro:
                print(motivoErro.args)

        else:
            print("nao e possivel calcular a raiz da funcao com os pontos informados.")



        return self.x0
        
    def calcularInteracoes(self, a, b, erro): # funcao para calcular a quantidade de iteracoes necessarias para executar o metodo da bisseccao # nao fui utilizado

        k = (log10(b -a) - log10(erro)) / log10(2.)
        #arredondar para cima
        return k
            