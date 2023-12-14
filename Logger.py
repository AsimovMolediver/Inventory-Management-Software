import csv
from datetime import datetime
import pandas as pd

def registrar_log(funcao, linha_modificada):
    data_hora_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = {'DataHora': data_hora_atual, 'Funcao': funcao, 'LinhaModificada': linha_modificada}
    with open('log.csv', 'a', newline='') as log_file:
        log_writer = csv.DictWriter(log_file, fieldnames=['DataHora', 'Funcao', 'LinhaModificada'])
        if log_file.tell() == 0:
            log_writer.writeheader()
        log_writer.writerow(log_entry)


def registrar_log7(**linha_modificada):

    registrar_log('VENDA',linha_modificada)
    print("\n")



def imprimir_csv():
    nome = 'log.csv'
    try:
        df = pd.read_csv(nome, encoding='utf-8')
    except UnicodeDecodeError:
        # Se ocorrer um erro, tente outro encoding
        df = pd.read_csv(nome, encoding='latin-1')
    
    print(df)
