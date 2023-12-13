import pandas as pd

nome = 'Products.csv'

p_df = pd.read_csv(nome)

nome = 'Calculo.csv'

c_df = pd.read_csv(nome)

nome = 'Total.csv'

t_df = pd.read_csv(nome)

def opt4():

    c_df['Valores'] = p_df['Quantidade'] * p_df['Preço']

    total_value = c_df['Valores'].sum()

    t_df = pd.DataFrame({'Total': [total_value]})

    t_df.to_csv('Total.csv', index=False)

    print('\n')
    print(f'O Valor total em inventário é: {total_value}')
    print('\n')
