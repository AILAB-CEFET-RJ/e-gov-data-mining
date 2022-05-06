# e-gov-data-mining
Projeto de mineração de dados em Notas Fiscais Eletrônicas (NFE)

## Requirements
Conda 4.11.0 or latest
Docker 20.10.14 or latest

## Install
In terminal, type:
```shell
./setup.sh
```
The above script will setup a conda environment to run scripts and also build a docker image to run fastText.

## Workflow
### Activate conda environment
```shell
conda activate egov
```

### Run the pipeline below
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
* RUN `training/train_test_split.py`

### Run fastText docker container
```shell
docker run --rm -it -v $PWD:/home fasttext /bin/bash
```

### Model training (from fastText docker container prompt)
```shell
fasttext supervised -input datasets/data.train.txt -output model/model
```

### Model test
```shell
fasttext test model/model.bin datasets/data.test.txt
```

The output of test will be displayed similar as below, where `P@1` and `R@1` are `Precision` and `Recall` values respectively.
```shell
N       734
P@1     0.00681
R@1     0.00681
```

### Get predictions of each sample
```shell
fasttext predict model/model.bin datasets/data.test.txt
```

## Deactivating docker container and conda environment

In fastText docker container prompt, type:
```shell
exit
```
To deactivate conda environment, type:
```shell
conda deactivate
```
