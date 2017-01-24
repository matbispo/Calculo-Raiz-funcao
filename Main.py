# -*- coding: utf-8 -*-

'''
Created on 01/11/2016

@author: mateus bispo
e-mail: math.l.bispo@gmail.com
'''

from Function import *
from RootBiss import RootBiss
from RootNR import RootNR

if __name__ == '__main__':

    fx = Function() # instanciando um objeto do tipo Function
    onr = RootNR(fx) # instanciando um objeto do tipo RootNR
    obs = RootBiss(fx)  # instanciando um objeto do tipo RootBiss
    print("a raiz da funcao utilizando o metodo de newton raphson e: %f" %onr.findRoot()) # chamando o metodo de calcula a raiz
    print("a raiz da funcao utilizando o metodo da biseccao e: %f" % obs.findRoot())  # chamando o metodo de calcula a raiz