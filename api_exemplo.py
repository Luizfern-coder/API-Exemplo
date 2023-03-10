# -*- coding: utf-8 -*-
"""API Exemplo.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Iog8HPM14GQL_F-_B6QTA6-XER4w8acl

## API Exemplo

Queremos pegar a cotação do dólar de forma automática e atualizada, como fazemos?
"""

pip install twilio

import requests
import json

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json()
cotacao_dolar = cotacoes['USDBRL']['bid']
#print(cotacoes)
print(cotacao_dolar)