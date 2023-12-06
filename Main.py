import pandas as pd

def add_item(df, product, type, model, color, size, quantity):
    
    new_row = pd.DataFrame({'Produto': [product], 'Tipo': [type], 'Modelo': [model], 'Cor': [color], 'Tamanho': [size], 'Quantidade': [quantity]})

    return pd.concat([df, new_row], ignore_index=True)

data = {'Produto' : ['Tira', 'Forma', 'Borracha'], 
        'Tipo': ['Lisa', 'Metálica', '90/10'],
        'Modelo': ['Aviador','Regular', 'Comum'],
        'Cor': ['Branca', '--',  'Azul/Vermelho'],
        'Tamanho': ['22', '22', '90cm'],
        'Quantidade': [10, 1, 2]
}

df = pd.DataFrame(data)

df.to_csv('teste.csv', index=False)

while True:
    print("""
    Welcome!

    Please, select your option:

    1 - Add
    2 - Reorder Alerts
    3 - Supplier Management
    0 - exit
    """)

    action = input('')

    if action == '1':
        # Novo Item!

        print("Please enter in this sequence:")

        product = input('Product: ')
        type = input('Type: ')
        model = input('Model: ')
        color = input('Color: ')
        size = input('Size: ')
        quantity = input('Quantity: ')

        # Se não tiver quantidade vai ficar sendo zero
        quantity = 0 if not quantity else quantity

        # Chama a função para adicionar os itens
        df = add_item(df, product, type, model, color, size, quantity)

        #print(df) # Debug

        df.to_csv('teste.csv', index=False) 

        print("Item added successfully!")


    elif action == '0':
        break
