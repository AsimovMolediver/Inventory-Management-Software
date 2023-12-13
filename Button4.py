import pandas as pd

nome = 'Products.csv'

p_df = pd.read_csv(nome)

nome = 'Calculo.csv'

c_df = pd.read_csv(nome)

nome = 'Total.csv'

t_df = pd.read_csv(nome)

def opt4():

    while True:

        nome_produto = input("\nShow? (Y or N): ")
            
        if nome_produto == 'N':
            break

        else:

            c_df['Valores'] = p_df['Quantidade'] * p_df['Preço']

            total_value = c_df['Valores'].sum()

            t_df = pd.DataFrame({'Total': [total_value]})

            t_df.to_csv('Total.csv', index=False)

            print('\n')
            print(f'The total value in inventory is: {total_value}')
            print('\n')

