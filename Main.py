import pandas as pd

def add_item(df, product, type, model, color, size, quantity):
    
    new_row = pd.DataFrame({'Produto': [product], 'Tipo': [type], 'Modelo': [model], 'Cor': [color], 'Tamanho': [size], 'Quantidade': [quantity]})

    return pd.concat([df, new_row], ignore_index=True)

def update_item(df, index, column, new_value):

  df.at[index, column] = new_value
  return df

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

    1 - Add/Update
    2 - Update Item
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

    elif action =='2':

        print("Choose a column to update(Enter the class you want to edit):")
        print(df.columns)

        column = input('')
        print("\nAvailable items:")
        print(df.to_string(index=True))

        try:
            index = int(input('\nEnter the index of the item to update: '))
            if 0 <= index < len(df):
                new_value = input(f'Enter the new value for {column}: ')
                df = update_item(df, index, column, new_value)
                df.to_csv('teste.csv', index=False)
                print("Item updated successfully!")
            else:
                print("Invalid index. Please enter a valid index.")
        except ValueError:
            print("Invalid input. Please enter a valid index.")

    elif action == '0':
        break
