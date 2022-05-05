# e-gov-data-mining
Projeto de mineração de dados em Notas Fiscais Eletrônicas (NFE)


## Requirements

Conda 4.11.0 or latest

## Install conda environment

In terminal, type:
```
conda env create -f config/environment.yml
```

## Activate environment
```
conda activate egov
```

## Deactivate environment
```
conda deactivate
```

## Pipeline
* RUN `pre_processamento/pre_proc_anvisa.ipynb`
* RUN `pre_processamento/pre_proc_medicamentos.ipynb`
* RUN `data_augmentation/medicamentos_augmentation.sh`
* RUN `data_augmentation/anvisa_prod_augmentation.sh`
* RUN `data_augmentation/anvisa_pa_augmentation.sh`
* MOVE `datasets/medicamentos/medicamentos_aumentado.csv` TO `datasets/medicamentos/augmented/medicamentos_aumentado.csv`
* MOVE `datasets/avisa/anvisa_principio_ativo_aumentado.csv` TO `datasets/anvisa/augmented/anvisa_principio_ativo_aumentado.csv`
* MOVE `datasets/avisa/anvisa_produto_aumentado.csv` TO `datasets/anvisa/augmented/anvisa_produto_aumentado.csv`
* RUN `pre_processamento/pre_proc_anvisa_augmented.ipynb`
* RUN `pre_processamento/pre_proc_medicamentos_augmented.ipynb`
* RUN `ean_key_map_builder` (not implemented)
* RUN `pre_processamento/mapeamento_ean_chave.ipynb`
* RUN `oversampling/oversampling.py`
