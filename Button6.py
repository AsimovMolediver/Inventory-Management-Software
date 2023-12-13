import pandas as pd
import cv2
from pyzbar.pyzbar import decode

p_df = pd.read_csv('Products.csv')
p_df = pd.DataFrame(p_df)

def read_code128(frame):
    barcodes = decode(frame)
    for barcode in barcodes:
        if barcode.type == 'QRCODE':
            code128_data = barcode.data.decode('utf-8')
            return code128_data
    return None

def return_code_data(code128_data):
    return code128_data


def opt6():
    global p_df
    cap = cv2.VideoCapture(0)

    print("Câmera aberta! Centralize o código de barras (Tipo QRCode) e certifique-se de estar visível. Com a câmera aberta pressione q para sair.")
    cnt = 0
    while True:
        cnt += 1
        _, frame = cap.read()

        # Adicionar uma borda ao redor da área desejada
        border_thickness = 2
        border_color = (0, 255, 0)  # Cor no formato BGR (verde)
        frame_with_border = cv2.copyMakeBorder(frame, border_thickness, border_thickness, border_thickness, border_thickness, cv2.BORDER_CONSTANT, value=border_color)

        # Chamar a função para ler o código de barras Code 128
        code128_data = read_code128(frame)

        # Exibir o frame com a borda
        cv2.imshow('Câmera', frame_with_border)

        # Armazenar o valor do código de barras
        if code128_data:
            print(f'\nCódigo Code 128 detectado: {code128_data}\n')
            lista = [item.strip() for item in code128_data.split(",")]
            new_df = pd.DataFrame([{'Produto': lista[0], 'Tipo': lista[1], 'Modelo': lista[2], 'Cor': lista[3], 
                                    'Tamanho': lista[4], 'Quantidade': lista[5], 'Preço': lista[6]}])
            existing_index = p_df[(p_df['Produto'] == lista[0]) & (p_df['Tipo'] == lista[1]) & (p_df['Modelo'] == lista[2])].index

            if not existing_index.empty:

                soma = int(new_df.at[0, 'Quantidade'])
                # Se existir, atualize apenas a quantidade
                p_df.at[existing_index[0], 'Quantidade'] += soma
                cv2.destroyAllWindows()
                p_df.to_csv('Products.csv', index=False)
                break
            else:
                # Se não existir, adicione a nova linha
                p_df = pd.concat([p_df, new_df], ignore_index=True)
                p_df.to_csv('Products.csv', index=False)
                # Você pode armazenar a variável 'code128_data' como preferir
                # Por exemplo, se deseja armazenar em uma lista, use: minha_lista.append(code128_data)

                # Sair do loop quando a tecla 'q' for pressionada
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if(cnt > 100000):
            cv2.destroyAllWindows()
            break

    # Liberar os recursos
    print(p_df)
    cap.release()
    cv2.destroyAllWindows()
