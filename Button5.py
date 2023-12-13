import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from datetime import date, datetime

data_hora_atual = datetime.now().strftime('%Y%m%d_%H%M%S')

# Função para carregar fornecedores do CSV
def carregar_fornecedores_csv():
    try:
        s_df = pd.read_csv('Suppliers.csv')
        return s_df
    except FileNotFoundError:
        print("Arquivo CSV 'Suppliers.csv' não encontrado. Certifique-se de que o arquivo está na mesma pasta que o script.")
        return None

# Função para exibir a lista de fornecedores e permitir a escolha
def selecionar_fornecedor(s_df):
    print("Selecione um fornecedor:")
    print(s_df)
    
    try:
        fornecedor_index = int(input("Digite o número do fornecedor desejado: "))
        return s_df.iloc[fornecedor_index].to_dict()
    except (ValueError, IndexError):
        print("Opção inválida. Certifique-se de selecionar um número válido.")
        return None

def opt5():

    s_df = carregar_fornecedores_csv()

    # Verificar se os fornecedores foram carregados com sucesso
    if s_df is not None:
        # Chamar a função para selecionar um fornecedor
        dados_fornecedor = selecionar_fornecedor(s_df)

        if dados_fornecedor is not None:
            # Chamar a função para criar a ordem de compra
            output_pdf = f'OC_{data_hora_atual}.pdf'
            criar_template_ordem_compra(output_pdf, dados_fornecedor)
    else:
        print("Erro ao carregar dados dos fornecedores. Certifique-se de que o arquivo CSV está correto.")


def criar_template_ordem_compra(output_pdf, dados_fornecedor):
    # Configurar o PDF usando reportlab
    pdf = SimpleDocTemplate(output_pdf, pagesize=letter, rightMargin=20, leftMargin=20, topMargin=30, bottomMargin=20)
    styles = getSampleStyleSheet()

    # Lista para armazenar os elementos do PDF
    elementos = []

    # Adicionar informações do fornecedor
    elementos.append(Paragraph("<u>Dados do Fornecedor</u>", styles['Heading1']))
    elementos.append(Spacer(1, 12))

    for chave, valor in dados_fornecedor.items():
        info_fornecedor = f"<b>{chave}:</b> {valor}"
        paragrafo = Paragraph(info_fornecedor, styles['BodyText'])
        elementos.append(paragrafo)
        elementos.append(Spacer(1, 6))

    # Adicionar tabela com detalhes dos itens
    elementos.append(Spacer(1, 12))
    elementos.append(Paragraph("<u>Detalhes dos Itens</u>", styles['Heading1']))
    elementos.append(Spacer(1, 6))

    cabecalho = ["Nome do Produto", "Tipo", "Quantidade", "Preço Unitário", "Subtotal"]
    dados_tabela = [cabecalho]

    valor_total = 0

    while True:
        nome_produto = input("Nome do Produto (ou 'exit' para encerrar): ")
        if nome_produto.lower() == 'exit':
            break

        tipo = input("Tipo: ")
        quantidade = int(input("Quantidade: "))
        preco_unitario = float(input("Preço Unitário: "))

        subtotal = quantidade * preco_unitario
        valor_total += subtotal
        dados_tabela.append([nome_produto, tipo, quantidade, f'R${preco_unitario:.2f}', f'R${subtotal:.2f}'])

    tabela = Table(dados_tabela, style=[
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])

    elementos.append(tabela)
    elementos.append(Spacer(1, 12))

    # Adicionar o valor total
    elementos.append(Paragraph(f"<b>Valor Total:</b> R${valor_total:.2f}", styles['Heading2']))

    # Adicionar a data de emissão
    elementos.append(Spacer(1, 12))
    data_atual = date.today().strftime('%d/%m/%Y')
    elementos.append(Paragraph(f"<b>Data de Emissão:</b> {data_atual}", styles['BodyText']))

    # Construir o PDF
    pdf.build(elementos)

    print(f"Template de ordem de compra salvo como {output_pdf}")

