import pandas as pd

def add_item(df, product, type, model, color, size, quantity):

    print("""Please, enter in this sequence:""")

    new_row = input('Product:'), input('Type:'), input('Model:'), input('Color:'), input('Size:'), input('Quantity:')

    new_row = pd.DataFrame({'Produto': [product], 'Tipo': [type], 'Modelo': [model], 'Cor': [color], 'Tamanho': [size], 'Quantidade': [quantity]})

    df = add_item(df, 'Macarrão', 'Não perecível', 'Penny', 'Qualquer', '100kg',200)

data = {'Produto' : ['Tira', 'Forma', 'Borracha', 'Símbolo','Cola','Couro'], 
        'Tipo': ['Grossa','Fina','Infantil','Regular','100', '90/10','70/30','Preto','Branco','Para Couro','Texturizado'],
        'Modelo': ['Aviador','Regular', 'Brilhante','Lisa','Texturizada','Padrão','Logotipo','TekBond','Courino'],
        'Cor': ['Branco', 'Preto','Azul','Vermelho','Rosa','Verde','Laranja','Ciano','Roxo','Prata','Dourado'],
        'Tamanho': ['20/21','22/23','24/25','26/27','28/29','30/31','32/33','34/35','36/37','38/39','40/41', '90cm','--','120cm','20g','Normal'],
        'Quantidade': [10]
}

df = pd.DataFrame(data)

#df.loc[df['Cor'] ==   'Qualquer', 'Quantidade'] = df.loc[df['Cor'] ==   'Qualquer', 'Quantidade'] - 5

df.to_csv('teste.csv', index=False)


while True:

  print("""Welcome!

  Please, select you option:

    1 - Add
    2 - Reorder Alerts
    3 - Supplier Management
    0 - exit

  """)

  action = input('')

  if action == '1':

    add_item('','','','','','','')

  elif action == '0':

    quit()