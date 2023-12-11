import pandas as pd
import Button1
import Button2
import Button3

data = {'Produto' : ['Tira', 'Forma', 'Borracha'], 
        'Tipo': ['Lisa', 'Metálica', '90/10'],
        'Modelo': ['Aviador','Regular', 'Comum'],
        'Cor': ['Branca', '--',  'Azul/Vermelho'],
        'Tamanho': ['22', '22', '90cm'],
        'Quantidade': [10, 1, 2]
}

fornecedores = {'Produto' : ['Tira', 'dhgsghdgsdg', '5760600']}

p_df = pd.DataFrame(data)
s_df = pd.DataFrame(fornecedores)

#Button3.listar_s(s_df, 'Tira')

#p_df.to_csv('Products.csv', index=False)
#s_df.to_csv('Suppliers.csv', index=False)

while True:
    print("""
    Welcome!

    Please, select your option:

    1 - Add
    2 - Update Item
    3 - Supplier Management
    0 - exit
    """)

    action = input('')

    if action == '1':
        
        Button1.opt1()

    elif action =='2':

        Button2.opt2()

    elif action == '3':

        Button3.opt3()

    elif action == '0':
        break