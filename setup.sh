#!/bin/bash

# conda environment
conda env create -f config/environment.yml

# fasttext docker image
docker build -t fasttext .
