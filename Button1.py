import pandas as pd
import Button3
from Logger import registrar_log

def print_df(df):
    print(df)

def add_item(df, product, type, model, color, size, quantity, price, ideal, min):
    
    new_row = pd.DataFrame({'Produto': [product], 'Tipo': [type], 'Modelo': [model], 'Cor': [color], 
                            'Tamanho': [size], 'Quantidade': [quantity], 'Preço': [price], 'Qtd.Ideal':[ideal],'Qtd.Min': [min]})
    return pd.concat([df, new_row], ignore_index=True)

def add_item_and_update_s(p_df, product, type, model, color, size, quantity, price, ideal, min):

    last_index = p_df.index[-1] if not p_df.empty else 0

    p_df = add_item(p_df, product, type, model, color, size, quantity, price, ideal, min)

    registrar_log('add_item_and_update_s', last_index + 1)

    return p_df

def opt1():
# Novo Item!

    nome = 'Products.csv'

    p_df = pd.read_csv(nome)

    nome = 'Suppliers.csv'

    s_df = pd.read_csv(nome)

    print('\nThe actual itens:\n')
    print_df(p_df)
    print("\n")

    print("Please enter in this sequence atributes product (with no accent):")

    product = input('Product: ')
    type = input('Type: ')
    model = input('Model: ')
    color = input('Color: ')
    size = input('Size: ')
    quantity = input('Quantity: ')
    price = input('Preço: ')
    ideal = input('Qtd.Ideal: ')
    min = input('Qtd.Min: ')

        # Se não tiver quantidade vai ficar sendo zero
    quantity = 0 if not quantity else quantity

        # Chama a função para adicionar os itens
    p_df = add_item_and_update_s(p_df, product, type, model, color, size, quantity, price, ideal, min)

    print("Item added successfully!")
    print_df(p_df)
    print("\n")

    p_df.to_csv("Products.csv", index=False)

    print('Actual suppliers:')
    print("\n")
    print_df(s_df)
    print("\n")

    sup = input('Would you like to add a new supplier to this item? Y/N: ')

    if sup == 'Y':

            supplier = input('Supplier: ')
            contact = ''
            email = ''
            CEP = ''
            CNPJ = ''
            s_df = Button3.add_s(s_df, supplier, product, contact, email, CEP, CNPJ)
            s_df.to_csv('Suppliers.csv', index=False)

            print('New Supplier! To update the informations select the option 3.')
            print('\n')
            print(s_df)
            print('\n')

    elif sup == 'N':

            print('Ok!')
            print('\n')


