#!/bin/bash
#BSUB -J cache_test
#BSUB -n 1
#BSUB -q hpc
#BSUB -W 1
#BSUB -o sleeper_%J.out
#BSUB -e sleeper_%J.err
#BSUB -u s242798@dtu.dk
#BSUB -B 
#BSUB -N 
#BSUB -R "select[model==XeonGold6126]"
#BSUB -R "span[hosts=1]"

cd ~/02613/Python-High-Performance-Computing/Week3

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

python ex3.py