# -*- coding: utf-8 -*-

class RootNR(object):


    def __init__(self, fx0):

        # margens de erro utilizadas nos testes
        #self.erro = 0.0001
        #self.erro = 0.0000001
        #self.erro = 0.00000000000001
        self.erro =  0.000000000000001
        #self.erro = 0.00000000000000000000000000001
        #self.erro = 0.00000000000000000000000000000000000000000000000000000001

        self.__fx = fx0 # atributo que recebe o objeto do tipo Function como argumento
        
    def findRoot(self):

        self.pontoA = float(input("informe o valor do ponto A para calcular a raiz da funcao: "))

        self.pontoB = float(input("informe o valor do ponto B para calcular a raiz da funcao: "))

        validar = self.__fx.function(self.pontoA) * self.__fx.function(self.pontoB) #se o resultado for maior que 0 existe pelo menos uma raiz na funcao

        index = 0  # contador de iteracoes

        self.raizF = 0.0  # variavel para armazenar o resultado do metodo de newton-raphson

        if validar < 0:

            self.xi = 0.0  # recebe o ponto mais apropriado para o calculo da raiz

            # selecionar qual ponto sera usado
            fa = abs(self.derivative(self.pontoA))
            fb = abs(self.derivative(self.pontoB))

            if fa > fb: # o maior valor retornado de f(x) e o valor mais apropriado para tomar como ponto de partida para o calculoa raiz
                self.xi  = self.pontoA
            else:
                self.xi = self.pontoB

            try:
                while True:

                    index = index + 1 # incrementando o contador

                    self.raizF = self.xi - (self.__fx.function(self.xi)/self.derivative(self.xi)) # calcular a raiz da funcao

                    precisao = abs(self.raizF - self.xi) # calcular a precisao da resposta

                    if precisao < self.erro: # testar se a precisao e menor que o erro definido
                        break # encerrar o laco pois a precisao ja e menor que o erro
                    else:
                        self.xi = self.raizF # trocar os valores das variaveis para calcular novamente a raiz

                print("Com a margem de erro: {0}, ocorreram {1} iteracoes para calcular a raiz da funcao.".format(
                    self.erro, index))

            except Exception as motivoErro:
                print(motivoErro.args)

        else:
            print("nao e possivel calcular a raiz da funcao com os pontos informados.")

        return self.raizF
              
    def derivative(self, x):

        dx = (self.__fx.function(x + self.erro) - self.__fx.function(x)) / self.erro # calcucar a derivada da funcao

        return dx
