import re
import pandas as pd

def split_into_sections(text):
    sections = []

    # Dividir o texto em livros
    livros = re.split(r'(LIVRO [ÚNICO|IVXLCDM|COMPLEMENTAR]+)', text)[1:]

    for i in range(0, len(livros), 2):
        livro_title = livros[i].strip()
        livro_content = livros[i + 1].strip()

        # Verificar se o livro contém capítulos ou vai diretamente para os artigos
        if 'CAPÍTULO' in livro_content:
            # Dividir o livro em títulos
            titulos = re.split(r'(TÍTULO [ÚNICO|IVXLCDM]+)', livro_content)[1:]

            for j in range(0, len(titulos), 2):
                titulo_title = titulos[j].strip()
                titulo_content = titulos[j + 1].strip()

                # Dividir o título em capítulos
                capitulos = re.split(r'(CAPÍTULO [ÚNICO|IVXLCDM]+)', titulo_content)[1:]

                for k in range(0, len(capitulos), 2):
                    capitulo_title = capitulos[k].strip()
                    capitulo_content = capitulos[k + 1].strip()

                    # Dividir o capítulo em seções
                    if 'Seção' in capitulo_content:
                        secoes = re.split(r'(Seção [A-Z]+)', capitulo_content)[1:]

                        for m in range(0, len(secoes), 2):
                            secao_title = secoes[m].strip()
                            secao_content = secoes[m + 1].strip()

                            # Dividir a seção em subseções
                            if 'Subseção' in secao_content:
                                subsecoes = re.split(r'(Subseção [A-Z]+)', secao_content)[1:]

                                for n in range(0, len(subsecoes), 2):
                                    subsecao_title = subsecoes[n].strip()
                                    subsecao_content = subsecoes[n + 1].strip()

                                    # Dividir a subseção em artigos
                                    artigos = re.split(r'(Art\.\s+\d+.\s|Art.\s+\d.\d+.\s|Art\.\s+\d+[\w]*\.\s)', subsecao_content)

                                    for o in range(1, len(artigos), 2):
                                        artigo_title = artigos[o].strip()
                                        artigo_content = artigos[o + 1].strip()
                                        section = (
                                            livro_title, titulo_title, capitulo_title, secao_title, subsecao_title,
                                            f"{artigo_title} {artigo_content}")
                                        sections.append(section)
                            else:
                                # Dividir a seção em artigos
                                artigos = re.split(r'(Art\.\s+\d+.\s|Art.\s+\d.\d+.\s|Art\.\s+\d+[\w]*\.\s)', secao_content)

                                for n in range(1, len(artigos), 2):
                                    artigo_title = artigos[n].strip()
                                    artigo_content = artigos[n + 1].strip()
                                    section = (
                                        livro_title, titulo_title, capitulo_title, secao_title, '',
                                        f"{artigo_title} {artigo_content}")
                                    sections.append(section)
                    else:
                        # Dividir o capítulo em artigos
                        artigos = re.split(r'(Art\.\s+\d+.\s|Art.\s+\d.\d+.\s|Art\.\s+\d+[\w]*\.\s)', capitulo_content)

                        for m in range(1, len(artigos), 2):
                            artigo_title = artigos[m].strip()
                            artigo_content = artigos[m + 1].strip()
                            section = (
                                livro_title, titulo_title, capitulo_title, '', '',
                                f"{artigo_title} {artigo_content}")
                            sections.append(section)
        else:
            # Dividir o livro em artigos
            artigos = re.split(r'(Art\.\s+\d+.\s|Art.\s+\d.\d+.\s|Art\.\s+\d+[\w]*\.\s)', livro_content)

            for j in range(1, len(artigos), 2):
                artigo_title = artigos[j].strip()
                artigo_content = artigos[j + 1].strip()
                section = (
                    livro_title, '', '', '', '',
                    f"{artigo_title} {artigo_content}")
                sections.append(section)

    return sections



with open("../data/cpc_2015_cleaned.txt", "r", encoding="utf-8") as file:
    cleaned_text = file.read()

# Dividir o texto em seções por livros, títulos, capítulos, seções, subseções e artigos
sections = split_into_sections(cleaned_text)
df = pd.DataFrame(sections, columns=['Livro', 'Titulo', 'Capitulo', 'Secao', 'Subsecao',  'Artigo'])
df.to_parquet('../data/cpc_2015_cleaned.parquet', index=False)
df.to_csv('../data/cpc_2015_cleaned.csv', index=False)

with open("../data/cpc_2015_sections.txt", "w", encoding="utf-8") as file:
    for section in sections:
        file.write("\n".join(section) + "\n\n")
