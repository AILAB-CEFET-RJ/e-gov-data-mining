import pandas as pd
import numpy as np
import time

from imblearn.over_sampling import RandomOverSampler

data_medicamentos = '../datasets/medicamentos/augmented/medicamentos_aumentado_preproc_mapped.csv'
data_anvisa_prod = '../datasets/anvisa/augmented/anvisa_produto_aumentado_preproc_mapped.csv'
data_anvisa_pa = '../datasets/anvisa/augmented/anvisa_principio_ativo_aumentado_preproc_mapped.csv'

df_medicamentos = pd.read_csv(data_medicamentos, sep=';', dtype=str)
df_anvisa_prod = pd.read_csv(data_anvisa_prod, sep=';', dtype=str)
df_anvisa_pa = pd.read_csv(data_anvisa_pa, sep=';', dtype=str)
print('data loaded')

df = pd.concat([df_medicamentos, df_anvisa_prod, df_anvisa_pa], ignore_index=True, sort=False)
print('data concatenated')
print('shape:', df.shape)

start = time.time()
ros = RandomOverSampler(random_state=0)
print('starting oversampling...')
X_resampled, y_resampled = ros.fit_resample(pd.DataFrame(df[['cod', 'descricao']]), df['chave'])
elapsed_time = (time.time() - start) / 60
print(f'oversampling finished after {elapsed_time} minutes')

df_oversampled = pd.concat([X_resampled, y_resampled], axis=1)
print('new shape:', df_oversampled.shape)

data_file = '../datasets/oversampled.csv'

print(f'saving file in {data_file}')
df_oversampled.to_csv(data_file,
                      sep=';',
                      header=df.columns,
                      index=False,
                      encoding='utf-8')
print('File saved')
