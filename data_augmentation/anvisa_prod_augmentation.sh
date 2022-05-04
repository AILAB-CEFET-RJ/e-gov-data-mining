#!/bin/bash

python data_augmentation.py "../datasets/anvisa/anvisa.csv" "../datasets/anvisa/anvisa_produto_aumentado.csv" anvisa 5 --use_col produto

