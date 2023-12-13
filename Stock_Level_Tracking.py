import pandas as pd


def stock_lvl():

    nome = 'Products.csv'

    p_df = pd.read_csv(nome)

    condicao_critica = p_df['Quantidade'] < p_df['Qtd.Min']
    
    tudo_certo = True

    if any(condicao_critica):
        
        tudo_certo = False
        print('\n')
        print("Alert: Some products have less than the minimum quantity in stock! Please do a purchase order!")
        print('\n')
        print(p_df[condicao_critica][['Produto','Tipo','Modelo', 'Quantidade', 'Qtd.Min']])
        print("----")


    elif tudo_certo:

        print('\n')
        print('Everything is right. No products below critical or ideal values.')
