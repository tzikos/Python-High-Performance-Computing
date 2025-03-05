#!/bin/bash
#BSUB -J cache_test
#BSUB -n 8
#BSUB -q hpc
#BSUB -W 2
#BSUB -o outputs/output_%J.out
#BSUB -e outputs/error_%J.err
#BSUB -u s242798@dtu.dk
#BSUB -B 
#BSUB -N 
#BSUB -R "select[model==XeonGold6126]"
#BSUB -R "rusage[mem=2G]"
#BSUB -R "span[hosts=1]"

cd ~/02613/Python-High-Performance-Computing/Week3

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

python ex2_1.py 256
python ex2_1.py 512
python ex2_1.py 1024