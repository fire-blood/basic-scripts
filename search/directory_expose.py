#!/usr/bin/env python 

#########################################################################
#   Repositorio:    Basic Scripts                                       #
#   Nome:           Directory Expose                                    #
#   Descrição:      Identifica arquivos e diretórios expostos           #
#   Autor:          Carine Constantino                                  #
#   Versão:         1.0                                                 #
#   Data:           05/07/2020                                          #
#   Python Version: 3.6.9                                               #
#   Função:         Scripts para identificar arquivos e/ou diretórios   #
#                   expostos em uma aplicação web.                      #
#########################################################################



import requests
from datetime import datetime
from pyfiglet import Figlet
import sys

print('-------------------------------------------------------------')
desenho  = Figlet(font='eftiwall')
banner_desenho = desenho.renderText('rtz')
fonte = Figlet(font='contessa')
banner_fonte = fonte.renderText('Directory Expose')

print(banner_desenho)
print(banner_fonte)
print('-------------------------------------------------------------')
print('Create By: Carine Constantino - seginfo.threatintel@gmail.com')
print('-------------------------------------------------------------')

print('-------------------------------------------------------------')
url = input("URL to Scan: ")
sel_file = input("Path to dirs file: ")
open_file = open(sel_file, "r")
read_file = open_file.readlines()


def validacao_url():

        verifica = requests.get(url)
        status = verifica.status_code
        if status == 200:
            print('\n-------------------------------------------------------------')
            print("VERIFICA ACESSO\n")
            print("Status UP -",status,"\n")
        else: 
            print("URL Inacessível", status, "\n")

def craw_url():

    for linha in read_file:
        req = requests.get(url + '/' + linha.rstrip())
        status = req.status_code
        print('URL Testing - ', req.url)
        print('Response Status -', req.status_code)
            
validacao_url()
craw_url()
