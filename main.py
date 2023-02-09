#1)IMPORTAR BIBLIOTECAS: TKINTER, TTK, CPROFILE => lABEL
#2)CRIAR INTERFACE GRÁFICA
    #1 DESCRIÇÃO
    #2 TIPO DE UNIDADE
    #3 QUANTIDADE D TIPO DA UNIDADE
#3)CRIAR INTELIGÊNCIA DA INTERFACE GRÁFICA
#4)FUNÇÃO

import tkinter as tk
from cProfile import label
from tkinter import ttk, Tk
import datetime as dt
from typing import List, Any

import pandas as pd
import openpyxl


materiais = pd.read_excel('materiais.xlsx', engine='openpyxl')

lista_codigos = []
lista_tipos = ['Galão', 'Caixa', 'Saco', 'Unidade', 'Metro', 'Quilo']

#CRIAR FUNÇÃO
def inserir_codigo():
    descricao = entry_descricao.get()
    tipo = combobox_selecionar_tipo.get()
    quantidade = entry_quantidade.get()
    data_criacao = dt.datetime.now()
    data_criacao = data_criacao.strftime('%d/%m/%a %h:%m')
    codigo = materiais.shape[0] + len(lista_codigos)+1
    codigo_str = 'COD-{}'.format(codigo)
    lista_codigos.append((codigo_str, descricao, tipo, quantidade, data_criacao))

janela: Tk = tk.Tk()

#titulo da janela
janela.title('Ferramenta de cadastro de materiais')

#Rótulo da tela
label_descricao = tk.Label(text='Descrição do material')
label_descricao.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

#espaço para dados de entrada

entry_descricao = tk.Entry()
entry_descricao.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

label_tipo_unidade = tk.Label(text='Tipo de unidade do material')
label_tipo_unidade.grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)

#cria uma lista suspensa de seleção
combobox_selecionar_tipo = ttk.Combobox(values=(lista_tipos))
combobox_selecionar_tipo.grid(row=3, column=1, padx=10, pady=10, sticky='nswe', columnspan=2)

#LABEL = RÓTULO
label_quantidade = tk.Label(text='Quantidade na unidade de material')
label_quantidade.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)

#ENTRY = ENTRADA DE INFORMAÇÕES
entry_quantidade = tk.Entry()
entry_quantidade.grid(row=4, column=1, padx=10, pady=10, sticky='nswe', columnspan=2)

#CRIAR BOTÃO

botao_criar_codigo = tk.Button(text='Criar código')# command=inserir_codigo)
botao_criar_codigo.grid(row=5, column=0,padx=10, pady=10, sticky='nswe',columnspan=4)

janela.mainloop()

novo_material = pd.DataFrame(lista_codigos, columns=['Código', 'Descricao', 'Tipo', 'Quantidade', 'Data Criação'])
materiais = materiais._append(novo_material, ignore_index=True)
materiais.to_excel('materiais.xlsx', index=False)





