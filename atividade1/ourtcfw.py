""" 
Descrevendo o Problema -  Running a single test from unittest TestCase via the command line
O usuário descreve que o time dele possui uma classe chamada OurTcFw que seria uma estrutura base do seu programa.
Ele também menciona que possui outros casos de Teste como o testMyCase.py

A dúvida dele é basicamente, se ele pode executar via linha de comando apenas um teste em especifico, sem a necessidade de executar os outros teste!

"""
import unittest

class OurTcFw(unittest.TestCase):
    def setUp(self):
        # Something 
        pass # usei o pass já que o usuário não especificou o que de fato havia nesta classe.

    # Other stuff that we want to use everywhere
    

