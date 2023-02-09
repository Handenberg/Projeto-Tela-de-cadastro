import datetime as dt
import tkinter as tk
from tkinter import ttk
import pandas as pd

materiais = pd.read_excel('materiais.xlsx', engine='openpyxl')

lista_codigos = []
lista_tipos = ["Galão", "Caixa", "Saco", "Unidade"]

janela = tk.Tk()

# Criação da função


def inserir_codigo():
    descricao = entry_descricao.get()
    tipo = combobox_selecionar_tipo.get()
    quant = entry_quant.get()
    data_criacao = dt.datetime.now()
    data_criacao = data_criacao.strftime("%d/%m/%Y %H:%M")
    codigo = materiais.shape[0] + len(lista_codigos)+1
    codigo_str = "COD-{}".format(codigo)
    lista_codigos.append(codigo_str, descricao, tipo, quant, data_criacao)
    #entry_descricao.delete(0,999) #OPCIONAL
    #entry_quant.delete(0,999) #OPCIONAL

#PARA LIMPAR O FORMULÁRIO PODE-SE ADICIONAR AS LINHAS DA FUNÇÃO "LIMPAR' E COLOCA-LAS DIRETO NO BOTÃO "GERAR CÓDIGO"
def limpar():
    entry_descricao.delete(0,999)
    entry_quant.delete(0,999)



# Título da Janela

janela.title('Ferramenta de cadastro de materiais')

label_descricao = tk.Label(text="Descrição do Material")
label_descricao.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

entry_descricao = tk.Entry()
entry_descricao.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

label_tipo_unidade = tk.Label(text="Tipo da unidade do Material")
label_tipo_unidade.grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

combobox_selecionar_tipo = ttk.Combobox(values=lista_tipos)
combobox_selecionar_tipo.grid(row=3, column=2, padx=10, pady=10, sticky='nswe', columnspan=2)

label_quant = tk.Label(text="Quantidade na unidade de matetial")
label_quant.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

entry_quant = tk.Entry()
entry_quant.grid(row=4, column=2, padx=10, pady=10, sticky='nswe', columnspan=2)

botao_criar_codigo = tk.Button(text="Criar código", command=inserir_codigo)
botao_criar_codigo.grid(row=5, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)

botao_reset = tk.Button(text ="Limpar", command=limpar)
botao_reset.grid(row=5, column=2, padx=10, pady=10, sticky='nswe', columnspan=2)




janela.mainloop()

novo_material = pd.DataFrame(lista_codigos, columns=['Código', 'Descrição','Tipo', 'Quantidade', 'Data Criação'])
materiais = materiais._append(novo_material, ignore_index=True)
materiais.to_excel('materiais.xlsx', index=False)
