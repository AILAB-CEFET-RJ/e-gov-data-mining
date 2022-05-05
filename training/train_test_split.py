import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


# Codificação do arquivo oversampled
# 1 - registro original MEDICAMENTOS
# 2 - registro original ANVISA
# 3 - derivado de um registro SEFAZ (google scrapping)
# 4 - derivado de um registro ANVISA (google scrapping)

df = pd.read_csv('../datasets/oversampled.csv', sep=';')

# Obtendo somente os registros originais de medicamentos
df = df[df['cod'] == 1]

# Removendo duplicatas
df.drop_duplicates(inplace=True)
df.drop_duplicates(subset=['descricao'], inplace=True)

# Removendo classes que só possuem 1 único exemplo
dfg = df.groupby('chave')['descricao'].count().sort_values().reset_index()
keys_to_remove = dfg[dfg['descricao'] == 1]['chave']
df = df[~df['chave'].isin(keys_to_remove)]

# Split
_, df_test = train_test_split(df, test_size=0.2, stratify=df['chave'])

# Gravando em arquivo o conjunto de teste
df_test['label'] = '__label__' + df_test['chave'].astype(str)
df_test.drop(['cod', 'chave'], axis=1, inplace=True)
df_test = df_test[['label', 'descricao']]
np.savetxt('../datasets/data.test.txt', df_test, fmt='%s')
print('Amount of classes: ', df_test['label'].unique().shape[0])
print('Num of test records: ', df_test.shape[0])

# Remover do dataset aumentado todos os registros com descrição pertencente ao conjunto de teste
df = pd.read_csv('../datasets/oversampled.csv', sep=';')
df = df[~df['descricao'].isin(df_test['descricao'])]

# Gravando em arquivo o conjunto de treino
df['label'] = '__label__' + df['chave'].astype(str)
df.drop(['cod', 'chave'], axis=1, inplace=True)
df = df[['label', 'descricao']]
np.savetxt('../datasets/data.train.txt', df, fmt='%s')
print('Num train records: ', df.shape[0])
