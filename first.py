from fpdf import FPDF

arquivo = input("Digite o caminho do seu arquivo: ")
arquivo = arquivo.strip('"')

if (arquivo == ""):
    print("Você deve digitar o caminho do seu arquivo")
    exit()

formato = arquivo.split(".")
ultimo = formato[-1]

if (ultimo.lower() == "txt"):
    file = arquivo.split("\\")
    name_file = file[-1]
    with open(arquivo, 'r', encoding='utf-8') as a:
        conteudo = a.read()
        pdf = FPDF()
        pdf.add_page()
        pdf.add_font('Dejavu', '', 'DejavuSans.ttf')
        pdf.set_font("Dejavu", '', 16)
        pdf.multi_cell(0,10, txt=conteudo)
        pdf_name = name_file.rsplit('.', 1)[0] + ".pdf"
        pdf.output(pdf_name)
        print("PDF gerado com sucesso")
elif (ultimo.lower() == "jpeg" or ultimo.lower() == "png"):
        file = arquivo.split("\\")
        name_file = file[-1]
        pdf = FPDF()
        pdf.add_page()
        pdf.image(arquivo, x=0, y=0, w=210, h=297)
        pdf_name = input("Nome do seu arquivo:")
        pdf.output(pdf_name + ".pdf") 
