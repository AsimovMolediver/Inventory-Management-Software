import pandas as pd 
from datetime import datetime
from Logger import registrar_log7

def update_item(p_df, index, column, new_value):
    new_value = int(new_value)
    p_df.at[index, 'Quantidade'] -= new_value
    return p_df

def history_df_exists():
    try:
        pd.read_csv('History.csv')
        return True
    except FileNotFoundError:
        return False

def opt7():
    nome = 'Products.csv'
    p_df = pd.read_csv(nome)

    print("""
******************
Sales and History
******************
          
1 - Sale
2 - History
0 - Exit
    """)
   
    ent = input('')

    if ent == '1':
        print('\nNew Sale!\n')
        print('Please, select the item that was sold and its quantity so we can update the inventory.\n')
        print(p_df.columns)

        column = 'Quantidade'
        print("\nAvailable items:")
        print(p_df.to_string(index=True))

        try:
            index = int(input('\nEnter the index of the item you sell to update: '))
            if 0 <= index < len(p_df):
                new_value = input(f'Enter the quantity of the item you sell: ')
                # Salvar a data e hora atual
                current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                # Atualizar o DataFrame
                p_df = update_item(p_df, index, column, new_value)
                # Salvar a linha modificada em outro arquivo CSV
                modified_row = p_df.iloc[index].copy()
                modified_row['DataHoraModificacao'] = current_datetime
                h_df = pd.DataFrame([modified_row])
                h_df.to_csv('History.csv', mode='a', header=not history_df_exists(), index=False)
                p_df.to_csv('Products.csv', index=False)
                log_info = {'action': 'SALE', 'index': index, 'datetime': current_datetime, **modified_row.to_dict()}
                registrar_log7(**log_info)
                print("Sale registered successfully!!")
            else:
                print("Invalid index. Please enter a valid index.")
        except ValueError:
            print("Invalid input. Please enter a valid index.")
    
    elif ent == '2':

        nome = 'History.csv'
        h_df = pd.read_csv(nome)

        print("""\n

        To track purchase orders, simply check the date and time in the PDF files generated.

        Here is the Sales History:

        \n""")
            
        print(h_df)
        
    while True:

            nome_produto = input("\nExit? (Y or N): ")
            
            if nome_produto == 'Y':
                break

            else:

                nome = 'History.csv'
                h_df = pd.read_csv(nome)

                print("""\n

                To track purchase orders, simply check the date and time in the PDF files generated.

                Here is the Sales History:

                \n""")
            
                print(h_df)


