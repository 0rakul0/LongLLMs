from datasets import load_dataset
from datasets import Dataset
import pandas as pd

# Carregar os dados do arquivo de texto
df = pd.read_parquet('../data/cpc_2015_cleaned.parquet')

data = {
    "livro": df["Livro"],
    "capitulo": df["Capitulo"],
    "titulo": df["Titulo"],
    "secao": df["Secao"],
    "subsecao": df["Subsecao"],
    "artigo": df["Artigo"]
}

# Dividir o texto em seções
dataset = Dataset.from_pandas(pd.DataFrame(data))

dataset.save_to_disk('../data/cpc_2015_brasil')

print(dataset)
