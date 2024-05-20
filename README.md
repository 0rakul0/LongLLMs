---
license: afl-3.0
language:
- pt
pretty_name: codigo processual civil 2015
size_categories:
- 1K<n<10K
---

# SALVAMENTO do Dataset
```
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

```

# LEITURA do Dataset

```
from datasets import load_from_disk

dataset = load_from_disk('../data/cpc_2015_brasil/')

print(dataset)

```

# AMOSTRA do Dataset

| Livro    | Titulo       | Capitulo   | Secao | Subsecao | Artigo                                                                                                                        |
|----------|--------------|------------|-------|----------|-------------------------------------------------------------------------------------------------------------------------------|
| LIVRO I  | TÍTULO ÚNICO | CAPÍTULO I |       |          | Art. 1º O processo civil será ordenado, disciplinado e interpretado conforme os valores e as normas fundamentais estabelecidos na Constituição da República Federativa do Brasil, observando-se as disposições deste Código. |
| LIVRO I  | TÍTULO ÚNICO | CAPÍTULO I |       |          | Art. 2º O processo começa por iniciativa da parte e se desenvolve por impulso oficial, salvo as exceções previstas em lei.    |
| LIVRO I  | TÍTULO ÚNICO | CAPÍTULO I |       |          | Art. 3º Não se excluirá da apreciação jurisdicional ameaça ou lesão a direito.  1º É permitida a arbitragem, na forma da lei.  2º O Estado promoverá, sempre que possível, a solução consensual dos conflitos.  3º A conciliação, a mediação e outros métodos de solução consensual de conflitos deverão ser estimulados por juízes, advogados, defensores públicos e membros do Ministério Público, inclusive no curso do processo judicial. |
| LIVRO I  | TÍTULO ÚNICO | CAPÍTULO I |       |          | Art. 4º As partes têm o direito de obter em prazo razoável a solução integral do mérito, incluída a atividade satisfativa. |
| LIVRO I  | TÍTULO ÚNICO | CAPÍTULO I |       |          | Art. 5º Aquele que de qualquer forma participa do processo deve comportar-se de acordo com a boa-fé.                            |
